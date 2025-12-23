# print the particular letter from the string. & print particular word from the string Use Slice method.
mystr = "Ashfaq is a good boy"

print(mystr)

print(mystr[3])     # string index start from the 0. It means, A=0, s=1, h=2, f=3, a=4, q=5.

print("\nString length: ", len(mystr))

# BASIC SLICING
print(mystr[0:6])   # take a Slice from the string.

print(mystr[0:58])  # give the more then string size.

print("Blank Starting value: ", mystr[:20])   # by default, take Starting value 0

print("Blank Ending value: ", mystr[0:])  # by default, take Ending value till string length.

print("Blank both value: ", mystr[:])   # taking full string.

#   ADVANCE SLICING.
print("3rd / Jump value", mystr[0:20:2])    
# Print the value by jumping on the 2nd value. so, it's jumping next 2nd value.

print("Blank all value: ", mystr[::])   
# by default, 3rd value is 1. so, it's jumping next 1st value.

print("Reverse a string: ", mystr[::-1])
# -1 indicate to last letter of the string, -2 indicate to 2nd last letter of the string.