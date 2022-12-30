class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.prev = None
    self.next = None

class linked_list:
  def __init__(self) -> None:
     self.head = None
    
  def create_linked_list(self, elements):
    # This will take the list of elements and add them to the linked list
    len1 = len(elements)
    i = 0
    current = self.head
    while i < len1:
      if self.head == None:
        self.head = Node(elements[i])
        current = self.head
      else:
        current.next = Node(elements[i])
        prev = current
        current = current.next
        current.prev = prev
      i+=1
      
  def print(self):
    current = self.head
    while current:
      print(current.val)
      current=current.next
