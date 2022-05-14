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

# Given two non empty arrays of integers, write a function that determines whether
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
            idx += 1
    return idx == len(seq)


print(fSequence(array, sequence))


# Write a function that takes in non-empty array of intergers that are sorted in ascending order and
# returns a new array of the same length with the squares of te original intergers also sorted in ascending order.

def sortedSquaredArray(array):
    sqrs = [0 for _ in array]
    sml = 0
    lrg = len(array) - 1
    for idx in range(len(array))[::-1]:
        smlV = array[sml]
        lrgV = array[lrg]
        if abs(smlV) > abs(lrgV):
            sqrs[idx] = smlV**2
            sml += 1
        else:
            sqrs[idx] = lrgV**2
            lrg -= 1
    return sqrs


def tournamentWinner(competitions, results):
    cBestTeam = ""
    scores = {cBestTeam: 0}
    for indx, comp in enumerate(competitions):
        result = results[indx]
        homeTeam, awayTeam = comp
        winnerT = homeTeam if result == 1 else awayTeam
        update(winnerT, scores)
        if scores[winnerT] > scores[cBestTeam]:
            cBestTeam = winnerT
    return cBestTeam


def update(team, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += 3
