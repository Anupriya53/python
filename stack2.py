stack=[]
choice="y"
while (choice=="y"):
    print("1.Push")
    print("2.Pop")
    print("3.display")
    your_choice=int(input("Enter your choice:"))
    if (your_choice==1):
        num=input("Input any number:")
        stack.append(num)
    elif(your_choice==2):
        if (stack==[]):
            print("Stack is empty")
        else:
            print("The deleted element is:",stack.pop())
    elif (your_choice==3):
        l=len(stack)
        for i in range(l-1,-1,-1):
            print(stack[i])
    else:
        print("Wrong choice selected")

