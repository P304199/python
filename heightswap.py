no=int(input("number of people : "))
L=[]
for i in range(no):
    h=int(input(" height of the person : "))
    L.append(h)
swap=0
print("\n")
print("Entered height order is : ")
for i in range(no) :
    print(L[i])
print("\n")
for i in range(no):
    mini=i
    for j in range(i+1,no) :
        if L[j]<L[mini] :
            mini=j
    if mini != i :
        L[i],L[mini]=L[mini],L[i]
        swap+=1
print("The sorted height order is : ")
for i in range(no) :
    print(L[i])
print("\nNo of minimum swaps : ",swap,sep="\n")