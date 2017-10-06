
"""
This program parses an argebraic sequence that contains integers, floats
parenthesis, and the four basic operators +,-,*,/
and returns the mathematical result
its not broadly tested

"""


import re
import math
from collections import deque
    
def main(a):
  a=parse_pows(a)
  a=parse_parentheseis(a)
  return upologise(a)

def f(a,s,b):
  """ 
  Βασικές πράξεις με δύο αριθμούς
  Τα a,b μπορεί να είναι str ή αριθμοί
  Το s μπορεί να είναι τα 4 βασικά σύμβολα 
  ή συνδυασμοί αυτών που μπορούν να αλλοιώσουν
  το αποτέλεσμα όπως --5 που γίνεται +5 
  ή *- που μας επιστρέφει τον πολλαπλασιασμό
  και το αρνητικό αποτέλεσμα κ.α.
  Επιστρέφει str του αποτελέσματος τη πράξης 
  """
  if s == '*-':
    return str(-(round(float(a) * float(b),6)))
  elif s == '/-':
    return str(-(round(float(a) / float(b),6)))
  elif s == '+' or s == '--':
    return str(round(float(a) + float(b),6))
  elif s=='-' or s == '+-':
    return str(round(float(a) - float(b),6))
  elif s=='*':
    return str(round(float(a) * float(b),6))
  elif s=='/':
    return str(round(float(a) / float(b),6))
  elif s=='**':
    return str(round(float(a) ** float(b),6))
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
    find=find.group()
    replacement=find
    replacement = replacement.strip('(')
    replacement = replacement.strip(')')
    replacement = upologise(replacement)
    a=a.replace(find,replacement)
    find=par.search(a)
  return a

def upologise (a):
  #pattern για τις πράξεις +-*/ 
  # Ψάχνω και διπλά για την περίπτωση που μετά τη αφαίρεση παρενθέσεων προκύψει *- ή /-
  symbol=re.compile(r'[\+\-\*/]{1,2}')
  args=symbol.split(a)
  # Εφόσον έχω πρόσημο ή προκύψει αυτό με την αφαίρεση παρενθέσεων
  # για τον 1ο αριθμό στην παράσταση, το split μου δίνει ένα '' ή ' ' και το μετατρέπω σε 0
  if args[0] == '' or args[0]== ' ': 
    args[0]='0'
  args=deque(args)
  symbols=symbol.findall(a) 
  symbols=deque(symbols)
  # Κάνω πρώρα τις πράξεις που έχουν προτεραιότητα */ με τη σειρά που τις συναντάω
  # από αριστερά προς τα δεξιά
  stack=[]
  stack.append(args.popleft())
  for i in range(len(symbols)):
    s=symbols.popleft()
    if s in '*/' or s=='*-' or s=='/-':
      result=f(stack.pop(),s,args.popleft())
      stack.append(result)
    else:
      stack.append(s)
      stack.append(args.popleft())
  # Κάνω τις προσθέσεις και αφαιρέσεις από αριστερά προς τα δεξιά
  stack=deque(stack)
  while len(stack)>1:
    first=stack.popleft()
    s=stack.popleft()
    second=stack.popleft()
    result=f(first,s,second)
    stack.appendleft(result)
  return stack.pop() 

def parse_pows(a):
  #pow_p=re.compile(r'pow\(([^\,]+),')
  pow_pat=re.compile(r'(pow\((\d+),(\d+)\))')
  find=pow_pat.search(a)
  while find:
    replacement=str(pow(float(find.group(2)),float(find.group(3))))
    a=a.replace(find.group(),replacement)
    find=pow_pat.search(a)
  return a
