'''
Oh you expected a real test suite like nose/pytest/unittest/doctest
not today
Just tested if the data is actually there.

TODO:
Implement try/catch. The software will brake under any circumstances 
(i.e. no internet, missing data, wrong data input)
without providing much useful information.
'''
from data.data import load


file = load('file')

print(file[0][0][0], '-- is the picture')
print(file[0][0][1], '-- is the page link')
print(file[0][0][2], '-- is the title')
print(file[0][0][3], '-- is the price')
print(file[0][0][4], '-- are the views')
print(file[0][0][5], '-- is the loc')
