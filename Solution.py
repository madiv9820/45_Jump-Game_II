from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 🏃‍♂️ totalJumps: Counts how many times we’ve jumped
        # 🚀 farthestIndexCovered: The farthest index we can reach *so far*
        # 🔚 currentEnd: Marks the end of the current jump range
        totalJumps = farthestIndexCovered = currentEnd = 0
        
        # 🧭 Loop through the array — but NOT including the last index
        # Because when we reach or pass the last index, we're DONE (no jump from there)
        for currentIndex in range(len(nums) - 1):
            # 🔭 Update the farthest place we can reach from where we've been so far
            farthestIndexCovered = max(farthestIndexCovered, currentIndex + nums[currentIndex])

            # 🎯 If we've reached the end of our current jump range...
            if currentIndex == currentEnd:
                # 🛫 It's time to make a jump!
                currentEnd = farthestIndexCovered
                totalJumps += 1

        # 🎉 Return the total number of jumps we made to escape the clutches of index 0
        return totalJumps