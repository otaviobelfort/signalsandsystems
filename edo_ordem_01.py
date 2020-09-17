#!/usr/bin/env python3
"""
'#!/usr/bin/env python3' aponta para o interpretador python e
permite a execução no terminal com -> ./namefile.py
Permissão: sudo chmod +x namefile.py
"""
"""
    - Bibliografia: Boyce, W. E. and Diprima, R. C. (2012). Equações Diferenciais Elementares e
Problemas de Valores de Contorno. LTC, 9 edition.

   Autor: Otávio Belfort
   
   github.com/otaviobelfort | facebook.com/otaviobelforth | 
"""  

import matplotlib.pyplot
import math
#function generetor the vector
def vector_generetor(i0,n,i1):
    vetor_t = list(range(i0, n, i1))
    vector_time = []
    interval = 0.1 # interval between each element of the vector
    for element in vetor_t:
        vector_time.append(interval * element)
    return vector_time
a = -0.2
b = 450
c = 1# c=0 equilibrio, - 
v_p = b/a
vector_result = []
vector_result2 = []
vector_time = vector_generetor(1,100,1)
for element in vector_time:
    vector_result.append(50 + (c*math.exp(a*element)))

#print(vector_result)

matplotlib.pyplot.plot(vector_time, vector_result)
matplotlib.pyplot.show() # plot graph
