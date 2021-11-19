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

import pytest
import random
import sort_lib.int_sort as sort

class TestIntSort:
  def is_sorted(self, int_list):
    """
    Testing oracle.
    """
    currentHighest = 0

    print("sorted list")
    print(int_list)
                
    for i in int_list:
      if i < currentHighest:
        return False
      else:
        currentHighest = i
    return True

  def test_bubble(self, int_list):
    #Act
    assert self.is_sorted(sort.bubble(int_list))
			  
  def test_quick(self, int_list):
    #Act
    assert self.is_sorted(sort.quick(int_list, 0, len(int_list)-1))
  		
  def test_insertion(self, int_list):
    #Act
    assert self.is_sorted(sort.insertion(int_list))

#Arrange
@pytest.fixture(autouse=True)
def int_list():
  n = random.randint(10,100)
  randomList = []
  for i in range(n):
    randomList.append(random.randint(0,200))
  print(randomList)
  yield randomList
        
  #Cleanup
  del randomList

'''
Alternative cases one could test, just comment alternative variants of the
function and uncomment out these ones

#Arrange
@pytest.fixture(autouse=True)
def int_list():
        sortedList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        yield sortedList
        del sortedList

#Arrange
@pytest.fixture(autouse=True)
def int_list():
        reverseList = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
        yield reverseList
        del reverseList

#Arrange
@pytest.fixture(autouse=True)
def int_list():
        unsortedList = [1,4,2,19,17,3,18,12,16,5,20,13,15,14,6,11,7,10,9,8]
        yield unsortedList
        del unsortedList
'''




