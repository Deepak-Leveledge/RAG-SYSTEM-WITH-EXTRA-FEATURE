import os 
from dotenv import load_dotenv
load_dotenv()
import math
import operator


OPS ={
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(expression: str) -> float:
     """
    Safely evaluate simple math expressions.
    Example: '12500 * 0.18'
    """
     
     try:
          parts = expression.split()

          if len(parts) != 3:
                raise ValueError("Invalid expression format. Use: <number> <operator> <number>")
          
          a, op, b = parts
          a = float(a)
          b = float(b)

          if op not in OPS:
            return "Unsupported operator"

          result = OPS[op](a, b)
          return str(round(result, 4))
     except Exception as e:
          raise e