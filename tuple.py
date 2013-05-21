from collections import namedtuple

point = namedtuple('point',['lt','lo'])

points = [point(1,2),point(3,4),point(5,6)]

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"



def gmaps_img(points):
    markers = '&'.join('markers=%s,%s' % (p.lt, p.lo)
                       for p in points)
    return GMAPS_URL + markers
def gmaps_img1(points):
    s=""
    for p in range(len(points)):
          s = s+'&marker='+str(points[p].lt)+','+str(points[p].lo)
    return GMAPS_URL + s
print gmaps_img(points)
