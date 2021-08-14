#Import Packages
import os
import numpy as np
import matplotlib.pyplot as plt

#Change Working Directory
os.chdir(r'C:\Users\malva\Thesis\GIS\Pipeline')
path =(r'C:\Users\malva\Desktop\Test')
       
#Read Data
dem = np.loadtxt('DEM.asc', skiprows=6)
dem[dem == -9999] = np.nan
resolution = 5

#Plot
# plt.imshow(dem, interpolation='none', origin='lower')
# plt.colorbar()
# plt.title('Elevation')
# plt.savefig(path + '\elevation.png', dpi=300)
# plt.show()

#####

def CalcularCelda(i, j, Z):
    for n in range(-1, 2, 1):
        for m in range(-1, 2, 1):
            if Z[i+n][j+m] == np.nan:
                return np.nan
    
    jdx = np.array([-1, 0, 1, -1, 1, -1, 0, 1])
    idy = np.array([-1, -1, -1, 0, 0, 1, 1, 1])
    fdirs = np.array([8, 7, 6, 1, 5, 2, 3, 4])
    
    fdir = np.nan
    max_slope = -1
    
    for s in range(8):
        z1 = Z[i+idy[s]][j+jdx[s]]
        z0 = Z[i][j]
        
        if np.abs(jdx[s]+idy[s])==1:
            local_slope = (z1-z0)/resolution
        else:
            local_slope = (z1-z0)/(resolution*np.sqrt(2))
        
        if local_slope > max_slope:
            max_slope = local_slope
            fdir = fdirs[s]
            
    return fdir


def CrearResultados(Z):
    nrows = Z.shape[0]
    ncols = Z.shape[1]

    FDir = np.empty([nrows, ncols])
    FDir[:] = np.nan
    
    for i in range(1, nrows-1):
        for j in range(1, ncols-1):
            FDir[i][j] = CalcularCelda(i, j, Z)
    return FDir

	
####

fdir = CrearResultados(dem)

#Plot
plt.imshow(fdir, interpolation='none', origin='lower')
plt.colorbar()
plt.title('FDir')
# plt.savefig(path + '\\slope.png', dpi=300)
plt.show()