def selection(array,size):
    for step in range (size):
        min_inx=step
        for i in range(step+1,size):
            #if (array[min_inx]<array[i]):
            if (array[min_inx] > array[i]): #for ascending order
                min_inx=i
        (array[step],array[min_inx])=(array[min_inx],array[step])


data = []
size = int(input("Enter the number of elements: "))
for i in range(size):
    element = input(f"Enter element {i+1}: ")
    data.append(element)

print("List:", data)

selection(data,size)
print("sorted array")
print(data)