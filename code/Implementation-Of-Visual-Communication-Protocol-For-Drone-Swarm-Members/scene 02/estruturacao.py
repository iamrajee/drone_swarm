# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:37:01 2021

@author: laura
"""

import sim
import time, random, math
import movements, inicializacao


mensagem = None

class Navegation(object):
    def __init__(self, clientID, n_drones, z_coord, timeout, dist_max, eixo_x, eixo_y, resources):
        self.clientID = clientID
        self.state = [] #estados A, B, C, D, E, F ou G dos drones
        self.message_progress = []
        self.z_coord = z_coord
        self.timeout = timeout
        self.dist_max = dist_max
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.resources = resources
        self.is_watching = []
        self.v_pos = []
        inicializa = inicializacao.Inicializa(clientID, n_drones, z_coord, self.resources)
        self.resourceObj, self.resourcePos = inicializa.get_resources()
        inicializa.init_resources()
        (self.targetObj, self.targetPos, self.droneObj, self.dronePos) = inicializa.get_drones(n_drones)
        
        self.mensagem = movements.movimento(self.clientID, self.targetObj, self.targetPos, self.droneObj, self.dronePos)
        
        self.main(n_drones)
                
    
    
    def main(self, n_drones):
        count = []
        _find = [] #indica qual recurso o drone encontrou
        for i in range(n_drones):  #inicializa drones
            self.state.insert(i, 'A')
            self.message_progress.insert(i, 0)
            _find.insert(i,-1)
            count.insert(i,0) #controle de tempo navegando até parar para observar
            #inicializa posições
            self.targetPos[i][2] = self.z_coord
            pos = self.get_random_coords() 
            self.v_pos.insert(i,pos)            
        
        while True:
            for drone in range(n_drones):
                print(f'drone {drone} estado {self.state[drone]}')
                if self.state[drone] == 'A':
                    count[drone] += 1
                    self.keep_navigation(drone)
                    _find[drone] = self.check_range_drone(drone)
                    
                    if _find[drone] != -1: #significa que encontrou recurso
                        if not self.observe_around(drone, n_drones):
                            self.state[drone] = 'B'
                            print(f'Drone {drone} =>\tRecurso {self.resources[_find[drone]][0]} \n\tQuantidade: {self.resources[_find[drone]][1]}')
                            
                        
                elif self.state[drone] == 'B':
                    self.found_resource(drone)
                    count[drone] = 0
                
                elif self.state[drone] == 'C':
                    if not self.observe_around(drone, n_drones): #não tem drones mensageiros
                        self.state[drone] = 'A'
                    count[drone] = 0
                                
                
                elif self.state[drone] == 'D':
                    self.start_message_bin(drone, self.resources[_find[drone]][1])
                    count[drone] = 0
                
                elif self.state[drone] == 'E':
                    self.finish_message_bin(drone)
                    count[drone] = 0
                    
                elif self.state[drone] == 'F':
                    self.verify(drone, n_drones)
                    count[drone] = 0
                
                elif self.state[drone] == 'G':
                    self.take_resource(drone, _find[drone])
                    count[drone] = 0
                
                
                elif self.state[drone] == 'H':
                    self.back_origin(drone, _find[drone])
                    
                if count[drone] == 100:
                    self.state[drone] = 'C'
                    count[drone] = 0
                    
            
                
           
    def keep_navigation(self, drone):
        """
        drone navega no ambiente
        """
        self.is_watching.insert(drone, -1)

        self.targetPos[drone][0] += self.v_pos[drone][0]
        self.targetPos[drone][1] += self.v_pos[drone][1]
        
        #verifica se chegou ao limite do ambiente
        while not (self.testa_coordenadas(self.targetPos[drone][0], self.targetPos[drone][1])):
            self.v_pos[drone] = self.get_random_coords()
            self.targetPos[drone][0] += self.v_pos[drone][0]
            self.targetPos[drone][1] += self.v_pos[drone][1]
            
        
        timeout = time.time() + self.timeout
        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            self.dronePos[drone] = self.mensagem.fix_coords(self.dronePos[drone]) 


    def get_random_coords(self):
        """
        gera números randomicos para navegar aleatoriamente pelo ambiente
        """
        while True:
            x = random.uniform(-0.4, 0.4)
            y = random.uniform(-0.4, 0.4)

            if self.testa_coordenadas(x, y):
                break
            
        return [x,y,self.z_coord]


    def testa_coordenadas(self, curr_x, curr_y):
        """
        testa para saber se pode prosseguir ou se ultrapassa o limite imposto
        """
        if abs(curr_x) > abs(self.eixo_x) or abs(curr_y) > abs(self.eixo_y):
            return False
        else:
            return True
        
        
    def check_range_drone(self, drone, resource=True, drone_aux=-1):
        """
        verifica raio de detecção de um drone com um recurso ou outro drone
        """
        x_drone = self.targetPos[drone][0]
        y_drone = self.targetPos[drone][1]

        if resource: #verifica distancia do recurso
            retorno = -1
            for i in range(len(self.resources)):
                x_resource = self.resourcePos[i][0]
                y_resource = self.resourcePos[i][1]
                                  
                distancia = math.sqrt(math.pow(x_resource - x_drone, 2) + math.pow(y_resource - y_drone, 2))

                if distancia <= self.dist_max:
                    if self.resources[i][1] == 0:
                        print(f'Objeto {self.resources[i][0]} com 0 recursos')
                    else:
                        retorno = i #armazena posição do recurso perto
                        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, [self.targetPos[drone][0], self.targetPos[drone][1], self.z_coord], sim.simx_opmode_continuous)
                        break
           
        else: #verifica distancia entre drones
            retorno = False
            x_drone_aux = self.targetPos[drone_aux][0]
            y_drone_aux = self.targetPos[drone_aux][1]

            distancia = math.sqrt(math.pow(x_drone_aux - x_drone, 2) + math.pow(y_drone_aux - y_drone, 2))

            if distancia <= self.dist_max:
                retorno = True
            
        return retorno    


    def found_resource(self, drone):
        """
        faz movimento de reconhecimento de recurso
        """        
        #aguarda drone chegar no target
        timeout = time.time() + self.timeout
        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            self.dronePos[drone] = self.mensagem.fix_coords(self.dronePos[drone])
        
        #movimento inicial para indicar que achou um recurso
        self.message_progress[drone] += 1
        self.do_movement('quadrado', drone, self.message_progress[drone])
        if self.message_progress[drone] == 8:
            self.state[drone] = 'D'
            self.message_progress[drone] = 0
        
   
    def observe_around(self, drone, n_drones):
        """
        Observa envolta para ver se tem algum drone realizando mensagem
        """
        check = False
        vizinhos = [v for v in range(n_drones) if v != drone]
        for v in vizinhos:
             if self.check_range_drone(drone=drone, resource=False, drone_aux=v) and (self.state[v] == 'B' or self.state[v] == 'F'):
                 self.is_watching[drone] = v
                 check = True
                 self.state[drone] = 'F'
                 break
        
        return check
        


    def start_message_bin(self, drone, resource):
        """
        riqueza do recurso tranformada em binário para envio da mensagem
        """
        _bin = ""
        aux = format(resource, '04b')
        for a in aux:
            if a == '0':
                _bin = _bin + "00"
            else:
                _bin = _bin + "11"
        
        print(f'drone {drone} : {_bin}')
        self.message_progress[drone] += 1
        b = self.message_progress[drone] - 1        
        if _bin[b] == '0':
            self.do_movement('vertical', drone, self.message_progress[drone])
                           
        elif _bin[b] == '1':
            self.do_movement('horizontal', drone, self.message_progress[drone])
      
        if self.message_progress[drone] == 8:
            self.state[drone] = 'E'
            self.message_progress[drone] = 0  
            
    
    def finish_message_bin(self, drone):
        """
        realiza mensagem para demonstrar fim de mensagem binária
        """        
        #aguarda drone chegar no target
        timeout = time.time() + self.timeout
        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            self.dronePos[drone] = self.mensagem.fix_coords(self.dronePos[drone])
        
        #movimento inicial para indicar que achou um recurso
        self.message_progress[drone] += 1
        self.do_movement('triangulo', drone, self.message_progress[drone])
        if self.message_progress[drone] == 6:
            self.state[drone] = 'F'
            self.message_progress[drone] = 0
        


    def verify(self, drone, n_drones):
        """
        aguarda resposta do drone observador ou faz a mensagem de reconhecimento
        """
        aux = 0
        #drone mensageiro
        if self.is_watching[drone] == -1:
            vizinhos = [v for v in range(n_drones) if v != drone]
            for v in vizinhos:
                #verifica se drone observador está assistindo este determinado drone
                if self.is_watching[v] == drone:
                    if self.state[v] != 'F': #verifica se terminou a mensagem
                        self.state[drone] = 'G'
                else:
                    aux += 1
            
            if aux == len(vizinhos): #verifica se não tem drones assistindo
                self.state[drone] = 'G'
            
        else: #drone observador
            if self.state[self.is_watching[drone]] == 'F': #se drone já finalizou a mensagem binaria
                self.message_progress[drone] += 1
                self.do_movement('ampulheta', drone, self.message_progress[drone])
                if self.message_progress[drone] == 4:
                    self.state[drone] = 'G'
                    self.is_watching[v] = -1
                    self.message_progress[drone] = 0
            

    def take_resource(self, drone, resource):
        """
        Vai até aonde está o recurso para pegá-lo
        """
        x_resource = self.resourcePos[resource][0]
        y_resource = self.resourcePos[resource][1]
        
        print(f'Em busca do recurso: {self.resources[resource][0]} => drone {drone}')
        self.goto_resource(drone, resource, x_resource, y_resource)
        

    def goto_resource(self, drone, resource, x_resource, y_resource):
        """
        calcula distancia entre drone e recurso
        """
        d = self.targetPos[drone]
        distancia = math.sqrt(math.pow(d[0] - x_resource, 2) + math.pow(d[1] - y_resource, 2))

        if distancia > 0.5:
            if d[0] > x_resource:
                d[0] -= 0.3
            else: 
                d[0] += 0.3
            if d[1] > y_resource:
                d[1] -= 0.3
            else:
                d[1] += 0.3

            # timeout = time.time() + self.timeout
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, d, sim.simx_opmode_continuous) 
            # while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            #     err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            #     self.dronePos[drone] = self.mensagem.fix_coords(self.dronePos[drone]) 
            
        else: #chegou no recurso       
            self.resources[resource][1] -= 1
            self.state[drone] = 'H'
            

    def back_origin(self, drone, resource):
        """
        Pega recurso e leva para origem
        """
        
        print('Levando para origem => drone ', drone)
        origin = 0.0
        d = self.targetPos[drone]
        #calcula distancia entre drone e origem
        distancia = math.sqrt(math.pow(d[0] - origin, 2) + math.pow(d[1] - origin, 2))
        
        if distancia > 0.5:        
            if d[0] > 0.0:
                d[0] -= 0.3
            else: 
                d[0] += 0.3
            if d[1] > 0.0:
                d[1] -= 0.3
            else:
                d[1] += 0.3
            
            # timeout = time.time() + self.timeout
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, d, sim.simx_opmode_continuous) 
            # while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            #     err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            #     self.dronePos[drone] = self.mensagem.fix_coords(self.dronePos[drone])
            
            # distancia = math.sqrt(math.pow(d[0] - origin, 2) + math.pow(d[1] - origin, 2))
        else:
            print('Qtd do recurso ', self.resources[resource][0],' sobrando: ', self.resources[resource][1])
            if (self.resources[resource][1]) == 0:
                self.state[drone] = 'A' #volta para navegação
                self.resources.pop(resource)    #retira da lista para simular realidade
                print('Retirado da lista de recursos: ', self.resources[resource][0])
                self.v_pos[drone] = self.get_random_coords() #atualiza lista de posição do drone
            
            else:
                self.state[drone] = 'G'
    
        
    def do_movement(self, movement, drone, progresso): 
        if (movement == 'vertical'):
            self.mensagem.vertical(drone, progresso)

        elif (movement == 'horizontal'):
            self.mensagem.horizontal(drone, progresso)

        elif (movement == 'quadrado'):    
            self.mensagem.quadrado(drone, progresso)
        
        elif (movement == 'triangulo'):
            self.mensagem.triangulo(drone, progresso)
      
        elif (movement == 'seta cima'):
            self.mensagem.setaCima(drone, progresso)

        elif (movement == 'seta baixo'):
            self.mensagem.setaBaixo(drone, progresso)
        
        elif (movement == 'letra T'):
            self.mensagem.letra_T(drone, progresso)
        
        elif (movement == 'letra M'):
            self.mensagem.letra_M(drone, progresso)

        elif (movement == 'zig zag'):
            self.mensagem.zig_zag(drone, progresso)

        elif (movement == 'ampulheta'):
            self.mensagem.ampulheta(drone, progresso)

        elif (movement == 'losango'):
            self.mensagem.losango(drone, progresso)
        



    
