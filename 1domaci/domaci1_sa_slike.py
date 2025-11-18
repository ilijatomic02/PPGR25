import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backend_bases import PickEvent

tacke = []
imena=["1", "2", "3", "5", "6", "7", "8","4"]


def onclick(event):
  global tacke
  if len(tacke) < 7:
    if event.xdata is not None and event.ydata is not None:
      x, y = event.xdata, event.ydata
      tacke.append([int(x), int(y),1])
      if len(tacke) == 7:
        print(f"Odabrane su tacke: {tacke}")
        fig.canvas.mpl_disconnect(cid)
        plt.close()

def prikaztacke():
    fig2, ax2 = plt.subplots()
    ax2.imshow(img)
    for i,p in enumerate(tacke):
        ax2.scatter(p[0], p[1], color="red", s=40)
        ax2.text(p[0] + 5, p[1] - 5, imena[i], color="red",
        fontsize=12, fontweight="bold")
    fig2.savefig("obelezene_tacke.png", dpi=300)
    plt.show()
  

def afinize(p):
    newp=[c/p[-1] for c in p]
    return newp


def osmoteme(tacke):

    xb1=np.round(afinize(np.cross(np.cross(tacke[1],tacke[4]),np.cross(tacke[0],tacke[3]))))
    xb2=np.round(afinize(np.cross(np.cross(tacke[1],tacke[4]),np.cross(tacke[5],tacke[2]))))
    xb3=np.round(afinize(np.cross(np.cross(tacke[5],tacke[2]),np.cross(tacke[3],tacke[0]))))
    
    xb=np.round((xb1+xb2+xb3)/3)

    yb1=np.round(afinize(np.cross(np.cross(tacke[4],tacke[3]),np.cross(tacke[5],tacke[6]))))
    yb2=np.round(afinize(np.cross(np.cross(tacke[1],tacke[0]),np.cross(tacke[4],tacke[3]))))
    yb3=np.round(afinize(np.cross(np.cross(tacke[5],tacke[6]),np.cross(tacke[1],tacke[0]))))
    
    yb=np.round((yb1+yb2+yb3)/3)

    zb1=np.round(afinize(np.cross(np.cross(tacke[1],tacke[2]),np.cross(tacke[4],tacke[5]))))
    zb2=np.round(afinize(np.cross(np.cross(tacke[3],tacke[6]),np.cross(tacke[4],tacke[5]))))
    zb3=np.round(afinize(np.cross(np.cross(tacke[1],tacke[2]),np.cross(tacke[3],tacke[6]))))
    
    zb=np.round((zb1+zb2+zb3)/3)

    p41=np.round(afinize(np.cross(np.cross(xb,tacke[6]),np.cross(yb,tacke[2]))))
    p42=np.round(afinize(np.cross(np.cross(xb,tacke[6]),np.cross(zb,tacke[0]))))
    p43=np.round(afinize(np.cross(np.cross(yb,tacke[2]),np.cross(zb,tacke[0]))))

    p4=np.round((p41+p42+p43)/3)
    return p4


img = mpimg.imread('kutija.jpg')

fig, ax = plt.subplots()
ax.imshow(img)
plt.title("Odaberite redom 7 tacaka (preskocite br. 4)")
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

tacke.append(osmoteme(tacke))
print("koordinate 4 temena su:",tacke[-1])
prikaztacke()

