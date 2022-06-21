import numpy as np

nmax=4
H=np.zeros((nmax,nmax),float)
XAXB=np.array([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
YAYB=np.array([[0,0,0,-1],[0,0,1,0],[0,1,0,0],[-1,0,0,0]])
ZAZB=np.array([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])
SASB=XAXB+YAYB+ZAZB-3*ZAZB
print('\n Hamiltonian without mu^2/r^3 factor \n',SASB,'\n')

es,ev=np.linalg.eig(SASB)
print ('Eigenvalues \n', np.round(es,2),'\n')
print('Eigenvalues (in columns) \n',ev,'\n')

phi1=ev[:,0]
phi4=ev[:,1]
phi3=ev[:,2]
phi2=ev[:,3]

basis=np.array([phi1,phi2,phi3,phi4]) 

for i in range(0,nmax):
    for j in range(0,nmax):
        term=np.dot(SASB,basis[i]) 
        H[i,j]=np.round(np.dot(basis[j],term),2) 
print('Hamiltonian in Eigenvector Basis \n',H)

