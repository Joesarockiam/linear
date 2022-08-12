def sort(a):
    for i in range(len(a)):
        for j in range(i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

                
a=[]
n=int(input("Enter the total no of values:"))
for i in range(0,n):
    b=int(input("Enter elements:"))
    a.append(b)

sort(a)
print(a)

/////
def bsearch(l,x,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)/2
        mid=int(mid)
        if x==l[mid]:
            return mid
        elif x>l[mid]:
            return bsearch(l,x,mid+1,high)
        else:
            return bsearch(l,x,low,mid-1)

n=int(input("Enter number of elements in list:"))
l=[]
for i in range(n):
    a=int(input("Enter an integer value:"))
    l.append(a)

print("The list is:\n",l)
print("\n\n\nBINARY SEARCH\n")
x=int(input("Enter value to be searched:"))

result=bsearch(l,x,0,len(l)-1)

if result!=-1:
    print("Element is present at index:" + str(result))
else:
    print("Not found.")
    ////

    a=[]
key=0
n=int(input("Enter the total no of values:"))
for i in range(0,n):
    b=int(input("Enter elements:"))
    a.append(b)

print(a)

k=int(input("Enter the value to bo searched:"))

for i in range(0,n):
    if k==a[i]:
        print("Key found!")
        key+=1
        print(key)
        print("It is present in",i,"index")
else:
        print("Key not found!")
