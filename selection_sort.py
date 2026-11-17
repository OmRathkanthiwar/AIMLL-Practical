
# SELECTION SORT
def selectionSort(arr):

    n = len(arr)

    for i in range(n):

        minIndex = i

        for j in range(i + 1, n):

            if arr[j] < arr[minIndex]:
                minIndex = j

        # SWAP MINIMUM ELEMENT
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

        print("Pass", i + 1, ":", arr)

    return arr


# INPUT ARRAY
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)


# SORT ARRAY
print("\nArray after each pass:")

sortedArray = selectionSort(arr)

# FINAL SORTED ARRAY
print("\nFinal Sorted Array:", sortedArray)
