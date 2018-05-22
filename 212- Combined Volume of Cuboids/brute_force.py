'''
the strategy to find the union volume is to push a plane through all of 3d space
for each step it takes, push a line through that plane. 
and for each step that line takes, push a point through the line 
while doing this: increment the total volume for each step the point takes while inside a rectangle
since this problem deals with cubes, we can go in chunks instead of continuously

'''
import heapq
import sets

def find_existence_of_points(points):
    if len(points) > 0:
        return 1
    return 0

def find_length_of_line_union(segments_in_lines,cuboids):
    if len(segments_in_lines) == 0:
        return 0
    segment_start = []
    segment_stop = []
    for i in segments_in_lines:
        segment_start.append((cuboids[i][0][2],i))
        segment_stop.append((cuboids[i][0][2]+cuboids[i][1][2],i))
    heapq.heapify(segment_start)
    heapq.heapify(segment_stop)
    
    length = 0
    points = sets.Set()
    start = min(segment_start[0][0],segment_stop[0][0])
    while len(segment_start) > 0:
        while True:
            if len(segment_start) == 0:
                break
            if segment_start[0][0] == start:
                points.add(heapq.heappop(segment_start)[1])
            else:
                break
        while True:
            if segment_stop[0][0] == start:
                points.remove(heapq.heappop(segment_stop)[1])
            else:
                break
        if len(segment_start)> 0:
            stop = min(segment_start[0][0],segment_stop[0][0])
        else:
            stop = segment_stop[0][0]
        length += (stop-start)*find_existence_of_points(points)
        start = stop
    while len(segment_stop) > 0:
        while True:
            if len(segment_stop) == 0:
                break
            if segment_stop[0][0] == start:
                points.remove(heapq.heappop(segment_stop)[1])
            else:
                break
        if len(segment_stop) > 0:
            stop = segment_stop[0][0]
        else:
            break
        length += (stop-start)*find_existence_of_points(points)
        start = stop
    return length
    
def find_area_of_rectangle_union(rectangles_in_plane,cuboids):
    if len(rectangles_in_plane) == 0:
        return 0
    rectangle_start = []
    rectangle_stop = []
    for i in rectangles_in_plane:
        rectangle_start.append((cuboids[i][0][1],i))
        rectangle_stop.append((cuboids[i][0][1]+cuboids[i][1][1],i))
    heapq.heapify(rectangle_start)
    heapq.heapify(rectangle_stop)
    
    area = 0
    lines = sets.Set()
    start = min(rectangle_start[0][0],rectangle_stop[0][0])
    while len(rectangle_start) > 0:
        while True:
            if len(rectangle_start) == 0:
                break
            if rectangle_start[0][0] == start:
                lines.add(heapq.heappop(rectangle_start)[1])
            else:
                break
        while True:
            if rectangle_stop[0][0] == start:
                lines.remove(heapq.heappop(rectangle_stop)[1])
            else:
                break
        if len(rectangle_start)> 0:
            stop = min(rectangle_start[0][0],rectangle_stop[0][0])
        else:
            stop = rectangle_stop[0][0]
        area += (stop-start)*find_length_of_line_union(lines,cuboids)
        start = stop
    while len(rectangle_stop) > 0:
        while True:
            if len(rectangle_stop) == 0:
                break
            if rectangle_stop[0][0] == start:
                lines.remove(heapq.heappop(rectangle_stop)[1])
            else:
                break
        if len(rectangle_stop) > 0:
            stop = rectangle_stop[0][0]
        else:
            break
        area += (stop-start)*find_length_of_line_union(lines,cuboids)
        start = stop
    return area
            
def find_volume_of_cuboid_union(cuboids):
    cuboid_start = []
    cuboid_stop = []
    for i in range(len(cuboids)):
        cuboid_start.append((cuboids[i][0][0],i))
        cuboid_stop.append((cuboids[i][0][0]+cuboids[i][1][0],i))
    heapq.heapify(cuboid_start)
    heapq.heapify(cuboid_stop)
    
    volume = 0
    rectangles = sets.Set()
    start = min(cuboid_start[0][0],cuboid_stop[0][0])
    while len(cuboid_start) > 0:
        while True:
            if len(cuboid_start) == 0:
                break
            if cuboid_start[0][0] == start:
                rectangles.add(heapq.heappop(cuboid_start)[1])
            else: 
                break
        while True:
            if cuboid_stop[0][0] == start:
                rectangles.remove(heapq.heappop(cuboid_stop)[1])
            else:
                break
        if len(cuboid_start) > 0:
            stop = min(cuboid_start[0][0],cuboid_stop[0][0])
        else:
            stop = cuboid_stop[0][0]
        volume += (stop-start)*find_area_of_rectangle_union(rectangles,cuboids)
        start = stop
        
    while len(cuboid_stop) > 0:
        while True:
            if len(cuboid_stop) == 0:
                break
            if cuboid_stop[0][0] == start:
                rectangles.remove(heapq.heappop(cuboid_stop)[1])
            else:
                break
        if len(cuboid_stop) > 0:
            stop = cuboid_stop[0][0]
        else:
            break
        volume += (stop-start)*find_area_of_rectangle_union(rectangles,cuboids)
        start = stop
    return volume
  

    
    
    

cuboids0 = [
[[0,0,0],[2,2,2]],
[[2,2,2],[2,2,2]],
[[1,1,1],[2,2,2]],
[[2,3,3],[4,2,2]],
[[10,10,10],[1,1,1]]]

cuboids1 = [
[[-1,-1,-1],[2,2,2]],
[[1,1,1],[2,2,2]]]

print(find_volume_of_cuboid_union(cuboids0))

solved = {}
def lagged_fib(k):
    if k <= 55:
        return (100003 - 200003*k + 300007*(k**3)) % (10**6)
    else:
        if k in solved:
            return solved[k]
        rtn = (lagged_fib(k-24) + lagged_fib(k-55)) % (10**6)
        solved[k] = rtn
        return rtn
        
def make_cuboid_list(vals):
    cuboids = []
    for n in range(1,vals[6]+1):
        x0y0z0 = [
        lagged_fib(6*n-5)%vals[0],
        lagged_fib(6*n-4)%vals[1],
        lagged_fib(6*n-3)%vals[2]]
        dxdydz = [
        1+(lagged_fib(6*n-2)%vals[3]),
        1+(lagged_fib(6*n-1)%vals[4]),
        1+(lagged_fib(6*n-0)%vals[5])]
        cuboids.append([x0y0z0,dxdydz])
    return cuboids
    
#cuboids = make_cuboid_list([53,54,48,257,51,81,2])
cuboids = make_cuboid_list([10**4,10**4,10**4,399,399,399,100])
print(cuboids)
total_volume = find_volume_of_cuboid_union(cuboids)
print(total_volume)
