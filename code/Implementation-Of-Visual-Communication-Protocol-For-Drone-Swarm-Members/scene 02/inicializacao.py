# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:54:01 2021

@author: laura
"""

import sim
import random

resources = [[]]

class Inicializa(object):
    def __init__(self, clientID, num_drones, z_coord, resources):
        self.clientID = clientID
        self.z_coord = z_coord
        self.resources = resources
        self.targetObj = []
        self.targetPos = []
        self.droneObj = []
        self.dronePos = []
        self.resourceObj = []
        self.resourcePos = []
        self.get_resources()
        self.init_resources()
        self.get_drones(num_drones)
        
        
            
    #atribui os drones para variaveis
    def get_drones(self, num_drones):
        for i in range(num_drones):
            err, aux = sim.simxGetObjectHandle(self.clientID, 'Quadricopter_target#' + str(i), sim.simx_opmode_blocking)
            self.targetObj.insert(i,aux)
            err, aux2 = sim.simxGetObjectPosition(self.clientID, self.targetObj[i], -1, sim.simx_opmode_blocking)
            self.targetPos.insert(i, aux2)

            err, aux = sim.simxGetObjectHandle(self.clientID, 'Quadricopter#' + str(i), sim.simx_opmode_blocking)
            self.droneObj.insert(i,aux)
            err, aux2 = sim.simxGetObjectPosition(self.clientID, self.droneObj[i], -1, sim.simx_opmode_blocking)
            self.dronePos.insert(i, aux2)
        
        return (self.targetObj, self.targetPos, self.droneObj, self.dronePos)
        
                

    def get_resources(self):
        for i in range(len(self.resources)):
            err, aux = sim.simxGetObjectHandle(self.clientID, self.resources[i][0], sim.simx_opmode_blocking)
            self.resourceObj.insert(i, aux) 
            err, aux2 = sim.simxGetObjectPosition(self.clientID, self.resourceObj[i], -1, sim.simx_opmode_blocking)
            self.resourcePos.insert(i, aux2)
        
        return self.resourceObj, self.resourcePos

    #drones começam em posicoes [0,0,z_coord]
    #resources começam em posicoes randomicas
    def init_resources(self):
        for j in range(len(self.resources)):
            r_x = random.uniform(-5.5, 5.5)
            r_y = random.uniform(-5.5, 5.5)
            
            # if r_x > -0.6 and r_x <=0.0:
            #     r_x -= 1.0
            # elif r_x < 0.6 and r_x > 0.0:
            #     r_x += 1.0
            # if r_y > -0.6 and r_y <=0.0:
            #     r_y -= 1.0
            # elif r_y < 0.6 and r_y > 0.0:
            #     r_y += 1.0    
                
            
            self.resourcePos[j][0] = r_x
            self.resourcePos[j][1] = r_y
               
            sim.simxSetObjectPosition(self.clientID, self.resourceObj[j], -1, self.resourcePos[j], sim.simx_opmode_continuous)
        
