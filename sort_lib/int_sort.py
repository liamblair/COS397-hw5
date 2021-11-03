# =========================================================================
#
#  Copyright COS 397
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

'''
This module sorts lists of integers...
'''

def bubble(int_list):
  '''
  Sort an array using Bubble Sort

  Parameters
  ----------
  int_list : list of ints
    list to be sorted
  '''

  for i in range(len(int_list)):
    for j in range(0, len(int_list) - i - 1):
      if int_list[j] > int_list[j+1]:
        tmp = int_list[j]
        int_list[j] = int_list[j+1]
        int_list[j+1] = tmp

  
def quick(int_list, start, end):
  '''
  Recursive function to sort with Quick Sort

  Parameters
  ----------
  int_list : list of ints
    list to be sorted
  start : int
    starting index
  end : int
    ending index
  '''

  if start < end:
    pivot = partition(int_list, start, end)
    quick(int_list, start, pivot-1)
    quick(int_list, pivot+1, end)
        

def partition(int_list, start, end):
  '''
  Sort the array until the pivot value

  Parameters
  ----------
  int_list : list of ints
    list to be sorted
  start : int
    starting index
  end : int
    ending index
  
  Returns
  -------
  int
    the index to partition the list around
  '''
  
  pivot = int_list[end]

  i = start - 1

  for j in range(start, end):
    if int_list[j] <= pivot:
      i = i + 1

      tmp = int_list[j]
      int_list[j] = int_list[i]
      int_list[i] = tmp
  
  tmp = int_list[i+1]
  int_list[i+1] = int_list[end]
  int_list[end] = tmp

  return i + 1

    
def insertion(int_list):
  '''
  Sort a list using Insertion Sort

  Parameters
  ----------
  int_list : list of ints
    list to be sorted
  '''
  
  for i in range(1, len(int_list)):
    val = int_list[i]

    j = i - 1
    while j >= 0 and val < int_list[j]:
      int_list[j+1] = int_list[j]
      j -= 1
    int_list[j+1] = val
