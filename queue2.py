q1=[]
def enqueue():
    element=input("enter the element:")
    q1.append(element)
    print("element is added")
    print(q1)
def dequeue():
    element=q1.pop(0)
    print("removed elemnt:",element)
    print(q1)
while True:
    print("enter the choice:\n 1.add\n 2.remove\n 3.quit\n")
    choice=int(input())
    if choice==1:
       enqueue()
    elif choice==2:
       dequeue()
    elif choice==3:
       break
    else:
        print("enter the correct operation")
