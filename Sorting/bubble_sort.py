def bubble_sort(list):
    unsorted = True

    while unsorted:
        unsorted = False
        
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                unsorted = True
    
    return list
