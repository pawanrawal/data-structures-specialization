# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def ShiftDown(self, i):
    minimum = i
    a = self._data

    leftChild = 2*i + 1
    if leftChild < len(a) and a[leftChild] < a[minimum]:
      minimum = leftChild

    rightChild = 2*i + 2
    if rightChild < len(a) and a[rightChild] < a[minimum]:
      minimum = rightChild

    if minimum != i:
      self._swaps.append([i,minimum])
      a[i], a[minimum] = a[minimum], a[i]
      self.ShiftDown(minimum)

  def GenerateSwaps(self):
    i = len(self._data)//2-1
    while i>=0:
      self.ShiftDown(i)
      i=i-1

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
