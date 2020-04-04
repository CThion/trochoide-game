# ==============================================================================
"""SQUARES : print the sequence of square numbers from 1*1 to n*n"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # use list comprehension then join into multi-line string
__date__    = "2018-01-15"
__usage__   = """
User input: <n> (where n:int > 0)
App output: sequence of square numbers from 1*1 to n*n"""
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
def square(n):
  """return the square of 'n'"""
  return n*n
# ------------------------------------------------------------------------------
def squares(n):
  """return a string containing the 'n' first square numbers"""
  lines = [f"{p} * {p} = {square(p)}" for p in range(1,n+1)]; #inspect()
  return '\n'.join(lines) # join all lines into a single multi-line string
# ------------------------------------------------------------------------------
def parser(command):
  """parse 'command' as integer 'n' before calling 'squares(n)'"""
  n = parse(command); #inspect()
  assert type(n) is int and n > 0, "<n> must be a strictly positive integer"
  return squares(n)
# ==============================================================================
if __name__ == '__main__':
  userloop(parser, "Enter value for <n>")
# ==============================================================================