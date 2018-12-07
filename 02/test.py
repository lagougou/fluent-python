symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

beyond_ascii = list(filter(lambda c : c > 127, map(ord,symbols)))
print(beyond_ascii)

colors = ['balck','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)

for tshirt in ('%s %s' % (color, size) for color in colors for size in sizes):
    print(tshirt)

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passort in sorted(traveler_ids):
    print('%s/%s' % passort)

for city, _ in traveler_ids:
    print(city) 


print(divmod(20,8))
t = (20,8)

quotient, remainder = divmod(*t)
print(quotient, remainder)

import os
path,filename = os.path.split('/home/deven/.ssh/idrsa.pub')
print(path,filename)

metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)), # ➊
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

fmt ='{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))


from collections import namedtuple

City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691677))
print(tokyo,tokyo.name,tokyo.coordinates)
print(City._fields)
LatLong = namedtuple('LatLong','lat long')
delhi_data =  ('Delphi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())

for key, val in delhi._asdict().items():
    print(key, val)

weird_board = [['_'] * 3] * 3 
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

t = (1, 2, 3)
print(id(t))
t  += (4,)
print(id(t))

import bisect
import sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:4d}    {2}{0:2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        postion = bisect_fn(HAYSTACK, needle)
        offset = postion * '|' 
        print(ROW_FMT.format(needle, postion, offset))


if __name__ == "__main__":

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print( 'Demo:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' %n for n in HAYSTACK))
    demo(bisect_fn)

def grade(score, breakpoints=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print(grade(40))

import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort_left(my_list, new_item)
    print('%2d ->' %new_item,my_list)
