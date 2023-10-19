#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:08:13 2020

@author: tassinho
"""

import sim
import time
import movements

mensagem = None

class AUX(object):
    def __init__(self, clientID):
        self.clientID = clientID
        self.targetObj = []
        self.arqTempoExec = open("tempoExec.txt", "w")
        self.filePositions = open("triangulo.txt", "w")
            
    def get_target(self):
        err, self.targetObj = sim.simxGetObjectHandle(self.clientID, 'Quadricopter_target', sim.simx_opmode_blocking)
        err, self.targetPos = sim.simxGetObjectPosition(self.clientID, self.targetObj, -1, sim.simx_opmode_streaming)
        
        err, self.droneObj = sim.simxGetObjectHandle(self.clientID, 'Quadricopter', sim.simx_opmode_blocking)
        err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)


    def start_navigation(self, coordX, coordY):
        #andar no ambiente de forma aleatória
        i= 0
        while i < 3:
            self.targetPos[0] = self.targetPos[0] + coordX
            self.targetPos[1] = self.targetPos[1] + coordY
            self.targetPos[2] = 1.0
            time.sleep(1)
           
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            i += 1

    #movement = movimento ao ser executado
    #repet = quantidade de vezes a executar o movimento
    def do_movement(self, movement, repet): 
        self.mensagem = movements.movimento(self.clientID, self.targetObj, self.targetPos, self.droneObj, self.dronePos, self.filePositions)

        time.sleep(2)        
        if (movement == 'vertical'):
            start = time.monotonic()
            self.mensagem.vertical(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('Vertical = ' + str((finish-start)/repet) + ' segundos')

        elif (movement == 'horizontal'):
            start = time.monotonic()
            self.mensagem.horizontal(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nHorizontal = ' + str((finish-start)/repet) + ' segundos')

        elif (movement == 'quadrado'):    
            start = time.monotonic()
            self.mensagem.quadrado(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nQuadrado = ' + str((finish-start)/repet) + ' segundos')
        
        elif (movement == 'triangulo'):
            start = time.monotonic()
            self.mensagem.triangulo(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nTriângulo = ' + str((finish-start)/repet) + ' segundos')
        
        elif (movement == 'infinito'):
            start = time.monotonic()
            self.mensagem.infinito(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nInfinito = ' + str((finish-start)/repet) + ' segundos')
        
        elif (movement == 'seta cima'):
            start = time.monotonic()
            self.mensagem.setaCima(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nSeta Cima = ' + str((finish-start)/repet) + ' segundos')

        elif (movement == 'seta baixo'):
            start = time.monotonic()
            self.mensagem.setaBaixo(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nSeta Baixo = ' + str((finish-start)/repet) + ' segundos')
        
        elif (movement == 'sinal maior'):
            start = time.monotonic()
            self.mensagem.sinalMaior(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nSinal Maior = ' + str((finish-start)/repet) + ' segundos')

        elif (movement == 'sinal menor'):
            start = time.monotonic()
            self.mensagem.sinalMenor(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nSinal Menor = ' + str((finish-start)/repet) + ' segundos')

        elif (movement == 'letra T'):
            start = time.monotonic()
            self.mensagem.letra_T(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nLetra T = ' + str((finish-start)/repet) + ' segundos')
        
        elif (movement == 'letra M'):
            start = time.monotonic()
            self.mensagem.letra_M(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nLetra M = ' + str((finish-start)/repet) + ' segundos')

        elif (movement == 'zig zag'):
            start = time.monotonic()
            self.mensagem.zig_zag(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nZig Zag = ' + str((finish-start)/repet) + ' segundos')

       # elif (movement == 'circulo'):
       #     self.mensagem.circulo(repet)

        elif (movement == 'ampulheta'):
            start = time.monotonic()
            self.mensagem.ampulheta(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nAmpulheta = ' + str((finish-start)/repet) + ' segundos')

        elif (movement == 'losango'):
            start = time.monotonic()
            self.mensagem.losango(repet)
            finish = time.monotonic()
            self.arqTempoExec.write('\nLosango = ' + str((finish-start)/repet) + ' segundos')
    

    