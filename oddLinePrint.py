f1=open('copy1.txt','w')
f2=open('copy2.txt','w')

sen=input('Enter the sentence :')
while(sen!=''):
    f1.write(sen)
    sen=input('Enter the sentence : ')

#write logic
for line in f1:
    
        f2.write(line)

f1.close()
f2.close()

f3=open('copy2.txt','r')

print(f3.read())
