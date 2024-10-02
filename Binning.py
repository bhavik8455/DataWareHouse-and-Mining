import statistics
bin   = int( input("Enter the Number of Bins : "))

count = int(input(f"Enter the length of the array in the multple of {bin} value : "))
print(count)


arr = []
binarr = []
   


print("Enter the elements in ARRAY")

for i in range(count):
    arr.append(int(input()))
    
arr.sort()
counter = 0

for i in range(bin):
    innerlist = []
    while counter <(i+1)*int(count/bin): 
         innerlist.append(arr[counter])
         counter = counter+1
       
    
    binarr.append(innerlist)



for i in binarr:
    bin1 = []
    bin2 = []
    bin3 = []

    result = statistics.mean(i)
    for k in range(0,int(count/bin)-1):
        bin1.append(result)
    
    result = statistics.median(i)
    for j in range(int(count/bin)):
        bin2.append(result)
    
    for j in range(0,int(count/bin)):
        if abs(i[j]-i[0] < abs(i[j]-i[int(count/bin)-1])):
            bin3.append(i[0])
        else:
            bin3.append(i[int(count/bin)-1])


    print("Bin : ",binarr.index(i)+1," ",i)
    print("Data Smoothing by Bin mean",bin1,
          "\nData Smoothing by Bin Median",bin2,
          "\nData Smoothing by Bin Boundries",bin3)
    
    bin1.clear()
    bin2.clear()
     

