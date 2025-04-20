def basic_calculator():
    """
    performs an basic mathematical operations like addition,subtraction,multiplication & division
    
    (integers)->integers

    returns an result as based on condition applied

    """
    
    print("BASIC CALCULATOR")

    a=int(input("enter 1st integer:"))
    b=int(input("enter 2nd integer:"))

    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
        
    choice=input("enter your choice(1-4):")
    if choice in ['1','2','3','4']:
        if choice=='1':
            add=a+b
            print(f"the addition is",add)
        if choice=='2':
            sub=a-b
            print("the subtraction is",sub)
        if choice=='3':
            mul=a*b
            print("the multiplication is",mul)
        if choice=='4':
            div=a/b
            print("the division is",div)
    else:
        print("please input valid choice")

        
    
