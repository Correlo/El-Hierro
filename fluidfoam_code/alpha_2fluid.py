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

Outdir='Figures/alpha/'

x, y, z = flf.readmesh(sol, True, precision = 5)

for t in timename:
    alpha = flf.readscalar(sol, t, 'alpha.water', True, precision = 5)
    #Color plot
    plt.figure(figsize = (5,6))
    plt.title('z = 0 (m)')
    plt.imshow(alpha[:,:,0].T, origin = 'lower' , extent=[np.amin(x),np.amax(x),np.amin(y),np.amax(y)])
    plt.colorbar().ax.set_ylabel(r'$\alpha$')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.tight_layout()
    plt.savefig(Outdir + 'alpha_' + t + '.png')
    plt.close()
