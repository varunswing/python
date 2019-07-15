arr = list()
n = int(input("Enter the no. of element in array: "))
print("Enter the values of array: ")
for i in range(0, n):
    a = int(input())
    arr.append(int(a))
print("Array is: ", arr)

pos = int(input("Enter position of element to be deleted: "))
arr.remove(arr[pos-1])
print("Array after deleting is: ", arr)