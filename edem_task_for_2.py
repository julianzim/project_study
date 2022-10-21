"""Input - [[1,10], [2,20]]
  Output - [[1,2], [1,20], [10,2], [10,20]]"""

input_ = [[1,10],[2,20]]

def combine(pairs):
    return [[a, b] for a in input_[0] for b in input_[1]]

print(combine(input_))