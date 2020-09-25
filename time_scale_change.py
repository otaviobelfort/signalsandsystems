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

# Vetores para função senoidal
#'''
t = np.arange(0.0, 4.0, 0.01)
x = 1 + np.sin(2*np.pi*t) # function sin
#'''

# Vetores para função Triangular, vetores explícitos
'''
t = [-2,-1,0,1,2]
x = [0,0,1,0,0]
'''
def time_scale_change(x, t, a):
    y = [] # vector out
    if a > 0:
        for i in t:
            y.append(i/a)

    #plt.plot(t,x,'r-', y,x,'b-')
    plt.plot(t,x,'b-', y,x,'r-')
    #plt.plot(y,x,'b-')
    
    #plt.xlabel('t \n Triangular ')
    plt.xlabel('t \n Senoidal ')
    plt.ylabel('y(t)')
    plt.title(' y(t) e t , a = 1(blue), a = 0.3(red)  ') #| BLUE: y(t) = x(at), a = 0.5')
    plt.grid(True)
    #plt.savefig("sigmal_triangular.png")
    plt.savefig("sigmal_sin.png")
    plt.show()

time_scale_change(x, t,0.3)