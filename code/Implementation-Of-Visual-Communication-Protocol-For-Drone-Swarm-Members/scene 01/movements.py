#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:08:13 2020

@author: tassinho
"""

import sim
import time, math
import numpy as np

class movimento(object):
    def __init__(self, clientID, targetObj, targetPos, droneObj, dronePos, filePositions):
        self.clientID = clientID
        self.targetObj = targetObj
        self.targetPos = targetPos
        self.droneObj = droneObj
        self.dronePos = dronePos
        self.filePositions = filePositions


    def fix_coords(self, coords):
        for i in range(len(coords)):
            coords[i] = float('%.1f' % (coords[i])) 
            if coords[i] < 0.0:
                coords[i] *= -1
        return coords  
    
    
    def vertical(self, repet):
        start = time.monotonic()   
        count = 0
        for i in range(repet):
            aux = 0.5
            for j in range(2):
                self.targetPos[2] += aux
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 1.8
                while (set(self.dronePos) != set(self.targetPos)) or (time.time() < timeout):
                    count += 1
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming) 
                    self.dronePos = self.fix_coords(self.dronePos)
                    if count == 100:
                        stop = float('%.2f' % (time.monotonic() - start))
                        self.filePositions.write(str(self.dronePos[0]) + '\t' + str(stop) + '\t' + str(self.dronePos[2]) + '\n') 
                        count = 0
                        
                aux *= -1


    def horizontal(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            aux = 0.5
            for j in range(2):            
                self.targetPos[0] += aux
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 1.6
                while (set(self.dronePos) != set(self.targetPos)) or (time.time() < timeout):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos)
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n') 
                
                aux *= -1
                

    def quadrado(self, repet):
        start = time.monotonic() 
        for j in range(repet):
            aux = 0.5
            for i in range(4):
                if i%2 == 0:
                    pos = 2 #eixo z
                else:
                    pos = 0 #eixo x
                    
                if i >= 2:
                    aux = -0.5 
                
                self.targetPos[pos] = self.targetPos[pos] + aux
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)) or (time.time() < timeout):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_blocking)     
                    self.dronePos = self.fix_coords(self.dronePos)  
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    
                

    def triangulo(self, repet): #triangulo equilatero
        start = time.monotonic() 
        for i in range(repet):
            aux = 0.35
            for j in range(2):
                self.targetPos[0] += 0.35
                self.targetPos[2] += aux
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos)
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    
                aux *= -1

            #terceiro lado _
            self.targetPos[0] -= 0.70
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)) or (time.time() < timeout):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos) 
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')


    def infinito(self, repet):  # y² = 4x² (1 - x²)
        for i in range(repet):
            scale = []
            x = []
            y = []
            t = np.linspace(-3.5, 3.5, 100)
            for j in range(99):
                scale.append(2 / (3 - math.cos(2*t[j+1])))
                x.append(scale[j] * math.cos(t[j+1]))
                y.append(scale[j] * math.sin(2*t[j+1]) / 2)

                self.targetPos[0] = x[j]
                self.targetPos[2] = y[j]
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                time.sleep(0.3)

                
    def setaCima(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            auxX = 0.3
            auxZ = 0.6
            
            for j in range(4):
                self.targetPos[0] += auxX
                self.targetPos[2] += auxZ
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos) 
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
    
                auxZ *= -1
                if j == 1:
                    auxX *= -1


    def setaBaixo(self, repet):
        start = time.monotonic() 
        # #subir um pouco mais alto
        # self.targetPos[2] += 0.6
        # sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
        # timeout = time.time() + 2.0
        # while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
        #     err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
        #     self.dronePos = self.fix_coords(self.dronePos)   
            
        for i in range(repet):
            auxX = 0.3
            auxZ = -0.6
            for j in range(4):
                self.targetPos[0] += auxX
                self.targetPos[2] += auxZ
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos)
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                
                auxZ *= -1
                if j == 1:
                    auxX *= -1

            
        # self.targetPos[2] -= 0.6
        # sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
        # timeout = time.time() + 2.0
        # while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
        #     err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
        #     self.dronePos = self.fix_coords(self.dronePos) 


    def sinalMaior(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            auxX = 0.6
            auxZ = 0.3
            
            for j in range(4):
                self.targetPos[0] += auxX
                self.targetPos[2] += auxZ
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos)
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    
                auxX *= -1
                if j == 1:
                    auxZ *= -1
  
    

    def sinalMenor(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            auxX = -0.6
            auxZ = 0.3
            
            for j in range(4):
                self.targetPos[0] += auxX
                self.targetPos[2] += auxZ
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos)
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    
                auxX *= -1
                if j == 1:
                    auxZ *= -1



    def letra_T(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            self.targetPos[2] += 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos)
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    
            self.targetPos[0] -= 0.4
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos)
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    
            self.targetPos[0] += 0.8
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos)
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                
            self.targetPos[0] -= 0.4
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos)
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')

            self.targetPos[2] -= 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)) and (time.time() < timeout):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos)
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                

    def letra_M(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            auxX = 0.25
            auxZ = 0.5
            for j in range(8):
                self.targetPos[0] = self.targetPos[0] + auxX
                self.targetPos[2] = self.targetPos[2] + auxZ
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos)
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    
                    if (time.time() > timeout):
                        break

                auxZ *= -1
                if j == 3:
                    auxX *= -1

           
    def zig_zag(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            #ida
            self.targetPos[0] = self.targetPos[0] - 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos) 
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                if (time.time() > timeout):
                    break     

            self.targetPos[0] = self.targetPos[0] + 0.6
            self.targetPos[2] = self.targetPos[2] + 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos)
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                if (time.time() > timeout):
                    break    

            self.targetPos[0] = self.targetPos[0] - 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos)
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                if (time.time() > timeout):
                    break

            #volta
            self.targetPos[0] = self.targetPos[0] + 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos) 
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                if (time.time() > timeout):
                    break     

            self.targetPos[0] = self.targetPos[0] - 0.6
            self.targetPos[2] = self.targetPos[2] - 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos) 
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                if (time.time() > timeout):
                    break
            
            self.targetPos[0] = self.targetPos[0] + 0.6
            sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
            timeout = time.time() + 2.0
            while (set(self.dronePos) != set(self.targetPos)):
                err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                self.dronePos = self.fix_coords(self.dronePos) 
                stop = float('%.2f' % (time.monotonic() - start))
                self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                if (time.time() > timeout):
                    break    

    # def circulo(self, repet):
    #     i = 0
    #     while i < repet:
    #         ang = 2 * math.pi
    #         xp = 0.25 * math.sin(ang)
    #         yp = 0.25 * math.cos(ang)
    #         self.targetPos[0] = self.targetPos[0] + xp
    #         self.targetPos[2] = self.targetPos[2] + yp
    #         sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
    #         time.sleep(1)
       
    #         i += 1


    def ampulheta(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            auxX = 0.6
            auxZ = 0.6
            
            for j in range(4):     
                if j%2 == 0:  
                    self.targetPos[0] += auxX
                    auxX *= -1
                    
                self.targetPos[2] += auxZ
                    
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos)
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    if (time.time() > timeout):
                        break 
                    
                auxZ *= -1



    def losango(self, repet):
        start = time.monotonic() 
        for i in range(repet):
            auxX = 0.3
            auxZ = 0.3
            for j in range(4):
                self.targetPos[0] += auxX
                self.targetPos[2] += auxZ
                sim.simxSetObjectPosition(self.clientID, self.targetObj, -1, self.targetPos, sim.simx_opmode_continuous)
                timeout = time.time() + 2.0
                while (set(self.dronePos) != set(self.targetPos)):
                    err, self.dronePos = sim.simxGetObjectPosition(self.clientID, self.droneObj, -1, sim.simx_opmode_streaming)     
                    self.dronePos = self.fix_coords(self.dronePos)
                    stop = float('%.2f' % (time.monotonic() - start))
                    self.filePositions.write(str(stop) + '\t' + str(self.dronePos[0]) + '\t' + str(self.dronePos[2]) + '\n')
                    if (time.time() > timeout):
                        break
                
                if j == 0:
                    auxZ *= -1
                
                elif j == 1:
                    auxX *= -1
                    
                elif j == 2:
                    auxZ *= -1
