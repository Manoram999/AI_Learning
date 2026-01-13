'''a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

for ranges in range(1,11):
    print(f"{int(a)} X {ranges} = {int(a)*ranges}")

print("Some imp lines of code")
print("End of program")'''





'''a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
  for ranges in range(1,11):
    print(f"{int(a)} X {ranges} = {int(a)*ranges}")
except Exception as e:
   print(e)#e is error

print("Some imp lines of code")
print("End of program")'''




'''a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
  for ranges in range(1,11):
    print(f"{int(a)} X {ranges} = {int(a)*ranges}")
except:
   print("Invalid Input")

print("Some imp lines of code")
print("End of program") '''

'''try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")'''



try:
    num = int(input("Enter an integer: "))
    a = [6,3]
    print(a[num])

except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error") 



