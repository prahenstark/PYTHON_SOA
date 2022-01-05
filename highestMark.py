class student:
    def __init__(self,roll,name,marks):
        #self.roll=111
        self.roll=roll
        self.name=name
        self.marks=marks
    
    def display(self):
        print('Roll No = ',self.roll)
        print('Name = ',self.name)
        print('Marks = ',self.marks)


def main():
    st=[]
    n=int(input('Enter the number students : '))
    for i in range(n):
        roll=int(input('Enter roll : '))
        name=(input('Enter name : '))
        marks=float(input('Enter marks : '))
        s=student(roll,name,marks)
        st.append(s)
        maxMarks=0
        maxName=""        
        
    
    for i in range(n):
        if maxMarks<st[i].marks:
            maxMarks=st[i].marks
            maxName=st[i].name
        st[i].display()
        

    print('Highest mark =', maxMarks)
    print('Name of that student is ', maxName)
        
        
main()
