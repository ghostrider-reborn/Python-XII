def linearSearch(lst, item):
    ''' LINEAR SEARCH - search for an element by traversing through the list one by one
        and return the posititon if found, else return False '''
    
    for i in range(0, len(lst)):
        if lst[i] == item: return i+1
    
    return False

#lst = list(eval(input("Enter list as comma seperated numbers >> ")))
#item = int(input("Enter element to search >> "))
#search = linearSearch(lst, item)

#if search: print("Found element", item, "at index", search)
#else: print("Element", item, "not found")

def bubbleSort(lst):
    ''' BUBBLE SORT '''
    
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]: lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

#lst = list(eval(input('Enter comma separated numbers >> ')))
#print("Sorted:", bubbleSort(lst))

def insertElement(lst, element, pos):
    ''' Insert a given element in a given list at a given posititon '''
    
    lst += [0]      # add an element 0 at the end of the list
    index = pos-1
    
    for i in range(len(lst)-1, index, -1): lst[i] = lst[i-1]
    
    lst[index] = element
    
    return lst
        
#print(insertElement(list(eval(input("Enter comma seperated numbers (list) >> "))),
#                    int(input("Enter the element to insert >> ")),
#                    int(input("Enter the position >> "))))

def insertElementSorted(lst, element):
    ''' Insert a number in a sorted list in its correct posititon
        so that the list still remains sorted '''
    
    if element <= lst[0]: index = 0
    elif element >= lst[-1]: index = len(lst)
    else:
        for i in range(1, len(lst) - 1):
            if element >= lst[i-1] and element <= lst[i]: index = i

    return insertElement(lst, element, index + 1)
        
#print(insertElementSorted(list(eval(input("Enter sorted comma seperated numbers (list) >> "))),
#                          int(input("Enter the element to insert >> "))))

def deleteElement(lst, element):
    ''' Delete a given element from a list '''
    pos = linearSearch(lst, element)
    if not pos: return "Specified element does not exist in the given list !"
    
    for i in range(pos-1, len(lst)-1):
        lst[i] = lst[i+1]

    return lst[:-1]

#print(deleteElement(list(eval(input("Enter a list of numbers, comma-separated >> "))),
#                    int(input("Enter element if you want do delete >> "))))

def selectionSort(lst):
    ''' SELECTION SORT '''
    for i in range(len(lst)):
        smallest = i
        for j in range(i+1, len(lst)):
            if lst[j] <= lst[smallest]: smallest = j
        
        lst[i], lst[smallest] = lst[smallest], lst[i]

    return lst

#print("Sorted:", selectionSort(list(eval(input('Enter comma separated numbers >> ')))))

def swapHalfList(lst):
    ''' Swap half parts of a given list containing even number of elements '''
    assert len(lst) % 2 == 0, "List should have even number of elements!"
    for i in range(len(lst)//2):
        lst[i], lst[len(lst)//2 + i] = lst[len(lst)//2 + i], lst[i]
    return lst

print(swapHalfList([1,2,3,4,5,6,7]))
