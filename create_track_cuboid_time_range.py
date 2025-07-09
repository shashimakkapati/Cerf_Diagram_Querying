import pyvista as pv
import numpy as np
import math
path=r"C:\Users\shash\OneDrive\Desktop\Cerf_diagrams\TXT_cerf\Cerf_150_650.txt"
with open(path) as file:
    lines = [line.strip().split() for line in file.readlines()]
pathoff=r"C:\Users\shash\OneDrive\Desktop\Cerf_diagrams\Coordinates_off_files\VortexStreet_2D.off"
with open(pathoff) as offile:
    lines2=[line.strip().split() for line in offile.readlines()]
dim=2
bounds = list(map(float, input("Enter x_min,x_max,y_min,y_max,z_min,z_max,t_min,t_max: ").split(",")))

for i in range(len(bounds)):
    bounds[i]=float(bounds[i])
'''for i in range(len(lines)):
    for j in range(len(lines[i])-2):
        lines[i][j]=str(round(float(lines[i][j]),5))'''
lines = [k for k in lines if not (k[0] == k[2] and k[1] == k[3])]
edges=[]
for k in lines:
    
    coordxyz=lines2[int(float(k[5]))+1]
    
    if bounds[0]<=float(coordxyz[0])<=bounds[1] and bounds[2]<=float(coordxyz[1])<=bounds[3] and bounds[4]<=float(coordxyz[2])<=bounds[5] and bounds[6]<=float(k[0]) and bounds[7]>=float(k[2]):
        edges.append(k)
        
start={}
stop={}


ld= sorted(lines, key=lambda x: (float(x[2]), float(x[3]),float(x[4])))
lb= sorted(lines,key=lambda x: (float(x[0]),float(x[1]),float(x[4])))
for i in range(len(lb)-1):
    start[(lb[i][0],lb[i][1])]=[[lb[i][2],lb[i][3],lb[i][4]]]
    if [lb[i+1][0],lb[i+1][1]]==[lb[i][0],lb[i][1]]:
        start[(lb[i][0],lb[i][1])]+=[[lb[i][2],lb[i][3],lb[i+1][4]]]
for i in range(len(ld)-1):
    stop[(ld[i][2],ld[i][3])]=[[ld[i][0],ld[i][1],ld[i][4]]]
    if [ld[i+1][2],ld[i+1][3]]==[ld[i][2],ld[i][3]]:
        stop[(ld[i][2],ld[i][3])]+=[[ld[i][0],ld[i][1],ld[i+1][4]]]

def right(t,f,color):
    if (t,f) not in start.keys():
        return None
    else:
        for k in start[(t,f)]:
            if k[2]==color:
                return k
            else:
                return None
def left(t,f,color):
    if (t,f) not in stop.keys():
        return []
    else:
        for k in stop[(t,f)]:
            if k[2]==color:
                return k
            else:
                return None
def left_travel(t,f,color):
    left_points=[]
    while left(t,f,color):
        
        
        t,f,color=left(t,f,color)
        left_points.append([float(t),float(f),0])
    left_points.reverse()
    return left_points
def right_travel(t,f,color):
    right_points=[]
    while right(t,f,color):
        
        
        t,f,color=right(t,f,color)
        right_points.append([float(t),float(f),0])

    
    
    return right_points

track_points=[]
track_lines=[]
counter=0
color=[]
for k in edges:
    
    t1=k[0]
    f1=k[1]
    t2=k[2]
    f2=k[3]
    index=k[4]
    
    points=left_travel(t1,f1,index)+[[float(t1),float(f1),0]]+[[float(t2),float(f2),0]]+right_travel(t2,f2,index)
    lines_all=[[2,i,i+1] for i in range(counter,counter+len(points)-1)]
    for p in range(len(lines_all)):
        line_color=(2/(dim+1))*(int(k[4])+1)
        color.append(line_color)
    track_lines+=lines_all
    counter+=len(points)
    track_points+=points

mesh = pv.PolyData()
mesh.points = np.array(track_points)

mesh.lines = np.array(track_lines)


mesh.cell_data["Type"] = np.array(color)

vtpath=path[0:-3]+"_imp_complex_lines_beta7.vtp"

mesh.save(vtpath)
