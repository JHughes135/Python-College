num1_str = input("Enter the integer to be converted to Binary :")

num1_int = int(num1_str)

if num1_int < 1:
    print("Number is invalid")
else:
   print(num1_int, "in binary is", bin(num1_int)[2:].zfill(8))