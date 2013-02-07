import numpy as np
import heap
#import heap_original as heap
import time

# Make a initial heap
data = np.sort(np.random.rand(100000))

sTime = time.time()

# Do some processing
for i in range(100000):
	data[0] += 0.1*np.random.rand()
	#heap.siftup(data,0)

eTime = time.time()
print "Took: %1.2f seconds" % (eTime-sTime)