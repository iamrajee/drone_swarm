#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:19:46 2020

@author: tassinho
"""

import sim
import f_aux
import time

aux_func = None
palavras = ['triangulo'] #circulo, infinito

try:  
    sim.simxFinish(-1)
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    
    if clientID != -1:
        aux_func = f_aux.AUX(clientID)
       
        aux_func.get_target()
        #while vrep.simxGetConnectionId(clientID) != -1:
        #while True:
        aux_func.start_navigation(0,0)
        i = 0
        for i in range(len(palavras)):
           aux_func.do_movement(palavras[i], 5) 
           time.sleep(2)
        # aux_func.do_movement('infinito', 3) 
  
    else:
        print('Failed to connect to remote API Server')
        
        sim.simxFinish(clientID)

except KeyboardInterrupt:
    sim.simxFinish(clientID)
