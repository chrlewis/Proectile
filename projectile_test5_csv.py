''' projectile_motion.py
projectile motion equations:
height = y(t) = hs + (t * v * sin(a)) - (g * t*t)/2
distance = x(t) = v * cos(a) * t
where:
t is the time in seconds
v is the velocity of the projectile (meters/second)
a is the firing angle with repsect to ground (radians)
hs is starting height with respect to ground (meters)
g is the gravitational pull (meters/second_square)
'''
import math
import csv
initial_velocity=float(input('What is the initial velocity?'))
initial_height=float(input('what is the initial height?'))
shooting_angle=float(input('measured from horizontal, what is the shooting angle?'))
outputfile = open ('Projectile.csv', 'w',) #set name of output file, w for write
DataWriter = csv.writer(outputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) # Create writer object
DataWriter.writerow(['X_Pos (x)','Y_Pos (y)']) # Write column headers for X and Y coordinates


def projectile_xy(v, a, hs=initial_height, g=9.8):
    '''
    calculate a list of (x, y) projectile motion data points
    where:
    x axis is distance (or range) in meters
    y axis is height in meters
    v is velocity of the projectile (meter/second)
    a is the firing angle with repsect to ground (radians)
    hs is starting height with respect to ground (meters)
    g is the gravitational pull (meters/second_square)
    '''
    data_xy = []
    t = 0.0
    while True:
        # now calculate the height y
        y = (hs + (t * v * math.sin(a)) - (g * t * t)/2)*100
        # projectile has hit ground level
        if y < 0:
            break
        # calculate the distance x
        x = (v * math.cos(a) * t)*100
        # append the (x, y) tuple to the list
        data_xy.append((x, y))
        # use the time in increments of 0.1 seconds
        t += 0.03
        DataWriter.writerow([str(x),str(y)])
    return data_xy
# use a firing angle of d degrees
d = shooting_angle
a = math.radians(d)  # radians
# velocity of the projectile (meters/second)
v = initial_velocity
data_result = projectile_xy(v, a)

# find maximum height ...
point_height_max = max(data_result, key = lambda q: q[1])
xm, ym = point_height_max
outputfile.close()
print('''
    Projectile Motion ...
Using a firing angle of {} degrees
and a velocity of {} meters/second
the maximum height is ({:0.1f}/100) meters
at a distance of ({:0.1f}/100) meters,'''.format(d, v, ym, xm))
# find maximum distance ...
x_max = int(max(data_result)[0])/100
print("the maximum distance is ({:0.1f}) meters.".format(x_max))
print("Lower height of center of mass in goal is 2.4m")
print("Upper height of center of mass in goal is 2.7m")
''' result ...
    Projectile Motion ...
Using a firing angle of 45 degrees
and a muzzle velocity of 100 meters/second
the maximum height is 255.1 meters
at a distance of 509.1 meters,
the maximum distance is 1018.2 meters.
'''
