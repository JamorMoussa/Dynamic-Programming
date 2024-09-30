
# Naive Implimentation of Grid Traveler

def grid_traveler(m, n):
    if m == 0  or n == 0: return 0
    if m == n == 1: return 1

    return grid_traveler(m-1, n) + grid_traveler(m, n-1)

# Improved Grid Traveler using Memorization

def grid_traveler(m, n, memo = {}):
    
    mn = f"{m},{n}"
    if mn in memo: return memo[mn]

    if m == 0  or n == 0: return 0
    if m == 1 and n == 1: return 1

    memo[mn] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)

    return memo[mn]


print(grid_traveler(18, 18))