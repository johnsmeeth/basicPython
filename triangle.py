__author__ = 'thanhnguyen'

# functions
def isTriangle(a, b, c):
    return (a + b > c) & (a + c > b) & (b + c > a)

def deu(a, b, c):
    return (a == b == c)

def vuong(a, b, c):
    return (a ** a == (b ** b) + (c ** c) ) | (b ** b == (a ** a) + (c ** c) ) | (c ** c == (a ** a) + (b ** b) )

def vuongCan(a, b, c):
    return vuong(a, b, c) & (a == b | a == c | b == c)

# data input from keyboard
a = raw_input('Enter a: ') or 3
b = raw_input('Enter b: ') or 4
c = raw_input('Enter c: ') or 5

if isTriangle(a, b, c):
    if deu(a, b, c):
        print "Tam giac deu"
    elif vuong(a, b, c):
        if vuongCan(a, b, c):
            print "Tam giac vuong can"
        else:
            print "Tam giac vuong"
    else:
        print "Tam giac thuong"
else:
    print "Ba canh khong phai la cua 1 tam giac !"
