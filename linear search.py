print(end="Enter the Size: ")
arrSize = int(input())
print("Enter " +str(arrSize)+ " Elements: ")
arr = []
for i in range(arrSize):
  arr.append(input())
print("Enter an Element to Search: ")
elem = input()
k = 0
index = []
for i in range(arrSize):
  if elem==arr[i]:
    index.insert(k, i)
    k = k+1
if k==0:
  print("\nElement doesn't found!")
else:
  if k==1:
    print("\nElement Found at Index Number: " + str(index[0]))
  else:
    print(end="\nElement Found at Index: ")
    indexLen = len(index)
    for i in range(indexLen):
      print(end=str(index[i])+" ")
    print()
