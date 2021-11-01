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
  bubble docstring
  '''

  for i in range(len(int_list)):
    for j in range(0, len(int_list) - i - 1):
      if int_list[j] > int_list[j+1]:
        tmp = int_list[j]
        int_list[j] = int_list[j+1]
        int_list[j+1] = tmp

  
def quick(int_list):
  '''
  qsort docstring
  '''
  pass
  
        
  
def insertion(int_list):
  '''
  insertion docstring
  '''
  
  for i in range(1, len(int_list)):
      val = int_list[i]

      j = i - 1
      while j >= 0 and val < int_list[j]:
              int_list[j+1] = int_list[j]
              j -= 1
      int_list[j+1] = val
