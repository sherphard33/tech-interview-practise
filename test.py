from typing import List
import ast
def getVariables(source):
    root = ast.parse(source)
    #print(ast.dump(root))
    #for node in ast.walk(root):
    names = sorted({node.targets[0] for node  in root.body if isinstance(node, ast.Assign)})
    print(names.index('id'))

src = """
def fn():
    str = 42
    a, b = 1, 2
    print(str, a, b)
"""

src1 = """
def fn():
    "str = 42"
    '''next=42'''
    'bin = dir = next = list'
    next == 42
    a, b = str, list
    print(str, a, b)
"""
#expected = []
src2 = """
def fn():
    next = 42
    str = next
    a, b = tuple, list
"""
#expected = ["next", "str", "dir", "list"]
src3 = "def reverse(str): return str[::-1]"
#expected = ["str"]
src4="""
def list(str, foo, iter): 
    def bin(set): 
        dict = 42 
        foo = zip
        bar = 0
    return str[::-1]
"""
#expected = ["str", "list", "iter", "bin", "set", "dict"]

#getVariables(src1)

def findBigest(s: List[int]):
    lrg = max(s)
    print(lrg)

redShirtsHeights = [5,8,1,3,4]

#findBigest(redShirtsHeights)

def convertRoman(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = roman[s[-1]]
    for i in range(1, len(s)):
        if roman[s[i-1]] < roman[s[i]]:
                
            total -= roman[s[i-1]]
        else:
            total += roman[s[i-1]]
    return print(total)


def decode(roman):
    romanNumerals = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numericDecimal = romanNumerals[roman[-1]]
    for n in range(1, len(roman)):
        if romanNumerals[ roman[n-1]] < romanNumerals[roman[n]] :
           numericDecimal -= romanNumerals[roman[n-1]]
        else:
           numericDecimal += romanNumerals[roman[n-1]]
    return print(numericDecimal)

#convertRoman("MMVIII")



def convtString(s: str) -> List[str]:
    newList = list(s.splitlines())
    target = []
    for i in newList:
        if "=" in i:
            newI = i.lstrip()
            target.append(newI)
    return print(newList)
#convtString(src)


def missingNumber(nums: List[int]):
    nums = sorted(nums)
    for n in range(len(nums)- 1):
        if nums[n] + 1 == nums[n + 1]:
            continue
        return nums[n] + 1
arrayz = [0, 1]
print(missingNumber(arrayz))