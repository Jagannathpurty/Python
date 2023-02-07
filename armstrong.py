num=int(input())
temp=num
result=0
digits=0
while num>0:
    digits=num%10
    result+=digits**3
    num=num//10
if temp==result:
    print("It is Armstrong number")
else:
    print("It is not armstrong")    