"""Input - [[1,10], [2,20]]
  Output - [[1,2], [1,20], [10,2], [10,20]]
   Input - [[1,10], [2,20], [3,30]]
  Output - [[1, 2, 3], [1, 2, 30], [1, 20, 3], [1, 20, 30], [10, 2, 3], [10, 2, 30], [10, 20, 3], [10, 20, 30]]"""

def find_unique(acc, pairs, res, curr):
  '''for any array'''
  #print('первый ', acc, res)
  for j in pairs[curr]:
    acc.append(j)
    #print('второй ',acc, res)
    if len(acc) == len(pairs):
      acc2 = []
      acc2 += acc
      res.append(acc2)
      acc.pop()
    else:
      #print('третий ',acc, res)
      find_unique(acc, pairs, res, curr+1)
      acc.pop()
      #print('четвертый ', acc, res)

def find_result(pairs):
  res = []
  find_unique([], pairs, res, 0)
  print(res)

pairs = [[1,2],[10,20],[100,200]]
find_result(pairs)

def test():
  acc = [1]
  res = []
  acc2 = []
  acc2 += acc
  res.append(acc2)
  acc.append(12321)
  print(res)

#test()

def combine(pairs):
  '''for double array'''
  out = []
  for j in range(len(pairs)): 
    elem = []
    for i in pairs[j]:
      for k in range(j+1, len(pairs)):
        for s in pairs[k]:
          out.append([i, s])
  print(out)