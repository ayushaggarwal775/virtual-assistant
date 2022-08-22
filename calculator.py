from math import sin , cos , tan , log , pi,acos,asin,atan

def opr(a,b,c):
    if(c == '+'):
        return a+b
    elif(c=='-'):
        return a-b
    elif(c=='*'):
        return a*b
    elif(c=='/'):
        return a/b
    elif(c=='^'):
        return a**b
    else:
        print("operator not defined")


def sci(t):


    t = ''.join(t)
    #print(t)
    #print('inside sci function ',t)
    if(t[:3]=='sin'):
        return sin(int(t[3:])*(pi/180))
    elif(t[:3]=='cos'):
        return cos(int(t[3:])*(pi/180))
    elif(t[:3]=='tan'):
        return tan(int(t[3:])*(pi/180))
    elif(t[:3]=='log'):
        return log(int(t[3:]))

    elif(t[:5]=='cosec' ):
        return asin(int(t[5:])*(pi/180))
    elif(t[:3]=='sec' ):
        return acos(int(t[3:])*(pi/180))
    elif(t[:3]=='cot' ):
        return atan(int(t[3:])*(pi/180))

    else:
        print('error')

def check(t):

    if(t[:3]=='sin'):
        return sin(int(t[3:])*(pi/180))
    elif(t[:3]=='cos'):
        return cos(int(t[3:])*(pi/180))
    elif(t[:3]=='tan'):
        return tan(int(t[3:])*(pi/180))

    elif(t[:3]=='log'):
        return log(int(t[3:]))

    elif(t[:3]=='asin' or t[:3]=='cosec' or t[:3]=='asine'):
        return asin(int(t[3:])*(pi/180))
    elif(t[:3]=='sec' or t[:3]=='acos'):
        return acos(int(t[3:])*(pi/180))
    elif(t[:3]=='cot' or t[:3]=='atan'):
        return atan(int(t[3 :])*(pi/180))


    else:
        return t

#entry point
def calculate(ar):
    print(''' \nenter expression
for trignometric functition enter like sin45 etc\n''')
    ar = ar.split()

    for i in range(len(ar)):
        if(ar[i]=='minus' or ar[i]=='subtract'):
            ar[i] = '-'
        elif(ar[i]=='multiply'):
            ar[i]='*'
        elif(ar[i]=='divide'):
            ar[i]='/'
        elif(ar[i]=='plus'):
            ar[i]= '+'


    if(len(ar)<=2):

        re = sci(ar)
        return round(re,4)

    temp = ar.copy()
    for i in range(len(ar)):
        temp[i] = check(temp[i])

    result = temp[0]

    for i in range(len(temp)//2):

        result = opr(int(result),int(temp[2*i+2]),temp[2*i+1])

    return result
    #print("\ndo you want to continue(y/n):")
    #condition = input()
    
print("inside calculator")
