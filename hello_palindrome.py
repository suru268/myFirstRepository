num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    #print(dig)
    rev=rev*10+dig
    #print(rev)
    num=num//10
    #print(num)
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
