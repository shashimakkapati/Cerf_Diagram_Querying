import pyvista as pv
import numpy as np
import math
path=r"C:\Users\shash\OneDrive\Desktop\Cerf_diagrams\TXT_cerf\Cerf_150_650.txt"
with open(path) as file:
    lines = [line.strip().split() for line in file.readlines()]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j]=str(round(float(lines[i][j]),4))
edge=eval(input("enter t1 f1"))
t_min=min([float(k[0]) for k in lines])
t_max=max([float(k[2]) for k in lines])
f_min=min([float(k[1]) for k in lines])
f_max=max([float(k[3]) for k in lines])

t_bound=float(t_max)-float(t_min)
f_bound=float(f_max)-float(f_min)
scale=[1481/t_bound,609/f_bound,1]
t=round(float(edge[0])/scale[0],4)
f=round(float(edge[1])/scale[1],4)

cerf_line=[]
dist=math.fabs(float(lines[0][0])-t)+math.fabs(float(lines[0][1])-f)
for k in lines:
    if math.fabs(float(k[0])-t)<2 and math.fabs(float(k[1])-f)<2:
        cerf_dist=math.fabs(float(k[0])-t)+math.fabs(float(k[1])-f)
        if cerf_dist<dist:
            cerf_line=k
            dist=cerf_dist
if not cerf_line:
    print("error")
print("nearest cerf diagram edge",cerf_line)
t1=cerf_line[0]
f1=cerf_line[1]
t2=cerf_line[2]
f2=cerf_line[3]
points = []
lines_all = []
colors= []
coordinates=[]
index = 0
start={}
stop={}
lines = [k for k in lines if not (k[0] == k[2] and k[1] == k[3])]

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

points=left_travel(t1,f1,start[(t1,f1)][0][2])+[[float(t1),float(f1),0]]+[[float(t2),float(f2),0]]+right_travel(t2,f2,stop[(t2,f2)][0][2])
lines_all=[[2,i,i+1] for i in range(len(points)-1)]

points = np.array(points)
lines_all = np.hstack(lines_all)

# Create the PolyData
mesh = pv.PolyData()
mesh.points = points
mesh.lines = lines_all



vtpath=path[0:-3]+"_line_beta7.vtp"

mesh.save(vtpath)
