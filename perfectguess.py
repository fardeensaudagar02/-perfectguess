import random

randnumber=random.randint(1,100)
print(randnumber)
user=None
nguesses=0
while (user!=randnumber):
    user=int(input("enter the number between 1 to 100\n"))
    nguesses+=1
    if user == randnumber:
        print (f"you guessed it right in {nguesses} turns")
    elif user > randnumber:
        print('Enter the smaller number')
    elif user < randnumber:
        print('Enter the larger number ')
    else:
        print('you have entered the wrong value ')