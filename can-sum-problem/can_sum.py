


def canSum(taget_sum: int, numbers: list[int]):

    if taget_sum == 0: return True

    if taget_sum < 0: return False

    return any(canSum(taget_sum - num, numbers) for num in numbers)



print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))