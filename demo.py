# queue implementation in python
# major oparation enque deque peek
a = []

def enquedata(a, userenque):
    a.append(userenque)

def dequedata(a):
    dequeview = a.pop(0)
    print('you dequeue value : ', dequeview)

def peekdata(a):
    viewpeek = a[0]
    print('your peek value is : ', viewpeek)

def displaydata(a):
    for x in a:
        print(x)

while True:
    userinput = int(input(
        'enque=>1 \n deque=>2 \n peek=>3 \n display=>4 \n exit=>5 \n Enter your choice : '))
    if userinput >= 1 and userinput <= 5:
       
        if userinput == 1:
            userenque = input('enter your value : ')
            enquedata(a, userenque)
        elif userinput == 2:
            if len(a) == 0:
                print('your queue is enpty')
            else:
                dequedata(a)
        elif userinput == 3:
            if len(a) == 0:
                print('your queue is enpty')
            else:
                peekdata(a)
        elif userinput == 4:
            if len(a) == 0:
                print('your queue is enpty')
            else:
                displaydata(a)
        elif userinput == 5:
            break
    else:
        print('you Enter wrong input')
        break
