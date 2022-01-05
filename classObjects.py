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
    
    for i in range(n):
        st[i].display()  



'''s1=student(111,'Prahen',39)         ##here object s1 is pased as argument implicitly to the constucter of class
s2=student(112,'Priyanshu', 69)   
s1.display()
s2.display()
'''
