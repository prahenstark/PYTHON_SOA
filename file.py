f=open("iter.txt", 'w')
f.write("iter is good+.\n")
f.write("iter is good++.\n")
f.write("iter is good+++.\n")
f.close()


f3=open('iter.txt','a')
f3.write('abey kitna good bolega.\n')
f3.close()


f2=open('iter.txt','r')
#print(f2.read())

#print(f2.readline())      #print one line i.e till \n
#print(f2.readlines())     #returns list of all contents

