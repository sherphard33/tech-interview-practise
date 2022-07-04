import ast
import builtins
from pprint import pprint

src = """
def list(str, foo, iter): 
    def bin(set): 
        dict = 42 
        foo = zip
        bar = 0
    return str[::-1]
"""
builtin_types = tuple(getattr(builtins, t) for t in dir(builtins) if isinstance(getattr(builtins, t), type))
#print(isinstance(int, builtin_types))
#Visit Assign class to get all variables in the source
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

#Helper function to get variable in source
def getVariables(source):
    tree = ast.parse(source)
    analyzer = Analyzer()
    analyzer.visit(tree)
    return analyzer.report()

arr1 = ['str', 'bool', 'next']
arr2 = ['str', 'next']

source_assignments =  getVariables(src)
print(source_assignments)
# def cheVar(a1, a2):
#     for v in a1:
#         if v in a2:
#             print(v)
# cheVar(arr1, arr2)



