import random
import sys

rand = random.randint(0, 32658)

tweets = open("TrumpTweets.txt")
words = tweets.readlines()
lst = []
for i in words:
  lst.append(i.split(" "))
if(len(sys.argv) == 1): 
	print ' '.join(lst[rand])
	
"""
i = 0
while(i < 32658):
	j = 0
	for j in lst:
		k = 0
		while(k < len(lst[rand])):
			for k in lst[rand]:
				if(lst[rand] == sys.argv[1]):
					print ' '.join(lst[rand])
					break
			rand = random.randint(0, 32658)
	i += 1
tweets.close()
"""
