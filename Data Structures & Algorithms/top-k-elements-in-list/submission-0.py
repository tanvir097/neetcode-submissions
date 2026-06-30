class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict()

        for i in nums:
            if i in freq_dict.keys():
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1

        top_k_list = heapq.nlargest(k, freq_dict.items(), key=lambda x: x[1])
        
        top_k = []

        for i in top_k_list:
            top_k.append(i[0])
        return top_k