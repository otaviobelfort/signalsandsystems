

import matplotlib.pyplot as plt
import numpy as np
import math

a = 0.5
t = np.arange(0.0, 50, 0.1) # vector generetor the time

'''
a, b, = 0.5, 450 # constantes
'''
a = -0.2
b = -9.8

equilib = b/a
func1 = (equilib + 1) + np.exp(a*t) # (equilib + 1) -> um valor acima do ponto de equilibrio
ponto_equilib = equilib + np.exp(a*t)*0
func2 = (equilib - 1) - np.exp(a*t) # (equilib - 1) -> um valor abaixo do ponto de equilibrio

plt.plot(t,func1,'r-', t,func2,'b-', t,ponto_equilib,'g-') 

plt.xlabel('time (s)')
plt.ylabel('(P(t))')
'''
plt.title('População de corujas - time plot')
plt.grid(True)
plt.savefig("População de corujas - time plot")
'''
plt.title('Sistemas Físico - time plot')
plt.grid(True)
plt.savefig("Sistemas Físico - time plot")

plt.show()
