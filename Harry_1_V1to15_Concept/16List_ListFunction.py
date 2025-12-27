grocery = ["Cadbury", "Dora-cake", 7, 91.2, True]
print(grocery)
print(grocery[2])       # print a particular index value

numbers = [10, 70, 30, 40, 30, 50, 60]
        #  0 ,  1,  2,  3,  4,  5,  6

numbers.sort()
print("Sorted list: ", numbers)                 #* It'll change the original list.

numbers.reverse()
print("Reverse variable list: ", numbers)       #* It'll change the original list.

print("Index value is: ", numbers.index(40))    #$ index_func, it return the index of the first occurrence of the list items.

print("Occurrence: ", numbers.count(30))        #$ count_func.


print("\nMaximum value: ", max(numbers))        #$ max_func.

print("Minimum value: ", min(numbers))          #$ min_func.


print("\nSlicing variable list: ", numbers[:])  #$ slice_func.

print("2nd Slicing variable list: ", numbers[1:6])


numbers.append(42)
print("\nAdd new value in list: ", numbers)     #$ append_func use to add new value at the END of the list.

numbers.insert(3, 69)   #$ insert_func use to add new value BTW the list. 1st value show the index position.
print("Insert new value in list: ", numbers)

numbers.remove(30)      #$ remove_func use to remove the value from the list.
print("Remove value from the list: ", numbers)

numbers.pop()           #$ pop_func remove the LAST value from the list.
print(numbers)

numbers[1] = 80         # change the value of the perticular index.
print(numbers)