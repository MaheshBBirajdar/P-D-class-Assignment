# not reapeated random value(1-100)

import random
list1 = list(range(1,101))
print(list1)
random.shuffle(list1)
for each in list1:
	input("press enter to the next value")
	print(each)