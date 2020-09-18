#!/usr/bin/env python3
"""
    Bibliografia: 
    - Boyce, W. E. and Diprima, R. C. (2012). Equações Diferenciais Elementares e
Problemas de Valores de Contorno. LTC, 9 edition.
    - http://www.doc.mmu.ac.uk/STAFF/S.Lynch/DSAP_Jupyter_Notebook.html

   Autor: Otávio Belfort
   github.com/otaviobelfort | facebook.com/otaviobelforth | 
"""  
import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(0.0, 50, 0.1) # vector generetor the time

'''
a, b, = 0.5, 450 # constantes
'''
a, b= -0.2, -9.8

def edo_ordem_01(a, b, t):
    equilib = b/a
    func1 = (equilib + 1) + np.exp(a*t) # (equilib + 1) -> a value above the breakeven point
    ponto_equilib = equilib + np.exp(a*t)*0
    func2 = (equilib - 1) - np.exp(a*t) # (equilib - 1) -> a value below the breakeven point

    plt.plot(t,func1,'r-', t,func2,'b-', t,ponto_equilib,'g-') 

    plt.xlabel('time (s)')
    plt.ylabel('(P(t))')
    '''
    plt.title('População de corujas - time plot')
    plt.grid(True)
    plt.savefig("População de corujas - time plot")
    # Graphic: https://github.com/otaviobelfort/signalsandsystems/blob/master/Popula%C3%A7%C3%A3o%20de%20corujas%20-%20time%20plot.png 
    '''
    plt.title('Sistemas Físico - time plot')
    plt.grid(True)
    plt.savefig("Sistemas Físico - time plot")
    # Graphic: https://github.com/otaviobelfort/signalsandsystems/blob/master/Sistemas%20F%C3%ADsico%20-%20time%20plot.png

    plt.show()

#plot
edo_ordem_01(-0.2, -9.8,t)