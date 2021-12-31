import sys

def compute(file1,file2,per):
    try:
        f1=open(file1,'r')
        f2=open(file2,'w')
    except IOError:
        print("Problem in opening the file.")
        sys.exit()
        
    line1=f1.readline()
    while(line1!=""):
        slist=line1.split(",")
        
        try:
            roll=int(slist[0])
            names=slist[1]
            marks=float(slist[2])
        except IndexError:
            print("Undefined index")
            sys.exit()
        except ValueError:
            print("Unsuccessful conversion")
            sys.exit()
            
        maxmarks=100
        moderatedmarks=marks+((per*maxmarks)/100)
        if(moderatedmarks>100):
            moderatedmarks=100
        f2.write(str(roll)+","+names+","+str(moderatedmarks)+"\n")
        line1=f1.readline()
    f2.close()
    f1.close()


        
    '''f1=open(file1,"wb")
    list1=[111,"Ashok",47]
    list2=[222,"Rakesh",58]
    list3=[333,"Rahhul",63]
    pickle.dump(list1,f1)
    pickle.dump(list2,f1)
    pickle.dump(list3,f1)
    f1.close()
    file2=open(file2,"rb")
    '''
        


def main():
    file1=input("Enter the name of the input file contaning the mark : \n")
    file2=input("Enter the name of the output file to store the mark : \n")
    per=int(input("Enter the  moderation percentage : \n"))
    compute(file1,file2,per)

if(__name__=="__main__"):
    main()































