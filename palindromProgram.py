num = 121
temp=num
rev=0
while(temp!=0):
    dig=temp%10
    rev=(rev*10)+dig
    temp=temp//10
if num==rev:
    print("palindrom No :",num)
else:
    print("not palindrom no :",num)


print("****************************")