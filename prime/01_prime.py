num=int(input())
count=0
if num>1:
     for i in range(2,num):
         if(num%i==0):
             count+=1
             break
     if count==1:
        print("It is not a prime number")
     else:
        print("It is prime number")     
         