num=7
for i in (2,num):
    if num%i==0:
        break
if num==i:
    print("prime no :", num)
else:
    print("not prime no :",num)
print("*******************************")