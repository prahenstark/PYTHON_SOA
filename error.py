try:
    a=int(input("Enter 1st number : "))    
    b=int(input("Enter 2nd number : "))
    res=a//b
    f=open("Result.txt","w")
    f.write("Result is "+str(res))
    f1.open("myfile.txt","r")

except ZeroDivisionError:
    print("Division by 0 is not allowed.")

except TypeError as ex:
    print("Type error : ",ex)

except ValueError as v:
    print("Value error : ",v)

except NameError as n:
    print("Name error : ",n)

except Exception as e:
    print("Universal error : ",e)
    
else:
    print("Result = ",res)
    
finally:
    try:
        f.close()
        print("Welcome to third year.")
    except NameError as n:
        print("Name error : ",n)

print("Welcome to ITER. ","\ud83d")
