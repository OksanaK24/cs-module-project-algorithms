'''
Input: a List of integers
Returns: a List of integers
'''
# def product_of_all_other_numbers(arr):
#     # Your code here
#     # A First-Pass Solution
#     new_arr = []
#     for i in range(0, len(arr)):
#         result = 1
#         for j in range(0, len(arr)):
#             if i != j:
#                 result = result * arr[j]
#             else:
#                 continue
#         new_arr.insert(i, result)
#     return new_arr

# Better solution? => not sure about time complexity
import math 
def product_of_all_other_numbers(arr):
    new_arr = []
    for i in range (0, len(arr)):
        if i == 0:
            new_arr.insert(i, math.prod(arr[i+1:]))
        elif i == len(arr) - 1:
            new_arr.insert(i, math.prod(arr[:i]))
        else:
            new_arr.insert(i, math.prod(arr[:i]) * math.prod(arr[i+1:]))
    return new_arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
