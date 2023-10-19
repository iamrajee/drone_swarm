#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tassinho
"""

import sim
import estruturacao

naveg = None
resources = [['Tree', 7], ['indoorPlant', 3], ['indoorPlant0', 3], ['Tree#0', 4], ['mannequin', 0]]

try:  
    sim.simxFinish(-1)
    clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
    
    if clientID != -1:
        """
        :param n_drones = quantidade de drones
        :param z_coord = altura do drone para navegação
        :param timeout = tempo usado para caso de parada
        :param dist_max = distancia máxima em que a camera consegue capturar recurso e/ou movimentos de outros drones
        :param eixo_x = posição maxima em que o drone pode ir no eixo x, considerando que a origem é no meio
        :param eixo_y = posição máxima em que o drone pode ir no eixo y, considerando que a origem é no meio
        :param resources = lista contendo o nome e quantidade de recurso disponível, simplesmente aleatório
        
        """       
        
        naveg = estruturacao.Navegation(clientID, n_drones=4, z_coord=2.5, timeout=0.5, dist_max=1.0, eixo_x=5.8, eixo_y=5.8,
                                        resources=resources)
  
    else:
        print('Falha ao conectar ao servidor de API remoto')
        
        sim.simxFinish(clientID)

except KeyboardInterrupt:
    sim.simxFinish(clientID)
