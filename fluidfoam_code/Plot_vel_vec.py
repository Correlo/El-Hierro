import numpy as np
import matplotlib.pyplot as plt
import fluidfoam as flf
import glob

#Function to check if a string can be converted to float
def isfloat(value):

    try:
        float(value)
        return True

    except ValueError:
        return False

#Input file
sol = input('Nombre de la carpeta de la simulacion: ')
#Create time list
Folders=glob.glob(sol + '*')

timename=[]
for folder in Folders:
    folder=folder.replace(sol,'')
    if isfloat(folder):
        if float(folder)!=0:
            timename.append(folder)
Outdir=''#'Figures/Vel_vec/'


x, y, z = flf.readmesh(sol, True, precision = 5)

for t in timename:
    vel = flf.readvector(sol, t, 'U', True, precision = 5)
    V = np.sqrt(vel[0, :, :, 0]**2 + vel[1, :, :, 0]**2)
    #Color plot
    plt.figure(figsize=(6,6))
    plt.title('z = 0 (m)')
    plt.quiver(x[:, :, 0], y[:, :, 0],
           vel[0, :, :, 0]/V, vel[1, :, :, 0]/V, V)
    plt.colorbar().ax.set_ylabel('|U| (m/s)')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.savefig(Outdir + 'cavity_vec_' + t + '.png')
    plt.close()
