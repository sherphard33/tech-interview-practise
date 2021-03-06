from typing import Counter, Dict, List
import ast
import builtins
from pprint import pprint
# Two Number Sum
# Write a function that takes in a non-empty array of distinct intergers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no
# two numbers sum up to the targetSum , the function should return an empty array.
arrayN = [3, 5, -4, 8, 11, 1, 0, 2]
targetSum = 10


def twoSumA(arr: List[int], tSum: int) -> List[int]:
    length = len(arr)
    for idx, n in enumerate(arr):
        for j in range(idx + 1, length):
            num2 = arr[j]
            if n + num2 == tSum:
                return [n, num2]
    return []

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def twoSumB(nums: List[int], target: int) -> List[int]:
    memo = {}
    for idx, i in enumerate(nums):
        num2 = target - i
        if num2 in memo:
            return [idx, memo[num2]]
        else:
            memo[i] = idx
    return []
# print(twoSum(arrayN, targetSum))

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up 
# to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.
def twoSumII(numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
def threeSum(nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
# Given two non empty arrays of integers, write a function that determines whether
# the second array is a subsequence of the first


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [2, 6, -1, 10]


def fSequence(arr, seq):
    sCount = 0
    for n in arr:
        if sCount == len(seq):
            return True
        if n == seq[sCount]:
            sCount += 1
    return sCount == len(seq)
# print(fSequence(array, sequence))


# Check if 2nd string is an anogram(contains the same letters in a diffrent order)
def isAnagram(s, t):
        # return Counter(s) == Counter(t) #makes the comparison in one line
        # check if they are same length first
        if len(s) != len(t):
            return False
        # create hashMaps to store number of occurance
        countS, countT = {}, {}
        # Loop through the range-length of one since they are the same length
        for idx, n in enumerate(s):
            # store number of occurece, using .Get() checks if a key already exists first
            countS[n] = 1 + countS.get(n, 0)
            # store number of occurece, using .Get() checks if a key already exists first
            countT[t[idx]] = 1 + countT.get(t[idx], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):  # compare key counts
                return False
        return True


s = 'ated'
t = 'tea'
# print(isAnagram(s, t))
# Group anagrams and return in an array


def groupAnagrams(strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            # sort the string and join letters
            sorted_string = "".join(sorted(string))
            # use one line to check if key already exists in the dic result
            result.setdefault(sorted_string, []).append(string)
            # if result.get(sorted_string):
            #     result[sorted_string].append(string)
            #     #print(result[sorted_string])
            # else:
            #     result[sorted_string] = [string]
        return [el for el in result.values()]


def checkAnog(s, t):
    return Counter(s) == Counter(t)


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams(strs = strs))


# Write a function that takes in non-empty array of intergers that are sorted in ascending order and
# returns a new array of the same length with the squares of te original intergers also sorted in ascending order.
# Solution A


def sortedSquaredArrayA(array):
    newArray = [i**2 for i in array]
    newArray.sort()
    return newArray

# Solution B


def sortedSquaredArrayB(array):
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
        
#print(sortedSquaredArrayB(array))
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    sButcket = [[] for _ in range(len(nums) + 1)]
    for i in nums:
        count[i] = 1 + count.get(i, 0)
    for key, n in count.items():
        sButcket[n].append(key)
    res = []
    print(sButcket)
    for el in range(len(sButcket) - 1, 0, -1):
        for c in sButcket[el]:
                res.append(c)
                if len(res) == k:
                    return res

# nums = [2,2,2,3,1,1,4,4,4,]
# k = 2

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        
        prefix = 1
        for i in range(N-1):
            prefix = prefix * nums[i]
            res[i+1] = prefix
        
        postfix = 1
        for i in range(N-1,-1,-1):
            res[i] *= postfix
            postfix = postfix * nums[i]
            
        return res
numz = [1,2,3,4]

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Please implement encode and decode
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
def longestConsecutive(nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

#Given a string s, find the length of the longest substring without repeating characters.
# def lengthOfLongestSubstring(s: str) -> int:
#         charSet = set()
#         sml = 0
#         total = 0
#         for i in range(len(s)):
#             while s[i] in charSet:
#                 charSet.remove(s[sml])
#                 sml += 1
#             charSet.add(s[i])
#             total = max(total, i - sml + 1)
#         return total
# Given a string s, find the length of the longest substring without repeating characters.
s = 'abcabcbb'
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

#Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
def isPalindrome(s: str):
    sml = 0
    newS = ""
    if s == "":
        return True
    for c in s:
        if c.isalnum():
            newS += c.lower()
    lrg = len(newS) - 1
    for n in range(len(newS)):
        smaV = newS[sml]
        lrgV = newS[lrg]
        print(smaV, lrgV)
        if smaV == lrgV:
            sml += 1
            lrg -= 1
        else:
            return False
        
    return True


s = "A man, a plan, a canal :Panama"
print(isPalindrome(s))
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


def update(team, scores: Dict):
    if team not in scores:
        scores[team] = 0
    scores[team] += 3

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
def maxProfit(prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res



# Write a function that takes in a Binary search Tree(BST) and a target interger value and returns
# the closest value to that target value contained in the BST.
# You can assume that there will only be one closest value.
# Each BST node has an integer value, a left child node, and a right child node. A
# node is said to be a valid BST node if and only if it satisfies the BST property: its value is stricly

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
    


# You're given two input arrays: onecontaining the heights of all the students with red shirts 
# and another one containing the heights of all the students with blue shirts. These arrays will always 
# have the same length, and each height will be a positive integer. Write a function that return weather or not
# a class photo that follows the stated guidelines can be taken. 
# Note: you can assume that each class has at least 2 students.
redShirtsHeights = [5,8,1,3,4]
blueShirtHeights = [6,9,2,4,5]

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    shirtColorInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFirstRow == 'RED':
            if redShirtHeight >= blueShirtHeight:
                return False 
        else:
            if blueShirtHeight >= redShirtHeight:
                return False
    return True


# Using AST module

src2 = """
next,dir,list,dir = 1,2,3,"bin = 4"
str = 45
"""
def find_value_of(source, target):
  mod_ast = ast.parse(source)  
  assert isinstance(mod_ast, ast.Module), type(mod_ast)
  for node in mod_ast.body:
    if isinstance(node, ast.Assign):
      if (len(node.targets) == 1 and
          isinstance(node.targets[0], ast.Name) and
          node.targets[0].id == target):
        return node.targets[0].id
  return None, None

# print(find_value_of(src2, 'str'))



src = """
def list(str, foo, iter): 
    def bin(set): 
        dict = 42 
        foo = zip
        bar = 0
    return str[::-1]
"""
builtin_types = tuple(getattr(builtins, t) for t in dir(builtins) if isinstance(getattr(builtins, t), type))
# print(isinstance(int, builtin_types))
# Visit Assign class to get all variables in the source
class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = []

    def visit_Assign(self, node):
        new_list = []
        for alias in node.targets:
            self.stats.append(alias.id)
        self.generic_visit(node)
        

    def report(self):
        return self.stats

# Helper function to get variable in source
def getVariables(source):
    tree = ast.parse(source)
    analyzer = Analyzer()
    analyzer.visit(tree)
    return analyzer.report()

arr1 = ['str', 'bool', 'next']
arr2 = ['str', 'next']

# source_assignments =  getVariables(src)
# print(source_assignments)
# def cheVar(a1, a2):
#     for v in a1:
#         if v in a2:
#             print(v)
# cheVar(arr1, arr2)

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
def isValid(s: str) -> bool:
        Map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue    
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack