class Node:
  def __init__(self,v=None):
    self.value=v
    self.next=None
  def isempty(self):
    if self.value==None:
      return True
    else:
      return False
  def append(self,v):
    if self.isempty():
      self.value=v
    elif self.next=None:
      self.next=Node(v)
    else:
      self.next.append(v)
    return
  def appendi(self,v):
    if self.isempty():
      self.value=v
      return
    temp=self
    while temp.next!=None:
      temp=temp.next
    if temp.next==None:
      temp.next=Node(v)
    return
  def insertBegin(self,v):
    if self.isempty():
      self.value=v
      return
    newnode=Node(v)
    self.value,newnode.value=newnode.value,self.value
    self.next,newnode.next=newnode,self.next
  return
def delete(self,v):
  if self.isempty():
    return
  if self.value==v:
    self.value=None
    if self.next!=None:
      self.value=self.next.value
      self.next=self.next.next
    else:
      if self.next!=None:
        self.next.delete(v)
        if self.next.value ==None:
          self.next=None
    return
