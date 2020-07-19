from itertools import combinations_with_replacement
'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # Your code here
#     # A First-Pass Solution

#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

def eating_cookies(n, cache):
    # Better solution

    if n < 0:
        return 0
    if n == 0:
        return 1

    if cache[n] > 0:
        return cache[n]

    result =  eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    cache[n] = result
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
