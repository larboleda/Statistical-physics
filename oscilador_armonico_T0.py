
# coding: utf-8

# In[2]:

import numpy as np
import matplotlib.pyplot as plt
import random 

get_ipython().magic('matplotlib inline')


# In[33]:

#Distribución de probabilidad 
    
def probability(x):
    return (1/np.sqrt(np.pi))*np.exp(-x**2)
   
#Muestreo usando algoritmo Metropolis

x_sample=[]

x= 0.0
delta = 0.5
niter = 100000

for k in range(niter):
    
    x_new = x + random.uniform(-delta,delta)
    
    Px_new = probability(x_new)
    Px = probability(x)
    
    if random.uniform(0.0,1.0) < (Px_new / Px):
        x = x_new
        
        x_sample.append(x)
        

xs = np.arange(-3.0, 3.0, 0.0001)

fi = probability(xs)

#histograma    

n_bins = int(np.sqrt(len(x_sample))/4)

plt.hist(x_sample, bins=n_bins,normed=True, histtype='bar', lw=2, color="b", label="Histograma")

#curva teórica

plt.plot(xs,fi,"-", color="k",lw=1.5,label=r"$\Pi(x)=\frac{1}{\sqrt{\pi}}e^{-x^2}$")
plt.xlabel(r"Posiciones",fontsize=15)
plt.ylabel(r"Frecuencia",fontsize=15)
plt.legend()
plt.grid()
plt.savefig('histograma.png')
plt.show()


# In[ ]:




# In[ ]:



