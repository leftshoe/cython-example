
from numpy import *

import numpy as np

# Operations for a max-heap. Largest element is first

def siftup(heap, pos):

    endpos = len(heap)
    startpos = pos
    
    newitem = heap[pos]
    
    # Bubble up the larger child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of the larger of the two children.
        
        rightpos = childpos + 1
        if rightpos < endpos and  heap[rightpos] > heap[childpos]:
            childpos = rightpos
            
        # Move the larger of the two children up.
        heap[pos] = heap[childpos]
        
        pos = childpos
        childpos = 2*pos + 1
    
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    
    siftdown(heap, pos)

def siftdown(heap, pos):
              
    newitem = heap[pos]
    
    ## Do a fast check to see if it needs moving
    if pos == 0:
        return
    parentpos = (pos - 1) >> 1
    if newitem < heap[parentpos]:
        return
    
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > 0:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        
        if newitem > parent:
            # Move parent down
            heap[pos] = parent
            
            pos = parentpos
        else:
            break
    
    # Place the item in its final location
    heap[pos] = newitem