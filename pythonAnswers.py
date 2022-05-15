# Two Number Sum
# Write a function that takes in a non-empty array of distinct intergers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no
# two numbers sum up to the targetSum , the function should return an empty array.


from numpy import integer


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
# Solution A
def sortedSquaredArray(array):
    newArray = [i**2 for i in array]
    newArray.sort()
    return newArray

# Solution B
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


# There's an algorithm tournament taking place in which teams of programmers compete againist each other to solve
# algorithmic problems as fast as possible. Temas compete in a round robin, where each team faces off aganist all other teams.
# only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other
# team is the away team.
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]
# C# beats HTML, Python beats C#, and Python beats HTML.
# HTML - 0 points
# C# - 3 points
# Python - 6 points


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

# Write a function that takes in a Binary search Tree(BST) and a target interger value and returns
# the closest value to that target value contained in the BST.
# You can assume that there will only be one closest value.
# Each BST node has an integer value, a left child node, and a right child node. A
# node is said to be a valid BST node if and only if it satisfies the BST property: its value is stricly
#


def findClosestValueInBst(tree, target):
    return helperfnct(tree, target, float("inf"))


def helperfnct(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if tree.value > target:
        return helperfnct(tree.left, target, closest)
    if tree.value < target:
        return helperfnct(tree.right, target, closest)
    else:
        return closest

# This is the class of the input tree.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
