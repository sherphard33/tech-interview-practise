import ast
from pprint import pprint

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

print(find_value_of(src2, 'str'))