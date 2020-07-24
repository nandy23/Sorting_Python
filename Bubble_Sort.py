def Bubble_Sort(list):
    iterasi = 0
    for j in range(len(list)-1):
        for i in range(len(list)-1-j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        iterasi += 1
        print(iterasi, list)


list = [9, 11, 2, 10, 1, 7, 3, 4, 8]
print('Data yang akan di sort :', list)
print('Bubble Sort :')
Bubble_Sort(list)
