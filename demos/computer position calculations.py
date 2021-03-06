from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def x_and_y(bearing, distance):
    if 0<bearing<90:
        x = math.sin(math.radians(bearing))*distance
        y = math.cos(math.radians(bearing))*distance
    elif 90<bearing<180:
        x = math.cos(math.radians(bearing-90))*distance
        y = math.sin(math.radians(bearing-90))*distance*-1
    elif 180<bearing<270:
        x = math.sin(math.radians(bearing-180))*distance*-1
        y = math.cos(math.radians(bearing-180))*distance*-1
    else:
        x = math.cos(math.radians(bearing-270))*distance*-1
        y = math.sin(math.radians(bearing-270))*distance
    return x,y

def get_intersections(x0, y0, r0, x1, y1, r1):
    d=sqrt((x1-x0)**2 + (y1-y0)**2)
    if d > r0 + r1 :
        return [[-1,-1],[-1,-1]]
    if d < abs(r0-r1):
        return [[-1,-1],[-1,-1]]
    if d == 0 and r0 == r1:
        return [[-1,-1],[-1,-1]]
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 
        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        return ([[x3, y3], [x4, y4]])


# calculates the distance of the marker from the robot
def calculate_distance(theta,psi,r, num):
	h = (r*cos(radians(theta))) #90-theta
	#z = (r*cos(radians(theta)))
	#x = (h*cos(radians(90-psi)))
	#y = (h*sin(radians(90-psi)))
	#print("x:",x,end = ', ')
	#print("y:",y,end = ', ')
	#print("z:",z)
	return h


# lists of positions
marker_list = [[0,718.75,5750],[1,1437.5,5750],[2,2156.25,5750],[3,2875,5750],[4,3593.75,5750],[5,4312.5,5750],[6,5031.25,5750],[7,5750,5031.25],[8,5750,4312.5],[9,5750,3593.75],[10,5750,2875],[11,5750,2156.25],[12,5750,1437.5],[13,5750,718.75],[14,5031.25,0],[15,4312.5,0],[16,3593.75,0],[17,2875,0],[18,2156.25,0],[19,1437.5,0],[20,718.75,0],[21,0,718.75],[22,0,1437.5],[23,0,2156.25],[24,0,2875],[25,0,3593.75],[26,0,4312.5],[27,0,5031.25]]
central_box = [[2275,2275],[2275,3475],[3475,3475],[3475,2275],[2275,2275]]
arena_border = [[0,0],[0,5750],[5750,5750],[5750,0],[0,0]]
can_list = [[2875,33.5],[2875,1140],[2475,1875],[1625,1625],[3280,1875],[1875,2475],[1875,3280],[1140,2875],[33.5,2875],[2875, 5716.5], [2875, 4610], [3275, 3875], [4125, 4125], [2470, 3875], [3875, 3275], [3875, 2470], [4610, 2875], [5716.5, 2875],[4125,1625],[1625, 4125],[2300, 2575], [2575, 2300], [3450, 2575], [3175, 2300], [3450, 3175], [3175, 3450], [2300, 3175], [2575, 3450]]
point_zone = [[2500,0],[3250,0],[5750,2500],[5750,3250],[3250,5750],[2500,5750],[0,3250],[0,2500],[2500,0]]
start_boxes = [[0,1000],[1000,1000],[1000,0],[4750,0],[4750,1000],[5750,1000],[5750,4750],[4740,4750],[4750,5750],[1000,5750],[1000,4750],[0,4750],[0,1000]]
marker_list = [[0,718.75,5750],[1,1437.5,5750],[2,2156.25,5750],[3,2875,5750],[4,3593.75,5750],[5,4312.5,5750],[6,5031.25,5750],[7,5750,5031.25],[8,5750,4312.5],[9,5750,3593.75],[10,5750,2875],[11,5750,2156.25],[12,5750,1437.5],[13,5750,718.75],[14,5031.25,0],[15,4312.5,0],[16,3593.75,0],[17,2875,0],[18,2156.25,0],[19,1437.5,0],[20,718.75,0],[21,0,718.75],[22,0,1437.5],[23,0,2156.25],[24,0,2875],[25,0,3593.75],[26,0,4312.5],[27,0,5031.25]]


# inputs from robot camera in degrees and mm
# list of markers seen by camera, in order theta, psi, r, marker number
seen_markers = [[-0.0664386764864363, 6.909065636331171, 2000, 1], [-0.810876826732748, -16.131817089783926, 1858, 2]]
#seen_markers = [[90,0,1000,0],[90,35.706691400602884725010135736866,1231.503781,1]]

plt.rcParams["figure.figsize"] = (6,6)
plt.xlim(0,5750)
plt.ylim(0,5750)
plt.gca().set_aspect('equal')
x = []
y = []
for i in range(len(start_boxes)):
	x.append(start_boxes[i][0])
	y.append(start_boxes[i][1])
plt.plot(x,y,'b')

x = []
y = []
for i in range(len(central_box)):
	x.append(central_box[i][0])
	y.append(central_box[i][1])
plt.plot(x,y)
x = []
y = []
for i in range(len(point_zone)):
	x.append(point_zone[i][0])
	y.append(point_zone[i][1])
plt.plot(x,y, linestyle='--', color = 'C1')
x = []
y = []
for i in range(len(arena_border)):
	x.append(arena_border[i][0])
	y.append(arena_border[i][1])
plt.plot(x,y,'b')
x = []
y = []
for i in range(len(can_list)):
	x.append(can_list[i][0])
	y.append(can_list[i][1])
plt.scatter(x,y,color='C4',s=25)

x = []
y = []
for i in range(len(marker_list)):
	x.append(marker_list[i][1])
	y.append(marker_list[i][2])
plt.scatter(x,y,color='b')

for i in range(len(x)):
	if i<7:
		plt.text(x[i], y[i]-80, str(i), horizontalalignment='center', verticalalignment='center', fontsize = 5, color='k')
	elif 6<i<14:
		plt.text(x[i]-100, y[i], str(i), horizontalalignment='center', verticalalignment='center', fontsize = 5, color='k')
	elif 13<i<21:
		plt.text(x[i], y[i]+80, str(i), horizontalalignment='center', verticalalignment='center', fontsize = 5, color='k')
	elif 20<i<28:
		plt.text(x[i]+100, y[i], str(i), horizontalalignment='center', verticalalignment='center', fontsize = 5, color='k')
	else:
		plt.text(x[i], y[i], str(i), horizontalalignment='center', verticalalignment='center', fontsize = 5, color='k')

circles = []
for i in seen_markers:
	point = calculate_distance(i[0],i[1],i[2], i[3])
	circles.append([marker_list[i[3]][1],marker_list[i[3]][2],point])
	print(i, point)

	plt.gca().add_patch(patches.Circle((marker_list[i[3]][1],marker_list[i[3]][2]),point, fill = False, linestyle=':',color = 'C1'))

valid_points = [[],[]]
for i in range(len(circles)):
	if i +1 != len(circles):
		a= i+1
	else:
		a = 0
	points = get_intersections(circles[i][0],circles[i][1],circles[i][2], circles[a][0],circles[a][1],circles[a][2])
	for i in points:
		if 0<i[0]<5750 and 0<i[1]<5750:
			valid_points[0].append(i[0])
			valid_points[1].append(i[1])

print(valid_points)
avg_x = sum(valid_points[0]) / len(valid_points[0])
avg_y = sum(valid_points[1]) / len(valid_points[1])
sum_of = []
markers = []
for i in seen_markers:
	bearing = math.atan2(marker_list[i[3]][1]-avg_x,marker_list[i[3]][2]-avg_y)-math.radians(i[1])
	if bearing < math.radians(0):
		bearing+=math.radians(360)
	elif bearing >math.radians(360):
		bearing -= math.radians(360)
	sum_of.append(bearing)
	markers.append(i[3])
	print(sum_of)
for i in markers:
	plt.scatter(marker_list[i][1],marker_list[i][2], color='C3')
x, y = 0, 0
for i in sum_of:
	x += math.cos(i)
	y += math.sin(i)
bearing = math.degrees(math.atan2(y, x))
if bearing < 0:
	bearing+=360
elif bearing >360:
	bearing -= 360
print(bearing)
fov = 47.5
x_dis,y_dis = x_and_y(bearing,7000)
plt.plot([avg_x,avg_x+x_dis],[avg_y,avg_y+y_dis])
x_dis,y_dis = x_and_y(bearing-(fov/2),7000)
plt.plot([avg_x,avg_x+x_dis],[avg_y,avg_y+y_dis], linestyle='--', color = 'C2')
x_dis,y_dis = x_and_y(bearing+(fov/2),7000)
plt.plot([avg_x,avg_x+x_dis],[avg_y,avg_y+y_dis], linestyle='--', color = 'C2')

plt.scatter(avg_x,avg_y, color = 'C3')# location
plt.axis("off")

plt.savefig(fname = 'figure.png', dpi = 300, transparent = True, bbox_inches='tight', pad_inches=0)
#plt.show()
