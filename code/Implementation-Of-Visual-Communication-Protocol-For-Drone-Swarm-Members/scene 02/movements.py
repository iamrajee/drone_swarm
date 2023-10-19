#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tassinho
"""

import sim
import time

class movimento(object):
    def __init__(self, clientID, targetObj, targetPos, droneObj, dronePos):
        self.clientID = clientID
        self.targetObj = targetObj
        self.targetPos = targetPos
        self.droneObj = droneObj
        self.dronePos = dronePos

    def fix_coords(self, coords):
        for i in range(3):
            coords[i] = abs(float('%.2f' % (coords[i])))
           
        return coords  
    
    def vertical(self, drone, progress):
        if progress%2 == 1:
            self.targetPos[drone][2] = self.targetPos[drone][2] + 0.7
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone])
        
        elif progress%2 == 0:
            self.targetPos[drone][2] = self.targetPos[drone][2] - 0.7    
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 
            

    def horizontal(self, drone, progress):
        if progress%2 == 1:
            self.targetPos[drone][0] = self.targetPos[drone][0] + 0.7
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone])       
    
        if progress%2 == 0:
            self.targetPos[drone][0] = self.targetPos[drone][0] - 0.7   
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone])        



    def quadrado(self, drone, progress):
        if progress == 1 or progress == 5:
            self.targetPos[drone][2] = self.targetPos[drone][2] + 0.5
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            # timeout = time.time() + 1.5
            # while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            #     err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            #     self.dronePos[drone] = self.fix_coords(self.dronePos[drone])  
        
        elif progress == 2 or progress == 6:
            self.targetPos[drone][0] = self.targetPos[drone][0] + 0.5     
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 

        elif progress == 3 or progress == 7:
            self.targetPos[drone][2] = self.targetPos[drone][2] - 0.5
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 
        
        elif progress == 4 or progress == 8:
            self.targetPos[drone][0] = self.targetPos[drone][0] - 0.5     
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 

    
    
    def triangulo(self, drone, progress): #triangulo
        if progress == 1 or progress == 4:
            #primeiro lado  /
            self.targetPos[drone][0] = self.targetPos[drone][0] + 0.35
            self.targetPos[drone][2] = self.targetPos[drone][2] + 0.50
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 
        
        elif progress == 2 or progress == 5:
            #segundo lado \
            self.targetPos[drone][0] = self.targetPos[drone][0] + 0.35
            self.targetPos[drone][2] = self.targetPos[drone][2] - 0.50
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 
        
        elif progress == 3 or progress == 6:
            #terceiro lado _
            self.targetPos[drone][0] = self.targetPos[drone][0] - 0.70
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 

                

    def letra_T(self, drone):
        self.targetPos[drone][2] = self.targetPos[drone][2] + 0.6
        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        timeout = time.time() + 2.0
        while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 

        self.targetPos[drone][0] = self.targetPos[drone][0] - 0.3
        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        timeout = time.time() + 2.0
        while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            self.dronePos[drone] = self.fix_coords(self.dronePos[drone])    

        self.targetPos[drone][0] = self.targetPos[drone][0] + 0.6
        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        timeout = time.time() + 2.5
        while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 

        self.targetPos[drone][0] = self.targetPos[drone][0] - 0.3
        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        timeout = time.time() + 2.5
        while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 

        self.targetPos[drone][2] = self.targetPos[drone][2] - 0.6
        sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
        timeout = time.time() + 2.0
        while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
            err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
            self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 


    

    def ampulheta(self, drone, progress):
        if progress == 1:
            self.targetPos[drone][0] = self.targetPos[drone][0] + 0.6
            self.targetPos[drone][2] = self.targetPos[drone][2] + 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 

        elif progress == 2:
            self.targetPos[drone][2] = self.targetPos[drone][2] - 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 
        
        elif progress == 3:
            self.targetPos[drone][0] = self.targetPos[drone][0] - 0.6
            self.targetPos[drone][2] = self.targetPos[drone][2] + 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 

        elif progress == 4:
            self.targetPos[drone][2] = self.targetPos[drone][2] - 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj[drone], -1, self.targetPos[drone], sim.simx_opmode_continuous)
            timeout = time.time() + 1.5
            while (set(self.dronePos[drone]) != set(self.targetPos[drone])) and (time.time() < timeout):
                err, self.dronePos[drone] = sim.simxGetObjectPosition(self.clientID, self.droneObj[drone], -1, sim.simx_opmode_blocking)     
                self.dronePos[drone] = self.fix_coords(self.dronePos[drone]) 
