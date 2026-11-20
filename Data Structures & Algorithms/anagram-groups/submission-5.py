from collections import Counter
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups ={}
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:
                groups[key] =[]
            groups[key].append(s)
        return list(groups.values())
                    
            



soltion = Solution()
ali = soltion.groupAnagrams(["act","pots","tops","cat","stop","ali"])
print(ali)
