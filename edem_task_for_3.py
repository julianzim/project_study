"""Input - [[1,10], [2,20], [3,30]]
  Output - [[1, 2, 3], [1, 2, 30], [1, 20, 3], [1, 20, 30], [10, 2, 3], [10, 2, 30], [10, 20, 3], [10, 20, 30]]"""

input_ = [[1,10],[2,20],[3,30]]

def combine(pairs):
    print([[a, b, c] for a in pairs[0] for b in pairs[1] for c in pairs[2]])

combine(input_)