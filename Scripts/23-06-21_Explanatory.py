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
plt.imshow(dem, interpolation='none', origin='lower')
plt.colorbar()
plt.title('Elevation')
plt.savefig(path + '\elevation.png', dpi=300)
plt.show()

#####

def CalcularCelda(i, j, Z):
    for n in range(-1, 2, 1):
        for m in range(-1, 2, 1):
            if Z[i+n][j+m] == np.nan:
                return np.nan
            
    z1 = Z[i-1][j-1]
    z2 = Z[i-1][j]
    z3 = Z[i-1][j+1]
    z4 = Z[i][j-1]
    z5 = Z[i][j]
    z6 = Z[i][j+1]
    z7 = Z[i+1][j-1]
    z8 = Z[i+1][j]
    z9 = Z[i+1][j+1]
    
    p = (z3 + z6 + z9 - z1 - z4 - z7)/(6*resolution)
    
    q = (z1 + z2 + z3 - z7 - z8 - z9)/(6*resolution)
    
    r = (z1 + z3 + z4 + z6 + z7 + z9 - 2*(z2 + z5 + z8))/(3*np.power(resolution,2))
    s = (-z1 + z3 + z7 - z9)/(4*np.power(resolution, 2))
    t = (z1 + z2 + z3 + z7 + z8 + z9 - 2*(z4 + z5 + z6))/(3*np.power(resolution,2))
    
    pendiente = np.arctan(np.sqrt(p*p + q*q))*180/np.pi
    pendiente = np.round(pendiente, 5)
    
    orientacion = np.arctan2(p,q)*180/np.pi
    orientacion = np.round(orientacion, 5)
    if pendiente == 0:
        orientacion = np.nan
    if orientacion < 0:
        orientacion = orientacion + 360
    
    kv = (-1*np.power(p,2)*r + 2*p*q*r*s + np.power(q,2)*t)/((np.power(p,2) + np.power(q,2))*np.sqrt(np.power(1 + np.power(p,2) + np.power(q,2),3)))
    kh = (p*q*s - np.power(p,2)*t - np.power(q,2)*r)/((np.power(p,2) + np.power(q,2))*np.sqrt(1 + np.power(p,2) + np.power(q,2)))
        
    return pendiente, orientacion, kv, kh


def CrearResultados(Z):
    nrows = Z.shape[0]
    ncols = Z.shape[1]

    S = np.empty([nrows, ncols])
    S[:] = np.nan
    A = np.empty([nrows, ncols])
    A[:] = np.nan
    K1 = np.empty([nrows, ncols])
    K1[:] = np.nan
    K2 = np.empty([nrows, ncols])
    K2[:] = np.nan
    
    for i in range(1, nrows-1):
        for j in range(1, ncols-1):
            s, a, k1, k2 = CalcularCelda(i, j, Z)
            S[i][j] = s
            A[i][j] = a
            K1[i][j] = k1
            K2[i][j] = k2
    return S, A, K1, K2

	
####

slope, aspect, curv_plan, curv_prof = CrearResultados(dem)

#Plot
plt.imshow(slope, interpolation='none', origin='lower')
plt.colorbar()
plt.title('Slopes')
plt.savefig(path + '\\slope.png', dpi=300)
plt.show()

#Plot
plt.imshow(aspect, interpolation='none', origin='lower')
plt.colorbar()
plt.title('Aspect')
plt.savefig(path + '\\aspect.png', dpi=300)
plt.show()

#Plot
plt.imshow(aspect, interpolation='none', origin='lower')
plt.colorbar()
plt.title('Aspect')
plt.savefig(path + '\\aspect.png', dpi=300)
plt.show()

#Plot
plt.imshow(curv_plan, interpolation='none', origin='lower')
plt.colorbar()
plt.title('Curvature Plan')
plt.savefig(path + '\\curv_plan.png', dpi=300)
plt.show()

#Plot
plt.imshow(curv_prof, interpolation='none', origin='lower')
plt.colorbar()
plt.title('Curvature Profile')
plt.savefig(path + '\\curv_prof.png', dpi=300)
plt.show()