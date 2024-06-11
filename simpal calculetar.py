print("simpal calculater")
num1 =  float(input("enter first num:"))
num2 = float(input("enter second num:"))
print ("press 1 for addition \npress 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division ")
 
choice = int(input("entre your choice from 1-4: "))
if choice == 1:
    print (num1 + num2)
if choice == 2:
    print (num1 - num2)
if choice == 3:
    print (num1 * num2)
if choice == 4:
    print (num1 % num2)
else:
    print ("invalid choice")
