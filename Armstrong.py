for num in range(1,1000):
    temp=num
    sum = 0
    while num > 0:
        r=num%10
        sum=sum+(r*r*r)
        num=num//10
    if sum==temp:
       print(temp)



