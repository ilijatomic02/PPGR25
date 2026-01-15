

# ====== PODACI ZA CRTANJE ======
C = centar(T1)[:3]   # centar kamere (x,y,z)
A = kamera_A(T1)     # matrica orijentacije kamere

# vektori osa kamere (iz vrsta matrice A)
cam_x = A[0]
cam_y = A[1]
cam_z = A[2]


# ====== KOCKA ======
cube_vertices = np.array([
    [0,0,0], [3,0,0], [3,3,0], [0,3,0],
    [0,0,3], [3,0,3], [3,3,3], [0,3,3]
])

cube_faces = [
    [cube_vertices[j] for j in [0,1,2,3]],
    [cube_vertices[j] for j in [4,5,6,7]],
    [cube_vertices[j] for j in [0,1,5,4]],
    [cube_vertices[j] for j in [2,3,7,6]],
    [cube_vertices[j] for j in [1,2,6,5]],
    [cube_vertices[j] for j in [0,3,7,4]]
]


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# ====== KOCKA ======
ax.add_collection3d(
    Poly3DCollection(cube_faces, alpha=0.3, facecolor='cyan', edgecolor='k')
)

# ====== SVETSKI KOORDINATNI SISTEM ======
origin = np.array([0,0,0])
ax.quiver(*origin, 1,0,0, color='r', linewidth=2)
ax.quiver(*origin, 0,1,0, color='g', linewidth=2)
ax.quiver(*origin, 0,0,1, color='b', linewidth=2)
ax.text(1,0,0,'X',color='r')
ax.text(0,1,0,'Y',color='g')
ax.text(0,0,1,'Z',color='b')

# ====== KOORDINATNI SISTEM KAMERE ======
scale = 1.5
ax.quiver(*C, *(cam_x*scale), color='darkred', linewidth=3)
ax.quiver(*C, *(cam_y*scale), color='darkgreen', linewidth=3)
ax.quiver(*C, *(cam_z*scale), color='darkblue', linewidth=3)

ax.text(*(C + cam_x*scale), 'Cx', color='darkred')
ax.text(*(C + cam_y*scale), 'Cy', color='darkgreen')
ax.text(*(C + cam_z*scale), 'Cz', color='darkblue')

# ====== PODEŠAVANJA ======
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D scena: kocka, svetski i kamerin koordinatni sistem')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)

plt.show()