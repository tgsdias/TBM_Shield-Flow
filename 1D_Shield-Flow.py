### Input Parameters ###

#Shield
L = 5 #Length(m
R = 5 #Excavation Radius(m)
dRcut = 0.01 #Overcutting(m)
dRtap = 0.01 #Tapering(m)

#1D Calculation Domain
n = 20 #number of nodes
dx = L/n #segment length

#Ground ; Soil
Soil_G = 50 #Shear Modulus (MPa)
Soil_P = 400 #Initial Total Isotropic Stress (kPa)

#Tail void grouting (back)
GrtP = 600 #Grout Pressure (kPa)
GrtYS = 1.5 #Grout Yield Strength (kPa)

#Face Mixture ; Muck (front)
FmxP = 300 #Grout Pressure (kPa)
FmxYS = 0.08 #Grout Yield Strength (kPa)


### Calculations based on pressure ###
X = [i*dx for i in range(n+1)] #domain from front to back
R_initial = [R for i in range(n+1)]
R_shield = [R - dRcut - (i*(dRtap/n)) for i in range(n+1)]
Gap = [R - R_shield[i] for i in range(n+1)]
Gap1 = list(Gap)
P = [0 for i in range(n+1)]
P_Grt = [GrtP for i in range(n+1)]
P_Fmx = [FmxP for i in range(n+1)]
P_Shd = [Soil_P - (2*Gap[i]*Soil_G*1000/R) for i in range(n+1)]
print("Maximum error between 2 consecutive GAP calculations (m):")
while True:
    for i in range(n-1,-1,-1):  #Back to front
        P_Grt[i] = P_Grt[i+1] - (GrtYS*dx*2/(Gap[i+1]+Gap[i]))
    for i in range(1,n+1):      #Front to back
        P_Fmx[i] = P_Fmx[i-1] - (FmxYS*dx*2/(Gap[i-1]+Gap[i]))
    Err = 0
    for i in range(n+1):
        P[i] = max(P_Grt[i],P_Fmx[i],P_Shd[i],0)   
        Gap1[i] = ((P[i] - Soil_P)*R/(2*1000*Soil_G))+(R - R_shield[i])
        if abs(Gap[i]-Gap1[i]) > Err:
            Err = abs(Gap[i]-Gap1[i])
    print(Err)
    Gap = list(Gap1)
    if Err < 1e-10:
        break
R_eq = [R_shield[i] + Gap[i] for i in range(n+1)]


### Graphs ###
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(X, P_Shd, '-k', label='Shield Contact')
plt.plot(X, P_Fmx, '-m', label='Face Mixture')
plt.plot(X, P_Grt, '-g', label='Tail Grouting')
plt.plot(X, P, '-r', label='Resultant')
plt.legend(loc='upper left')
plt.xlabel('Distance from the TBM face (m)')
plt.ylabel('Pressure (kPa)')

plt.figure(2)
plt.plot(X, R_initial, '-b', label='Initial Cavity')
plt.plot(X, R_shield, '-k', label='Shield')
plt.plot(X, R_eq, '-r', label='Deformed Cavity')
plt.legend(loc='upper left')
plt.xlabel('Distance from the TBM face (m)')
plt.ylabel('Radius (m)')
plt.show()
