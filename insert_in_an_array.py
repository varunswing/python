arr = list()
num = int(input("Enter how many elements you want: "))
print('Enter numbers in arr: ')
for i in range(0, num):
    n = int(input())
    arr.append(int(n))
print("Array is: ", arr)

pos = int(input("Enter position of element to be inserted: ")) 
ele = int(input("Enter value of element to be inserted: ")) 
arr.insert(pos-1,ele)
print("Array after insertation is: ", arr)