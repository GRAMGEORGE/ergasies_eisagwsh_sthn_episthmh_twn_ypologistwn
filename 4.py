#input
stringvalue=input("give a String: ")

#number representation
printvalue=''.join(str(ord(c)) for c in stringvalue)
print("representation of the word:'",stringvalue,"' in numbers according to the representation of numbers in ASCII code")
print("number: ",printvalue)
integervalue=int(printvalue)

#check if the number is first
for i in range(2, integervalue//2):  
  if (integervalue % i) == 0: 
    print("is not a prime number") 
    break
  else: 
    print("is a prime number")
  break
