def isEven(num): #function for checking Even
    if (num % 2) == 0:
        return True
    else: return False
def isPrime(x): #function for checking PRIME
    if (x>=2):
        for y in range(2, x):
            if (not (x%y)):
                return False
        else:
            return False
    return True
def GCD(a, b):  #functin to find GCD
    if a > b:
        s = b
    else:
        s = a
    for i in range(1, s+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd
#the main program starts here...........
n, m =map(int, input().split())
N=[]
for i in range(n):
	M = list(map(int, input().split()))
	while(len(M) > m):     #input length  verification
		del M[len(M) - 1] 
	N.append(M)
if (isEven(n) and (isEven(m))):
    if(n==m):
        SubSize= int(n/2)
    else:
        SubSize= GCD(n,m)
else:
    exit()
#here begins the operation on inputs....
Acount=0
Bcount=0
Ocount=0
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
    print("Initial Majority Party:Seats = AAA:{}".format(Acount))
elif ((Acount!=mx) and (Bcount==mx) and (Ocount!=mx)):
      print("Initial Majority Party:Seats = BBB:{}".format(Bcount))
elif ((Acount!=mx) and (Bcount!=mx) and (Ocount==mx)):
      print("Initial Majority Party:Seats = OTHERS:{}".format(Ocount))
else:
      print("No Majority")
#teh next half..........             
horseTrade =int(input())
Const=[]
for i in range(horseTrade):
      M = list(map(int, input().split()))
      Const.append(M)
for i in range(horseTrade):
      N[(Const[i][0])-1][(Const[i][1])-1] = Const[i][2]
Acount=0
Bcount=0
Ocount=0
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
    print("Party Won Party:Seats = AAA:{}".format(Acount))
elif ((Acount!=mx) and (Bcount==mx) and (Ocount!=mx)):
    print("Party Won Party:Seats = BBB:{}".format(Bcount))
elif ((Acount!=mx) and (Bcount!=mx) and (Ocount==mx)):
    print("Party Won Party:Seats = OTHERS:{}".format(Ocount))
else:
    print("No Majority")              
