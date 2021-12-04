class Queue:
  def __init__(self):
    self.queue=[]
  
  def addq(self,v):
    self.queue.append(v)

  def delq(self):
    v=None
    if self.queue!=[]:
      v=self.queue[0]
      self.queue=self.queue[1:]
    return v
  def empty(self):
    if self.queue==[]:
      return True
    return False

  def __str__(self):
    return(str(self.queue))

"""Q=Queue()
Q.addq(15)
Q.addq(78)
Q.addq(93)
Q.addq(25)
print(Q)
print(Q.delq())
print(Q)
print(Q.delq())
print(Q)
print(Q.delq())
print(Q)
print(Q.delq())"""