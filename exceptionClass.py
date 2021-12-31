class MyException(Exception):
    def __init__(self,arg):
        self.msg=arg


def main():
    dict1={"Ashok":2000,"Rakesh":1000,"Harish":3000,"Ashu":500}
    for k,v in dict1.items():
        try:
            print("Customer Name = {} ,Balance = {}".format(k,v))
            if(v<2000):
                raise MyException("Insufficient balance of "+str(k))
        except MyException as m:
            print(m)


main()
