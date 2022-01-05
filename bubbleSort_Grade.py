class Student:
    ## __init is the initiallization
    def _init_(self,roll,name,marks):  
        self.roll=roll
        self.name=name
        self.marks=marks

    def display(self):
        print("Name:",self.name,"\nRoll:",self.roll,"\nMarks:",self.marks)
    
    def highest_mark(self,st):
        highest = st[0]
        for i in range(1,len(st)):
            if st[i].marks>highest.marks:
                highest=st[i]
        print(highest.name,"has secured highest mark that is ",highest.marks)

    def sorted_by_marks(self,st):
        for i in range(0,len(st)-1):
            for j in range(0,len(st)-1-i):
                if st[j].marks>st[j+1].marks:
                    st[j],st[j+1]=st[j+1],st[j]
        return st
        
def main():
    
    ## s1 = Student(1,"Jonhny Depp",100)
    ## s1.display()

    ## s2 = Student(2,"Keanu Reeves",10)
    ## s2.display()

    student_count=int(input("Enter the number of students : "))
    students = list()
    for i in range(student_count):
        roll,name,marks=int(input("Enter roll: ")),input("Enter name: "),float(input("Enter marks: "))
        students.append(Student(roll,name,marks))
        
    for i in range(student_count):
        students[i].display()
    '''
    students[0].highest_mark(students)
    students=students[0].sorted_by_marks(students)
    for i in range(student_count):
        students[i].display()
    '''
    ##grade
    for i in students:
        print(i.name,"---->",end=" ")
        if i.marks>=90:
            print('O')
        elif 80<=i.marks<90:
            print('A')
        elif 70<=i.marks<80:
            print('B')
        elif 60<=i.marks<70:
            print('C')
        elif 50<=i.marks<60:
            print('D')
        elif 40<=i.marks<50:
            print('E')
        else:
            print('F')

if _name_ == '_main_':
    main()
