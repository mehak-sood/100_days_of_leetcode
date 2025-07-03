
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Pointer to the last valid element in nums1
        p1 = m - 1  
        # Pointer to the last element in nums2
        p2 = n - 1  

        # Fill nums1 from the end (backward)
        for p in range(n + m - 1, -1, -1):  
            # If all elements in nums2 are merged, we are done
            if p2 < 0:  
                break
            # If nums1[p1] is greater, place it at current position
            if p1 >= 0 and nums1[p1] > nums2[p2]:  
                nums1[p] = nums1[p1]
                p1 -= 1
            else:  
                # Else place nums2[p2] at current position
                nums1[p] = nums2[p2]
                p2 -= 1  
