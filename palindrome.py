import os
os.system("clear")
a=input("Enter a string: ")
if(a==a[::-1]):
      print(f"{a} is a palindrome")
else:
      print("Entered input is not a palindrome")
