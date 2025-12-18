# Fixed-size array
# arr =[122,........]
arr = [None] * 10

arr[0] = 20
arr[1] = 40
arr[2] = 30
arr[3] = 10

max_Size = len(arr)
end_position = 0

# calculate filled size
for i in arr:
    if i is not None:
        end_position += 1

print("Initial Array:")
print(arr)


# ---------------- INSERT BEGINNING ----------------
def insert_begining(item):
    global end_position

    if end_position == max_Size:
        print("Overflow ❌")
        return

    for i in range(end_position - 1, -1, -1):
        arr[i + 1] = arr[i]

    arr[0] = item
    end_position += 1
    print("Inserted at beginning ✅")
    print(arr)

# ---------------- INSERT END ----------------
def insert_end(item):
    global end_position

    if end_position == max_Size:
        print("Overflow ❌")
        return

    arr[end_position] = item
    end_position += 1
    print("Inserted at end ✅")
    print(arr)

# ---------------- INSERT MIDDLE ----------------
def insert_middle(item):
    global end_position

    if end_position == max_Size:
        print("Overflow ❌")
        return

    mid = end_position // 2

    for i in range(end_position - 1, mid - 1, -1):
        arr[i + 1] = arr[i]

    arr[mid] = item
    end_position += 1
    print("Inserted in middle ✅")
    print(arr)

# ---------------- INSERT DESIRED POSITION ----------------
def insert_desire(posi, item):
    global end_position

    if end_position == max_Size:
        print("Overflow ❌")
        return

    if posi < 0 or posi > end_position:
        print("Invalid Position ❌")
        return

    for i in range(end_position - 1, posi - 1, -1):
        arr[i + 1] = arr[i]

    arr[posi] = item
    end_position += 1
    print("Inserted at desired position ✅")
    print(arr)

# ---------------- DELETE BEGINNING ----------------
def delete_begining():
    global end_position

    if end_position == 0:
        print("Underflow ❌")
        return

    for i in range(0, end_position - 1):
        arr[i] = arr[i + 1]

    arr[end_position - 1] = None
    end_position -= 1
    print("Deleted from beginning ✅")
    print(arr)

# ---------------- DELETE END ----------------
def delete_end():
    global end_position

    if end_position == 0:
        print("Underflow ❌")
        return

    arr[end_position - 1] = None
    end_position -= 1
    print("Deleted from end ✅")
    print(arr)

#------------- delete_desire_position------------------
def delete_desire_position(index):
    global end_position
    if end_position ==0:
        print("UnderFlow")
        return
    if index < 0 or index >= end_position:
        print("Invalid location ❌")
        return

    for i in range(index, end_position - 1):
        arr[i] = arr[i + 1]

    arr[end_position - 1] = None
    end_position -= 1

    print("Deleted from desired position ✅")
    print(arr)
    
#------------- delete middle position------------------
def delete_middle():
    global end_position

    if end_position == -1:
        print("Underflow ❌")
        return

    mid = end_position // 2

    # shift elements to left
    for i in range(mid, end_position - 1):
        arr[i] = arr[i + 1]

    arr[end_position - 1] = None
    end_position -= 1

    print("Deleted from middle ✅")
    print(arr)

#------------- traverse array ------------------
def traverse():
    if end_position == -1:
        print("Array is empty ❌")
        return

    print("Array elements:")
    for i in range(end_position):
        print(arr[i], end=" ")
    print()

# ------------------ Linear Search -----------
def linear_Search(item):
    global end_position
    for i in range(end_position ):
        if arr[i]== item:
            print("array item  is found at index",i)
            return
    print(" your items is not fount")

# --------- Binary search------------

def binary_Search(item):
    last = 0
    high = end_position - 1

    while last <= high:
        mid = (last + high) // 2

        if arr[mid] == item:
            print("Item found at index:", mid)
            return
        elif item > arr[mid]:
            last = mid + 1
        else:
            high = mid - 1

    print("Item not found")

# -------------- bubble sort-------------
def bubble_sort():
    for i in range(end_position - 1):
        for j in range(end_position - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
            #    arr[j], arr[j + 1] = arr[j + 1], arr[j]
               temp=arr[j]
               arr[j]=arr[j+1]
               arr[j+1]=temp
            print("bubble sort", arr)

# ------------- selection sort ------------------
def selection_sort():
    for i in range(end_position - 1):
        min_index = i

        for j in range(i + 1, end_position):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap smallest with current position
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print("selection sort :", arr)
            
# ------------------- Insertion sort ------------------
def insertion_sort():
    global end_position

    for i in range(1, end_position):
        pivot = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > pivot:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = pivot   # insert pivot at correct place
        print("insertion sort", arr)
        
        
# --------------- heap sort ------------------
def heap_sort():
    global end_position

    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    for i in range(end_position // 2 - 1, -1, -1):
        heapify(end_position, i)

    for i in range(end_position - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

        print("Heap sorted array:", arr)
    
        
# ---------------- MENU ----------------
while True:
    print("\n********** MENU **********")
    print("1. Insert Beginning")
    print("2. Insert End")
    print("3. Insert Middle")
    print("4. Insert Desired Position")
    print("5. Delete Beginning")
    print("6. Delete End")
    print("7. Delete desire position")
    print("8. Delete middle position")
    print("9. Traverse Array")
    print("10. Linear search ")
    print("11. Binary search ")
    print("12. Bubble sort ")
    print("13. selection sort ")
    print("14. insertion sort ")
    print("15. Heap sort ")
    print("16. Exit")
    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            item = int(input("Enter value: "))
            insert_begining(item)

        case 2:
            item = int(input("Enter value: "))
            insert_end(item)

        case 3:
            item = int(input("Enter value: "))
            insert_middle(item)

        case 4:
            posi = int(input("Enter position: "))
            item = int(input("Enter value: "))
            insert_desire(posi, item)

        case 5:
            delete_begining()

        case 6:
            delete_end()
        case 7:
            desire_position = int(input("Enter desire position "))
            delete_desire_position(desire_position)
        case 8:
            delete_middle()
        case 9:
            traverse()
        case 10:
            item = int(input("Enter your search Item :"))
            linear_Search(item)
        case 11:
            item = int(input("Enter your search Item :"))
            binary_Search(item)
        case 12:
            bubble_sort()
        case 13:
            selection_sort()
        case 14:
            insertion_sort()
        case 15:
            heap_sort()

        case 16:
            print("Exit ✅")
            break

        case _:
            print("Invalid choice ❌")
