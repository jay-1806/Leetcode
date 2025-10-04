class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        merged = []
        p1,p2 = 0, 0
        n1, n2 = len(arr1) , len(arr2)

        while p1 < n1 and p2 < n2:
            if arr1[p1] <= arr2[p2]:
                merged.append(arr1[p1])
                p1 +=1
            else:
                merged.append(arr2[p2])
                p2 +=1

        while p1 < n1:
            merged.append(arr1[p1])
            p1 += 1

        while p2 < n2:
            merged.append(arr2[p2])
            p2 += 1
        
        N = len(merged)
        
        # Index of the lower middle element
        index_lower = (N - 1) // 2
        
        # Index of the upper middle element
        index_upper = N // 2
        
        # The median is the average of the elements at these two indices.
        # This single formula works for both odd and even lengths.
        median = (merged[index_lower] + merged[index_upper]) / 2
        
        return median
        



        