#import required libraries
import math

#Getting the data
n=int(input("Enter number of polygon points:"))

# Input all coordinate
x=[]
y=[]
print("")
print("Enter coordinate x and y...")
print("")
for i in range(n):
    point=(input(f"Point {i+1}: "))
    xy=(point.split(sep=" "))
    x.append(float(xy[0]))
    y.append(float(xy[1]))

#Calculation geometric characteristics
Ax=0
Sx=0
Sy=0
Ix=0
Iy=0
Ixy=0
xt=0
yt=0
Ixt=0
Iyt=0
Ixyt=0
for i in range(n):
    if (i+1)==n:
        Ax=Ax+0.5*(x[i]+x[0])*(y[0]-y[i])
        Sx=Sx+(-1/6)*(x[0]-x[i])*(y[0]**2+y[i]*y[0]+y[i]**2)
        Sy=Sy+(1/6)*(y[0]-y[i])*(x[0]**2+x[i]*x[0]+x[i]**2)
        Ix=Ix+(-1/12)*(x[0]-x[i])*((y[0]**3)+y[i]*(y[0]**2)+(y[i]**2)*y[0]+y[i]**3)
        Iy=Iy+(1/12)*(y[0]-y[i])*((x[0]**3)+x[i]*(x[0]**2)+(x[i]**2)*x[0]+x[i]**3)
        Ixy=Ixy+(-1/24)*(y[0]-y[i])*(y[0]*(3*(x[0]**2)+2*x[0]*x[i]+x[i]**2)+y[i]*(3*(x[i]**2)+2*x[0]*x[i]+x[0]**2))
    else:
        Ax=Ax+0.5*(x[i]+x[i+1])*(y[i+1]-y[i])
        Sx=Sx+(-1/6)*(x[i+1]-x[i])*(y[i+1]**2+y[i]*y[i+1]+y[i]**2)
        Sy=Sy+(1/6)*(y[i+1]-y[i])*(x[i+1]**2+x[i]*x[i+1]+x[i]**2)
        Ix=Ix+(-1/12)*(x[i+1]-x[i])*((y[i+1]**3)+y[i]*(y[i+1]**2)+(y[i]**2)*y[i+1]+y[i]**3)
        Iy=Iy+(1/12)*(y[i+1]-y[i])*((x[i+1]**3)+x[i]*(x[i+1]**2)+(x[i]**2)*x[i+1]+x[i]**3)
        Ixy=Ixy+(-1/24)*(y[i+1]-y[i])*(y[i+1]*(3*(x[i+1]**2)+2*x[i+1]*x[i]+x[i]**2)+y[i]*(3*(x[i]**2)+2*x[i+1]*x[i]+x[i+1]**2))
    
xt= Sy / Ax
yt= Sx / Ax
Ixt= Ix-(yt*yt)*Ax
Iyt= Iy-(xt*xt)*Ax
Ixyt= Ixy + xt * yt * Ax

#print x and y coordinates of polygon points
print("")
print("Point    Coord. X   Coord. Y")
print("------------------------------")
for i in range(n):
    print(f"{i+1:3.0f} {x[i]:10.2f} {y[i]:10.2f}")

print("")
#print results geometric characteristics
print(f"Ax:{Ax:10.2f}")
print(f"Sx:{Sx:10.2f}")
print(f"Sy:{Sy:10.2f}")
print(f"Ix:{Ix:10.2f}")
print(f"Iy:{Iy:10.2f}")
print(f"Ixy:{Ixy:9.2f}")
print(f"xt:{xt:10.2f}")
print(f"yt:{yt:10.2f}")
print(f"Ixt:{Ixt:9.2f}")
print(f"Iyt:{Iyt:9.2f}")
print(f"Ixyt:{Ixyt:8.2f}")