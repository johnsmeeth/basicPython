__author__ = 'thanhnguyen'

cars = ["Audi", "BMW", "Mercedes"]

for car in cars:
    print car

print "--------------"

n = 0
while n < len(cars):
    print cars[n], len(cars[n])
    n += 1


print "Using range method to create an array"
for i in range(10):
    print i,

print '\nlist created from start and end use range'
for i in range(4, 9):
    print i,

print '\nlist created from start, end, step use range'
for i in range(0, 10, 2):
    print i,

print '\n Combine range, len and for'
for i in range(len(cars)):
    print i, cars[i]

print '\nExercise GIAITHUA'
def gt(n):
    if n <= 1:
        return 1
    else:
        return n * gt(n-1)

n = int(raw_input('Enter n: '))
print n, "! = ", gt(n)