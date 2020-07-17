'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # A First-Pass Solution 
    arr.sort()

    for i in range(0, len(arr)):
        if i == 0 and arr[i] != arr[i + 1]:
            return arr[i]
        elif i == len(arr)-1 and arr[i] != arr[i - 1]:
            return arr[i]
        elif arr[i] == arr[i - 1] or arr[i] == arr[i + 1]:
            continue
        return arr[i]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# arr1 = [1, 5, 3, 6, 8, 3, 1, 6, 8, 0, 9, 9, 0]

# print(single_number(arr1))