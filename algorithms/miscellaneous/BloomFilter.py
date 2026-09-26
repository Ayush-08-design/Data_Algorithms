# A bloon filter is a probabilistic data structure that efficiently tests whether an element
# is a member of a set

# Working
# A bloom filter uses a bitarray of size m , initially all 0's
# it uses k independent hash functions to map an element to k positions in the bitarray
# when inserting a element we set those k positions to 1
# When checking membership if all k positions are 1 the element may exists , otherwise it definitely not exist
# eg - databases , caches , network filters

import math
import bitarray
import hashlib

class BloomFilter:
    def __init__(self , size , hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)
        
    def _hashes(self , item):
        results = []
        for i in range(self.hash_count):
            digest = hashlib.sha256((item + str(i)).encode('utf-8')).hexdigest()
            index = int(digest , 16) % self.size
            results.append(index)
        return results
    
    def add(self , item):
        for index in self._hashes(item):
            self.bit_array[index] = 1
            
    def check(self , item):
        for index in self._hashes(item):
            if self.bit_array[index] == 0:
                return False
        return True
    
    
## Testing
bf = BloomFilter(size=50 , hash_count=3)

bf.add('apple')
bf.add('banana')
bf.add('cherry')

# Check Membership
print('apple in filter :' , bf.check('apple')) # Expected True
print('banana in filter :' , bf.check('banana')) # Expected True
print('grape in filter :' , bf.check('grape')) # Expected False (most likely)
