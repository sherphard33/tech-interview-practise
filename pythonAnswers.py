# Two Number Sum
# Write a function that takes in a non-empty array of distinct intergers and an integer representing a target sum. 
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no
# two numbers sum up to the targetSum , the function should return an empty array.



array = [3, 5, -4, 8, 11, 1, 0, 2]
targetSum = 10

def tSumNum(arr, tSum):
    length = len(arr)
    for n in range(length):
        num1 = arr[n]
        for j in range(num1 + 1, length):
            num2 = arr[j]
            if num1 + num2 == tSum:
                return [num1, num2]
    return []

print(tSumNum(array, targetSum))

#Given two non empty arrays of integers, write a function that determines whether 
# the second array is a subsequence of the first

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def fSequence(arr, seq):
    idx = 0
    length = len(arr)
    for i in arr:
        if idx == len(seq):
            return True
        if i == seq[idx]:
            idx +=1
    return idx == len(seq)



print(fSequence(array, sequence))