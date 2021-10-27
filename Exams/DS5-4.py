def sumOfPositiveNums(nums):
    if nums < 0:
        print("Must be positive")
        return
    if nums == 1:
        return nums
    else:
        return nums+sumOfPositiveNums(nums-1)

print(sumOfPositiveNums(-1))


def sumOfOddNums(nums):
    if nums < 0:
        print("Must be positive")
    if nums == 1:
        return nums
    else:
        return sumOfOddNums(nums-1) + (2 * nums) - 1
print(sumOfOddNums(5))