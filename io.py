
## demo io in python 2.x using raw_input() method which replace by input() method on python 3.x
print "Listen and answer pro v1.0.0"
print "What is your name?"
name = raw_input()
born = int(raw_input('when was you born?'))
sexAsk = "What is your sex?"
sex = raw_input(sexAsk)

print "Thankyou to take this survey"
print """ Special thank to %s , you are %d year old and your sex is %s""" %(name, born, sex)

## take excercise with function
def resolveEquationLevel2():
    # import lib
    import math

    print("---- resolve equation level 2 ")
    a = int(raw_input('Enter a: '))
    b = int(raw_input('Enter b: '))
    c = int(raw_input('Enter c: '))
    delta = b * b - 4 * a * c
    if delta < 0 :
        print "the equation has no root"
    elif delta == 0:
        x = -b / 2 * a
        print "the equation has two double root x1 = x2 = %f" %x
    else:
        x1 = -b + math.sqrt(delta) / 2 * a
        x2 = -b - math.sqrt(delta) / 2 * a
        print "the equation has two separate root x1: %f, x2: %f" %(x1, x2)
resolveEquationLevel2()
