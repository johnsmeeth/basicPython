__author__ = 'thanhnguyen'
cars = ["Mercedes", "Audi", "Lexus", "BMW"]

# loop use for..in
for car in cars:
    print car

# loop use while

i = 0
while i < cars.count(8) - 1: # parameter of count method can be any digit
    i += 1
    print cars[i]


odd = [1, 3, 5, 7, 9]
squareOdd = [item ** 2 for item in odd]

print squareOdd

try:
    print "try run"
except e:
    print "catch run, ", e




