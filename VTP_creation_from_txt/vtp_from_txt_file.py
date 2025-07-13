import pyvista as pv
import numpy as np

path=input(r"Enter text file Path ")
with open(path[1:-1]) as file:
    lines = [line.strip().split() for line in file.readlines()]
dim=int(input("enter dimension "))
points = []
lines_all = []
colors= []

index = 0
for k in lines:
    p1 = [float(k[0]), float(k[1]), 0]
    p2 = [float(k[2]), float(k[3]), 0]
    segment_color=(2/(dim+1))*(int(k[4])+1)
    
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


mesh.cell_data["Type"] = colors
vtpath=path[1:-4]+"_created_without_off.vtp"

mesh.save(vtpath)
