'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here
#     # A First-Pass Solution

#     new_arr = arr

#     for i in arr:
#         if i == 0:
#             new_arr.append(0)
#             new_arr.remove(0)
#     return new_arr

    # Better solution
def moving_zeroes(arr):
    zero_amount = arr.count(0)
    for i in range(zero_amount):
        arr.remove(0)
        arr.append(0)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")