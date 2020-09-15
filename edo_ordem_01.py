#!/usr/bin/env python3
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
a = 0.5
b = 450
c = 1


vector_result = []
vector_time = vector_generetor(1,100,1)
for element in vector_time:
    vector_result.append(b/a + (c * math.exp(a*element)))


print(vector_time, vector_result)

#matplotlib.pyplot.plot(vector_time, vector_result)
#matplotlib.pyplot.show()