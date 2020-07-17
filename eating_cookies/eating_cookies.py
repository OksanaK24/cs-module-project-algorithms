from itertools import combinations_with_replacement
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # A First-Pass Solution
    # all_combos =[]
    # q = [1, 2, 3]
    # for i in range(1, n + 1):
    #     for combo in combinations_with_replacement(q, i):
    #         if sum(combo) == n:
    #             all_combos.append(combo)
    # if n <= 1:
    #     return 1
    # else:
    #     print(all_combos)
    #     return len(all_combos)

    if n < 0:
        return 0
    if n == 0:
        return 1
    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
