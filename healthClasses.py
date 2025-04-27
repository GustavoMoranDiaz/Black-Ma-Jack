#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 16:07:15 2025

@author: andrewczekay
"""

"""player and dealer clases for healths
"""
import pygame

class Player:
    def __init__(self, health):
        self.health = health
        
    def getHealth(self):
        return self.health
    
    def setHealth(self, newHealth):
        self.health = newHealth
        
    #def buildHealthBar(self, health, change):
        
        
        
class Dealer:
    def __init__(self, health):
        self.health = health
        
    def getHealth(self):
        return self.health
    
    def setHealth(self, newHealth):
        self.health = newHealth