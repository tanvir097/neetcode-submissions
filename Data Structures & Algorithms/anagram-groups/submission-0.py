class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang_dict = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(list(s)))
            ang_dict[sorted_s].append(s)
        
        return list(ang_dict.values())
