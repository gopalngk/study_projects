
def func1(var1):
    print("We are inside func1")
    print("Var1 value {}".format(var1))

def condition1(var2):
    print("We are inside condition1 function")
    if var2 > 0 :
        print("Its a positive number")
    else:
        print("Inside else function")
        print("Its negative number")

if __name__ == "__main__":
    a=10
    b=-3
    func1(a)
    condition1(b)
    condition1(a)

