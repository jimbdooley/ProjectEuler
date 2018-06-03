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
    
def find_volume_of_cuboid_union(cuboids):
	#TODO, find a better solution that doesn't time out
    pass

    
cuboids = make_cuboid_list([53,54,48,257,51,81,2])
#cuboids = make_cuboid_list([10**4,10**4,10**4,399,399,399,100])
print(cuboids)
total_volume = find_volume_of_cuboid_union(cuboids)
print(total_volume)
