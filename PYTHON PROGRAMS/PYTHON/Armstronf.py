u=int(input("Enter a number: "))
sum=0
while(u>0):
    r=u%10
    sum=sum+r*r*r
    u=u//10
print(sum)    

