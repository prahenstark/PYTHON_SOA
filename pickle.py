import pickle
try:
    f1=open("myfile.dat","wb")
    list1=[1,2,3,4,5,6,7,8,9,10]
    dict1={111:"Asok",222:"Rahul",333:"Mohan"}
    pickle.dump(list1,f1)
    pickle.dump(dict1,f1)
    f1.close()
    f2=open("myfile.dat","rb")
    value1=pickle.load(f2)
    value2=pickle.load(f2)
    print(value1)
    print(value2)

except IOError:
    print("Error in opening the file.")







































