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

sol = input('Nombre de la carpeta de la simulacion: ')
#Create time list
Folders=glob.glob(sol + '*')

timename=[]
for folder in Folders:
    folder=folder.replace(sol,'')
    if isfloat(folder):
        if float(folder)!=0:
            timename.append(folder)

Outdir=''#'Figures/Streamlines/'


x, y, z = flf.readmesh(sol, True)

for t in timename:
    vel = flf.readvector(sol, t, 'U', True)
    #Module of velocity. The quantity is measured transposed, according to stream plot config.
    V=np.sqrt(vel[0, :, :, 0].T**2+vel[1, :, :, 0].T**2)
    #Color plot
    plt.figure(figsize=(6,6))
    plt.title('z = 0 (m)')
    #plt.plot(y[:,:,0],x[:,:,0],'.w')
    plt.streamplot(y[:,:,0],x[:,:,0], vel[0, :, :, 0].T, vel[1, :, :, 0].T,
                   color=V, linewidth=2, cmap=plt.cm.viridis)
    plt.colorbar(fraction=0.046, pad=0.04).ax.set_ylabel('|U| (m/s)')
    plt.ylabel('y (m)')
    plt.xlabel('x (m)')
    plt.xlim(np.amin(x[:,:,0]),np.amax(x[:,:,0]))
    plt.ylim(np.amin(y[:,:,0]),np.amax(y[:,:,0]))
    plt.savefig(Outdir + 'cavity_Str_' + t + '.png')
    plt.close()
