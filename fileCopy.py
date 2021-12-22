#A9Q1

f1=open('iter.txt','r')
f2=open('soa.txt','w')

for line in f1:
    f2.write(line)

f1.close()
f2.close()


'''
with open('iter.txt','r') as f1:
    with f2=open('soa.txt','w') as f2:
        for line in f1:
            f2.write(line)

f1.close()
f2.close()

'''
