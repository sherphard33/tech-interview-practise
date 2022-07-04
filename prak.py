from typing import List

nums = [2,2,2,3,1,1,4,4,4,]
k = 2

def topKFreq(num: List[int], k: int) -> List[int]:
    #store occurences
    counter = {}
    #store in sorting bucket
    sBkt = [[] for _ in range(len(num) + 1)]
    #loop through the list and record occur
    for n in num:
        counter[n]  = counter.get(n, 0) + 1
    #store the n in the index == to occur
    for key, l in counter.items():
        sBkt[l].append(key)
    #inst output array
    res = []
    #print(sBkt)
    for el in range(len(sBkt) - 1, 0, -1):
        #print(el)
        for s in sBkt[el]:
            print(s)
            res.append(s)
            if len(res) == k:
                return res
  
print(topKFreq(nums, 2))