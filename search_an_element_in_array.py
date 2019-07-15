arr = list()
n = int(input("Enter the no. of element in an array: "))
print("Enter the values of array: ")
for i in range(0, n):
    a = int(input())
    arr.append(int(a))
print("Array is: ", arr)
ele = int(input("Enter the element to be searched in an array: "))
for i in range(0, n):
    if(arr[i] == ele):
        print("Element found: ")