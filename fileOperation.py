#coding: utf-8
## work with file
# define functions
def printFile(file):
    # move cursor to first of file
    file.seek(0)
    print "All contents of file %s has size %d" %(file.name, int(file.read().__len__()))
    file.seek(0)
    print file.read()

file = raw_input('Enter file that you want to work - include path?: ') or "data.txt"

# open file
f = open(file, "r+")
printFile(f)

answer = raw_input('Would you like to add more something?(yes/no): ') or "yes"
if answer == "yes":
    newContent = str(raw_input('Enter something you want to add: ')) or "\nThis is new content to add"
    f.write(newContent)
    printFile(f)
else:
    print "Goodbye by ctrl + d"
