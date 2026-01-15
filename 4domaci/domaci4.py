import numpy as np
import numpy as np
from numpy import linalg as LA
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D

np.set_printoptions(precision=5,suppress=True)
nula = np.array([0,0,0])


def dveJed(img, orig):
  nula = np.array([0,0,0,0])
  jed1 = np.concatenate((nula, -img[2]*orig, img[1]*orig))
  jed2 = np.concatenate(( img[2]*orig, nula, -img[0]*orig))
  return np.array([jed1, jed2])


def napravimatricu(img, orig):
    A=[]
    n=len(img)
    for i in range(n):
        dve=(dveJed(img[i],orig[i]))
        A.append(dve[0])
        A.append(dve[1])

    T=np.array(A)

    return T

def matricakamere(imgs,origs):
    a=napravimatricu(imgs,origs)
    a=np.array(a)
    _, _, Vh = LA.svd(a)


    T=Vh[-1]
    T=(1/T[-1])*T
    T=T.reshape(3, 4)

    T = np.where(np.isclose(T, 0) , 0.0 , T)
    return T


  
testpts2D = np.array([[12, 61, 31], [1, 95, 4], [20, 82, 19], [56, 50, 55], [32, 65, 84], [46, 39, 16], [67, 63, 78]])
testpts3D = np.array([[44, 61, 31, 99], [17, 84, 40, 45], [20, 59, 65, 3], [37, 81, 70, 82], [7, 95, 8, 29], [31, 61, 91, 37], [82, 99, 80, 7]])




testorg =  np.array([1,-1,-1])*(np.array([1600,0,0]) -  np.array([[625,345, 1], [917,500, 1], [628,730,1],[316,508,1],  [379,783,1],[637,1000,1], [875,775,1],[630, 570,1]] ))

testimg=np.array([[0,0,3,1],[0,3,3,1],[3,3,3,1],[3,0,3,1],[3,0,0,1],[3,3,0,1],[0,3,0,1],[2,2,3,1]])



org =  np.array([1,-1,-1])*(np.array([3468,0,0]) -  np.array([[2981,817, 1], [3633,1305, 1], [2869,1621,1],[2257,1053,1],  [2201,1733,1],[2685,2285,1], [3341,1945,1],[2909, 1313,1]] ))

img=np.array([[0,0,3,1],[0,3,3,1],[3,3,3,1],[3,0,3,1],[3,0,0,1],[3,3,0,1],[0,3,0,1],[2,2,3,1]])

T1=matricakamere(org,img)
print("Matrica kamere: \n",T1)


def centar(T):
    C1 = LA.det(np.delete(T,0,1))
    C2 = LA.det(np.delete(T,1,1))
    C3 = LA.det(np.delete(T,2,1))
    C4 = LA.det(np.delete(T,3,1))

    C = np.array([C1, -C2, C3, -C4]) *(-1/C4)
    C = np.where(np.isclose(C, 0) , 0.0 , C)

    return C

print("pozicija centra \n",centar(T1))

def kamera_K(T):
    t0 = np.delete(T, 3, 1)
    if LA.det(t0)<0:
        t0=-1*t0
    t0i = LA.inv(t0)

    Q,R=LA.qr(t0i)

    if(R[0,0]<0):
        R=np.matmul(np.diag([-1,1,1]),R)
        Q=np.matmul(Q,np.diag([-1,1,1]))
    if(R[1,1]<0):
        R=np.matmul(np.diag([1,-1,1]),R)
        Q=np.matmul(Q,np.diag([1,-1,1]))
    if(R[2,2]<0):
        R=np.matmul(np.diag([1,1,-1]),R)
        Q=np.matmul(Q,np.diag([1,1,-1]))

    K = LA.inv(R)
    K = K / K[2, 2]
    K = np.where(np.isclose(K, 0), 0.0, K)

    return K

def kamera_A(T):
    t0 = np.delete(T, 3, 1)
    if LA.det(t0)<0:
        t0=-1*t0
    t0i = LA.inv(t0)

    Q,R=LA.qr(t0i)

    if(R[0,0]<0):
        R=np.matmul(np.diag([-1,1,1]),R)
        Q=np.matmul(Q,np.diag([-1,1,1]))
    if(R[1,1]<0):
        R=np.matmul(np.diag([1,-1,1]),R)
        Q=np.matmul(Q,np.diag([1,-1,1]))
    if(R[2,2]<0):
        R=np.matmul(np.diag([1,1,-1]),R)
        Q=np.matmul(Q,np.diag([1,1,-1]))

    A=Q.T
    A = np.where(np.isclose(A, 0) , 0.0 , A)
    return A

# T=-1*np.array([[-2,3,0,7],[-3,0,3,-6],[1,0,0,-2]])
print("matrica K \n",kamera_K(T1))
print("matrica A \n",kamera_A(T1))


