from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")

def binary_search(array: Sequence[T], val: T) -> int | None:
  """
  Return val index in a sorted array. If not found, return None
  """
  
  if not array or val < array[0] or val > array[-1]:
    return None
    
  inf, sup = 0, len(array) - 1
  
  while inf <= sup:
    
    mid = (inf + sup) // 2

    if array[mid] == val:
      return mid
      
    if array[mid] > val:
      sup = mid - 1
    else:
      inf = mid + 1
  
  return None 
