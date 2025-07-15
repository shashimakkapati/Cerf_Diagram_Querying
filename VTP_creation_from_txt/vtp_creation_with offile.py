import pyvista as pv
import numpy as np

path=input(r"Enter text file Path in quotes ")
with open(path[1:-1]) as file:
    lines = [line.strip().split() for line in file.readlines()]
pathoff=input(r"Enter Coordinate off file in quotes ")
with open(pathoff[1:-1]) as offile:
    lines2=[line.strip().split() for line in offile.readlines()]

points_limit=lines2[0][0]
dim=int(input("enter dimension "))
points = []
lines_all = []
colors= []
coordinates=[]
index = 0

for k in lines:
    p1 = [float(k[0]), float(k[1]), 0]
    p2 = [float(k[2]), float(k[3]), 0]
    segment_color=(2/(dim+1))*(int(k[4])+1)
    coordinates.append(lines2[int(k[5])+2])
    
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
vtpath=path[1:-4]+"_created.vtp"

mesh.save(vtpath)
