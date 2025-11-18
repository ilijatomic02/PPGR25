import numpy as np

#test rucni unos
p1=[959,484,1]
p2=[308,746,1]
p3=[72,460,1]
p4=[0,0,1]
p5=[1159,208,1]
p6=[360,439,1]
p7=[64,150,1]
p8=[809,30,1]

def afinize(p):

    newp=[c/p[-1] for c in p]
    return newp


def osmoteme():

    xb1=np.round(afinize(np.cross(np.cross(p2,p6),np.cross(p1,p5))))
    xb2=np.round(afinize(np.cross(np.cross(p2,p6),np.cross(p7,p3))))
    xb3=np.round(afinize(np.cross(np.cross(p7,p3),np.cross(p5,p1))))
    
    xb=np.round((xb1+xb2+xb3)/3)

    yb1=np.round(afinize(np.cross(np.cross(p6,p5),np.cross(p7,p8))))
    yb2=np.round(afinize(np.cross(np.cross(p2,p1),np.cross(p6,p5))))
    yb3=np.round(afinize(np.cross(np.cross(p7,p8),np.cross(p2,p1))))
    
    yb=np.round((yb1+yb2+yb3)/3)

    zb1=np.round(afinize(np.cross(np.cross(p2,p3),np.cross(p6,p7))))
    zb2=np.round(afinize(np.cross(np.cross(p5,p8),np.cross(p6,p7))))
    zb3=np.round(afinize(np.cross(np.cross(p2,p3),np.cross(p5,p8))))
    
    zb=np.round((zb1+zb2+zb3)/3)

    p41=np.round(afinize(np.cross(np.cross(xb,p8),np.cross(yb,p3))))
    p42=np.round(afinize(np.cross(np.cross(xb,p8),np.cross(zb,p1))))
    p43=np.round(afinize(np.cross(np.cross(yb,p3),np.cross(zb,p1))))

    p4=np.round((p41+p42+p43)/3)
    print(p4)

    
osmoteme()