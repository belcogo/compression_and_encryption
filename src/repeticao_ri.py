import collections

class RRepetition:
  def __init__(self, r):
    self.r = r
  
  def encode(self, data):
    return data * self.r

  def transmit(self, data):
    result = [self.encode(char) for char in list(data)]
    return ''.join(result)
  
  def decode(self, data):
    result = ''
    dataChars = list(data)
    for k in range(0, self.r):
      step = (k * self.r)
      subArr = ''.join(dataChars[step:step + self.r])
      result += collections.Counter(subArr).most_common(1)[0][0]

    return result



