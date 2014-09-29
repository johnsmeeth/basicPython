from fileOperation import printFile
def resolveEquation():
    a = raw_input('Enter a: ') or 3
    b = raw_input('Enter b: ') or 4
    c = raw_input('Enter c: ') or 10

    result = int((c - b) / a)
    print "x = %d" %result


def interreview():
    name = raw_input('What is your name?') or "Thanh Nguyen"
    born = raw_input('When was you born?') or "1989"
    married = raw_input('Are you get married?') or "Yes"

    print "---------- your information -----------"
    print "your name: %s " %name
    print "your born: %s" %born
    print "your married status: %s" %married

    answer = raw_input('Would you like to save information to file?(yes/no)') or "yes"
    if answer == "yes":
        saveToFile()

    f = open("data.txt", "r+")
    printFile(f)

def saveToFile():
    file = raw_input('Enter file do you want to append?: ') or "data.txt"
    f = open(file, "w")
    f.write(name + "\n" + born + "\n" + married)
    f.close()

#resolveEquation()


