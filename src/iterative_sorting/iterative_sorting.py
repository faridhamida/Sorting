# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        print(arr)
        cur_index = i
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i+1, len(arr)):
            if arr[x] < arr[cur_index]:
                cur_index = x 

        arr[i], arr[cur_index] = arr[cur_index], arr[i]




         



        # TO-DO: swap


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps_occured = True
    while swaps_occured:
        swaps_occured = False
    for i in range(len(arr)):
        print(arr)
        for x in range(i+1, len(arr)):
            if arr[x] < arr[i]:
                arr[i], arr[x] = arr[x], arr[i]
                swaps_occured = True

    return arr


# STRETCH: implement the Count Sort function below

def count_sort( arr, maximum=-1 ):


        


    return arr