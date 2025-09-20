class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0 , len(height)-1
        current_area = 0
        area = 0

        while i < j:
            current_area = (j-i) * min(height[i],height[j])
            area = max(current_area, area)
            
            if height[i] <= height[j]:
                i += 1
            
            else:
                j -= 1

        return area

        