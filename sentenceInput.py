f1=open('cse.txt','w')
sen=input('Enter the sentence :')
while(sen!=''):
    f1.write(sen)
    sen=input('Enter the sentence : ')

f1.close()
f2=open('cse.txt','r')
print(f2.read())
