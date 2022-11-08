import re
hand = open('sample.txt')

tot=0
for line in hand:
  line = line.rstrip()
  
  x = re.findall('([0-9]+)', line)
  if len(x) > 0: 
    #print(x)
    for num in x:
      tot += int(num)
      #print(tot)
print(tot)