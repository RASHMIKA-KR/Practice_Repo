def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Take input from the user
user_input = input("Enter a list of numbers separated by commas: ")
arr = [int(x) for x in user_input.split(',')]

# Let the user select the sorting algorithm
while True:
    choice = input("Enter '1' for Bubble Sort or '2' for Quick Sort: ")
    if choice == '1':
        sorted_arr = bubble_sort(arr.copy())
        print("Sorted array using Bubble Sort:", sorted_arr)
        break
    elif choice == '2':
        sorted_arr = quick_sort(arr.copy())
        print("Sorted array using Quick Sort:", sorted_arr)
        break
    else:
        print("Invalid choice. Please enter '1' or '2'.")
