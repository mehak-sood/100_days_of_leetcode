### **Problem 347: Top K Frequent Elements**

# Brute Force approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency hashmap to count occurrences of each number
        freq_map = collections.defaultdict(int)
        for i in nums:
            freq_map[i] += 1

        # Convert the freq hashmap into a list of [frequency, number] pairs
        freq_list = [[value, key] for key, value in freq_map.items()]

        # Sort the list in descending order based on frequency
        sorted_list = sorted(freq_list, key=lambda x: x[0], reverse=True)

        # Collect the top k elements based on highest frequency
        ans = []
        for i in range(k):
            ans.append(sorted_list[i][1])
        
        return ans

# Heap approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_heap = []

        # Quick return if we want all elements
        if k == len(nums):
            return nums 

        # Count frequencies of each number
        count = Counter(nums)  

        for key, value in count.items():
            # Push (frequency, number) into the min-heap
            heapq.heappush(freq_heap, (value, key))
            # Keep the heap size at most k by popping the smallest frequency
            if len(freq_heap) > k:
                heapq.heappop(freq_heap)

        # Extract just the numbers from the heap
        return [key for value, key in freq_heap]
