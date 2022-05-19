from typing import List, Set
# Two Number Sum
# Write a function that takes in a non-empty array of distinct intergers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no
# two numbers sum up to the targetSum , the function should return an empty array.
array = [3, 5, -4, 8, 11, 1, 0, 2]
targetSum = 10


def tSumNum(arr: List[int], tSum: int) -> List[int]:
    length = len(arr)
    for n in range(length):
        num1 = arr[n]
        for j in range(num1 + 1, length):
            num2 = arr[j]
            if num1 + num2 == tSum:
                return [num1, num2]
    return []

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums: List[int], target: int) -> List[int]:
    memo = {}
    for idx, i in enumerate(nums):
        num2 = target - nums[idx]
        if num2 in memo:
            return [idx, memo[num2]]
        else:
            memo[i] = idx
    return []

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

# Write  function that takes in a Binary Tree and return a list of its branch sums Ordered
# from leftmost branch to rightmost branch sum.
# A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path
# of node in a tree that starts at the root node and ends at the leaf node.
# Each Binary-Tree node has an interger value, a left child node and a right child node.
# Children node can either be BinaryTree nodes themselves on None/Null.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []  # Branch sums array
    clcTotals(root, 0, sums)
    return sums


def clcTotals(node, running_sum, sums):  # calculate Branch Sums
    if node is None:
        return
    new_running_sum = running_sum + node.value
    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return
    clcTotals(node.left, new_running_sum, sums)
    clcTotals(node.right, new_running_sum, sums)

# Node depths
# Solution A, interative


def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOfDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Solution B, recussive


def nodeDepths(root, depth=0):
    # Handle base case of recursion
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# Depth-first Search
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstsearch(array)
        return array

# Minimum waiting waiting time
def minWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        remainingQueries = len(queries) - (idx + 1)
        totalWaitingTime += duration * remainingQueries
    return totalWaitingTime
    
#Given a string s, find the length of the longest substring without repeating characters.
def longestSubString(s: str) -> int:
    charSet = set()
    sml = 0
    total = 0
    for i in range(len(s)):
        while s[i] in charSet:
            charSet.remove(s[sml])
            sml += 1
        charSet.add(s[i])
        total = max(total, i - sml + 1)
    return total