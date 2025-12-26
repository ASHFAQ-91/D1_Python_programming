# Break & Continue statement.
for i in range(12):
    if(i == 11):
        break                           #$ break statement
    elif(i == 0 or i == 5):
        continue
    print("5 X", i, "=", 5 * (i))

print("Loop ko chodkar nikal jao, hehe")
