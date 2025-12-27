# Conditional Statement.
# 1. if
# 2. if-else
# 3. if-else-elif
# 4. nested if-else-elif

#$ nested-if-else
grocery = ["Cadbury", "Dora-cake", 7, 91.2, True]
if 7 in grocery:
    print("Yes, 7 is present")
    if "AS" in "MASQ":
        print("YES, AS is Pesent")


#$ if-else
print("*****Car Eligibility*****".center(40))
age = int(input("Enter your Age: "))

if(age>17):
    print("You can Drive.")
else:
    print("You can't Drive.")


#$ if-else-elif
print("*****Check Greater Value*****".center(40))
var1 = 5
var2 = 10
if var1 > var2:
    print("Lesser")
elif var1 == var2:
    print("Equal")
else:
    print("Greater")