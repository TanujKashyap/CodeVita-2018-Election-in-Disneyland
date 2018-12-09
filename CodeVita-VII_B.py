def GCD(a, b):  #functin to find GCD
    if a > b:
        s = b
    else:
        s = a
    for i in range(1, s+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd

def cal(N,SubSize,m,n):
    Acount=Bcount=Ocount=0
    for x in range(int(n/SubSize)):
        l=(x*SubSize)
        for y in range(int(m/SubSize)):
            k=(y*SubSize)
            A=[]
            for i in range(l, (l+SubSize)):
                for j in range(k, (k+SubSize)):
                    A.append(N[i][j])
            AAA=A.count(1)
            BBB=A.count(2)
            OTH=A.count(3)
            mx=max(AAA, BBB, OTH)
            if (AAA==mx):
                Acount+=1
            if (BBB==mx):
                Bcount+=1
            if (OTH==mx):
                Ocount+=1  
    mx=max(Acount, Bcount, Ocount)
    if ((Acount==mx) and (Bcount!=mx) and (Ocount!=mx)):
        return 1, Acount
    elif ((Acount!=mx) and (Bcount==mx) and (Ocount!=mx)):
        return 2, Bcount
    elif ((Acount!=mx) and (Bcount!=mx) and (Ocount==mx)):
        return 3, Ocount
    else:
        return 0,0
	
#the main program starts here...........
n, m =map(int, input().split())
N=[]
for i in range(n):
	M = list(map(int, input().split())) 
	N.append(M)
if(n==m):
    SubSize= int(n/2)
else:
    SubSize= GCD(n,m)
x,y = cal(N,SubSize,m,n)
#teh next half..........             
horseTrade =int(input())
Const=[]
for i in range(horseTrade):
      M = list(map(int, input().split()))
      Const.append(M)
      N[(Const[i][0])-1][(Const[i][1])-1] = Const[i][2]

x1,y1 = cal(N,SubSize,m,n)

if (x==1):
    print("Initial Majority Party:Seats = AAA:{}".format(y))
elif (x==2):
      print("Initial Majority Party:Seats = BBB:{}".format(y))
elif (x==3):
      print("Initial Majority Party:Seats = OTHERS:{}".format(y))
else:
      print("No Majority")

if (x1==1):
    print("Party Won Party:Seats = AAA:{}".format(y1))
elif (x1==2):
    print("Party Won Party:Seats = BBB:{}".format(y1))
elif (x1==3):
    print("Party Won Party:Seats = OTHERS:{}".format(y1))
else:
    print("No Majority") 
