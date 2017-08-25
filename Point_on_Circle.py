# x = cx + r * cos(a)
# y = cy + r * sin(a)

import math
import time


def point_on_circle(center_x, center_y, radius, angle):
    # generate a sequence of (x,y) coords to simulate a point moving on a circumference

    # center_x   X coordinate of circle center
    # center_y   Y coordinate of circle center
    # radius     radius of the circle
    # angle      value of angle to calculate the point

    px = float(center_x) + float(radius) * math.cos(math.radians(float(angle)))
    py = float(center_y) + float(radius) * math.sin(math.radians(float(angle)))

    return px, py


# speed      time to pause between a move and the next one. small value = fast, large value = slow

cnx = input('Enter center X: ')
cny = input('Enter center Y: ')
ray = input('Enter circle radius: ')
ang = input('Enter angle in deegrees to calulate (only integer not decimals): ')
step = input('Enter time between calculation: ')

slot = range(0, 360, int(ang))

for e in slot:
    Point = point_on_circle(cnx, cny, ray, e)
    print("Angle = %d\tX = %.4f\tY = %.4f" % (e, Point[0], Point[1]))
    time.sleep(float(step))


