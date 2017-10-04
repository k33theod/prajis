
"""
This program parses an argebraic sequence that contains integers, floats
parenthesis, and the four basic operators +,-,*,/
and returns the mathematical result
its not broadly tested

"""


import re
from collections import deque
    
def upologise(a):
  """
  Gets an arithmetic expression and return the result as a string
  """
  a=parse_parentheseis(a)#remove parenthesis
  symbol=re.compile(r'[\+\-\*/]')#pattern for +-*/
  args=symbol.split(a)#get all numbers in their order
  args=deque(args)
  symbols=symbol.findall(a) #gets praksis in their initial order
  symbols=deque(symbols)
  #Algorithm 
  stack=[]
  stack.append(args.popleft())
  for i in range(len(symbols)):
    s=symbols.popleft()
    if s in '*/':
      result=f(stack.pop(),s,args.popleft())
      stack.append(result)
    else:
      stack.append(s)
      stack.append(args.popleft())
  return parse_stack(stack)
  
def parse_stack(stack):
  """ stack is a list containing numbers and arithmetic symbols +,-
      return the result of the algebraic sequence
  """
  #algorithm
  stack=deque(stack)
  while len(stack)>1:
    first=stack.popleft()
    s=stack.popleft()
    second=stack.popleft()
    result=f(first,s,second)
    stack.appendleft(result)
  return stack.pop()

def f(a,s,b):
  """
   computes the result of operands a,b and operator s as a string
   
  """
  if s == '+':
    return str(float(a) + float(b))
  elif s=='-':
    return str(float(a) - float(b))
  elif s=='*':
    return str(float(a) * float(b))
  elif s=='/':
    return str(float(a) / float(b))
  else:
    return 'I cant support such an operation'  
    
def parse_parentheseis(a):
  """
  eliminates an algebraic sequense from parentheseis replacing them with the
  algebraic result
  returns a sequence with no parenthesis
  """
  par=re.compile(r'\([^\(\)]+\)')
  find=par.search(a)
  while find:
    find=par.search(a).group()
    replacement=find
    replacement = replacement.strip('(')
    replacement = replacement.strip(')')
    replacement = upologise(replacement)
    a=a.replace(find,replacement)
    find=par.search(a)
  return a

  
