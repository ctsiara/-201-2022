#SU3.py
import numpy as np

L1=np.array([[0,1,0],[1,0,0],[0,0,0]])
L2=np.array([[0,-1j,0],[1j,0,0],[0,0,0]])
L3=np.array([[1,0,0],[0,-1,0],[0,0,0]])
L4=np.array([[0,0,1],[0,0,0],[1,0,0]])
L5=np.array([[0,0,-1j],[0,0,0],[1j,0,0]])
L6=np.array([[0,0,0],[0,0,1],[0,1,0]])
L7=np.array([[0,0,0],[0,0,-1j],[0,1j,0]])
L8=np.array([[1,0,0],[0,1,0],[0,0,-2]])*1/np.sqrt(3)

u=np.array([1,0,0])
d=np.array([0,1,0])
s=np.array([0,0,1])

Ip=0.5*(L1+1j*L2)
Up=0.5*(L6+1j*L7)
Vp=0.5*(L4+1j*L5)
Im=0.5*(L1-1j*L2)
Um=0.5*(L6-1j*L7)
Vm=0.5*(L4-1j*L5)

Ipxd=np.dot(Ip,d)
print("Ipdu",Ipxd)
Vpxs=np.dot(Vp,s)
print("Vpsu",Vpxs)
Upxs=np.dot(Up,s)
print("Upsd",Upxs)
