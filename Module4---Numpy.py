import numpy as np

a= np.array ([0,1,2,3,4,5,6,7,8,9,10.2])
type (a)
a.dtype
a[2]
a.size
a.ndim
a.shape


u =np.array([3,1])
v =np.array([5,9])
z=u+v
z
z2= u*v
z2
z3=np.dot(u,v)
z3
u+1


np.pi
np.linspace(-2,2,num=9)
x= np.linspace(0,2*np.pi,100)
y = np.sin(x)

import matplotlib.pyplot as plt
plt.plot(x,y)
np.zeros((3,3))
np.arange(10,30,4)
np.linspace(10,30,5)
qq=np.ones((3000,3000),dtype=int)
qq
# ============================================================================#
# Import the libraries

import time
import sys
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

# Plotting functions
def Plotvec1(u, z, v):

    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

a.size
a.ndim
a.shape
a.mean()
a.max()
standard_deviation = a.std()
standard_deviation
Plotvec1(u,v,z)
#================================================== 2D numpy
s= np.ones ((3,3,3))
s
s.size
s.ndim
s.shape
s.mean()
s.max()
standard_deviation = s.std()
standard_deviation
x= pi.linspace(-2*np.pi,2*np.pi,100)
y = np.sin(x)
z= np.cos(x)

plt.plot (x,y,z)
