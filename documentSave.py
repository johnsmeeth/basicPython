__author__ = 'thanhnguyen'

name = raw_input('Enter your name:')
age = raw_input('Enter your age: ')
sex = raw_input('Enter your sex: ')

# write to file
f = open("data.txt", "r+")
f.write("-----------------------------------------\n")
f.write("\n" + name)
f.write("\n" + age)
f.write("\n" + sex)
f.close()
print "Save success !"

# read file to see change
f = open("data.txt", "r+")
print f.read()
f.close()
