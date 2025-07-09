import pyvista as pv
import numpy as np

path=input(r"Enter text file Path")
with open(path[1:-1]) as file:
    lines = [line.strip().split() for line in file.readlines()]
pathoff=input(r"Enter Coordinate off file")
with open(pathoff[1:-1]) as offile:
    lines2=[line.strip().split() for line in offile.readlines()]

points_limit=lines2[0][0]
dim=int(input("enter dimension"))
points = []
lines_all = []
colors= []
coordinates=[]
index = 0
death=[]
birth=[]
ld= sorted(lines, key=lambda x: (float(x[2]), float(x[3]),float(x[4])))
lb= sorted(lines,key=lambda x: (float(x[0]),float(x[1]),float(x[4])))
for i in range(len(ld)-1):
    if [ld[i][2],ld[i][3]]==[ld[i+1][2],ld[i+1][3]] and ld[i][4]!=ld[i+1][4]:
        death.append([float(ld[i][2]),float(ld[i][3]),0])
        
for i in range(len(lb)-1):
    if [lb[i][0],lb[i][1]]==[lb[i+1][0],lb[i+1][1]] and lb[i][4]!=lb[i+1][4]:
        birth.append([float(lb[i][0]),float(lb[i][1]),0])
for k in lines:
    p1 = [float(k[0]), float(k[1]), 0]
    p2 = [float(k[2]), float(k[3]), 0]
    segment_color=(2/(dim+1))*(int(k[4])+1)
    coordinates.append(lines2[int(k[5])+1])
    
    points.append(p1)
    points.append(p2)
    lines_all.append([2, index, index + 1])
    colors.append(segment_color)
    index += 2


points = np.array(points)
lines_all = np.hstack(lines_all)
colors = np.array(colors)

# Create the PolyData
mesh = pv.PolyData()
mesh.points = points
mesh.lines = lines_all
for i in range(max(dim,3)):
 mesh.cell_data[chr(ord('x')+i)+"coordinates"]=[float(k[i]) for k in coordinates]

mesh.cell_data["Type"] = colors
vtpath=path[1:-4]+"_beta7.vtp"

mesh.save(vtpath)
meshb = pv.PolyData()
meshb.points = np.array(birth)

vtpath=path[1:-4]+"_birth_beta7.vtp"

meshb.save(vtpath)
meshd= pv.PolyData()
meshd.points = np.array(death)




vtpath=path[1:-4]+"_death_beta7.vtp"

meshd.save(vtpath)
