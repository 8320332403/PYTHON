n=eval(input("Enter a list: "))
p=list(n)
o=[]
op=[]
oi=[]
for i in p:
    if(i%3==0):
        o.append(i)
    elif(i%5==0):
        op.append(i)
    elif(i%15==0):
        oi.append(i)

print(tuple(o))  
print(tuple(op)) 
print(tuple(oi))

        
