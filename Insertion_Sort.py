def Insertion_Sort(list):
    for j in range(len(list)-1, -1, -1):
        value = list[j]
        hole = j
        while hole < (len(list)-1) and list[hole+1] > list[hole]:
            list[hole] = list[hole+1]
            hole = hole+1
            list[hole] = value
        print(list)


list = [9, 11, 2, 10, 1, 7, 3, 4, 8]
print("Data yang akan di sort", list)
print("Insertion Sort :")
Insertion_Sort(list)
