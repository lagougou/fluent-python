from collections import abc
my_dict = {}
print(isinstance(my_dict,abc.Mapping))

a = dict(one=1, two=2, three=3)
b = {'one':1}

DIAL_CODES = [(86,'China'),(91,'India'),(1,'United States'),
                (62,'Indonesia'),(55,'Brazil'),(92, 'Pakistan'),
                (880, 'Bangladesh'),(234, 'Nigeria'),(7,'Russia')]

country_code = {country: code  for code, country in DIAL_CODES }
print(country_code)
from dis import dis

dis('{1}')

from unicodedata import name
uni_char = {chr(i) for i in range (32,256) if 'SIGN' in name(chr(i),'')}
print(uni_char)


DIAL_CODES = [
(86, 'China'),
(91, 'India'),
(1, 'United States'),
(62, 'Indonesia'),
(55, 'Brazil'),
(92, 'Pakistan'),
(880, 'Bangladesh'),
(234, 'Nigeria'),
(7, 'Russia'),
(81, 'Japan'),
]
d1 = dict(DIAL_CODES) 
print('d1:', d1)
d2 = dict(sorted(DIAL_CODES)) 
print('d2:', d2)
d3 = dict(sorted(DIAL_CODES,key = lambda x:x[1]))
print('d3:', d3)
assert d2 == d3 

