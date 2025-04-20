from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        # 🧠 DP array where index i tells us the *minimum* jumps needed to reach the END from i
        # Initialized with a ridiculously large number because we like dramatic tension.
        minJumpsRequiredForEachIndex = [1_000_000] * n

        # 🎯 The last index requires 0 jumps to reach the end. Because... it's already there. Congrats.
        minJumpsRequiredForEachIndex[n - 1] = 0

        # 🔁 Working backwards from second-last index to the beginning
        for currentIndex in range(n - 2, -1, -1):
            # 🏃 Try every possible jump from current index (1 to nums[currentIndex])
            for steps in range(1, nums[currentIndex] + 1):
                if currentIndex + steps <= n - 1:
                    # 🧮 Choose the path that offers minimum regret (fewer jumps)
                    minJumpsRequiredForEachIndex[currentIndex] = min(
                        minJumpsRequiredForEachIndex[currentIndex],
                        1 + minJumpsRequiredForEachIndex[currentIndex + steps]
                    )
                else:
                    # 🧱 If the jump goes out of bounds, stop. We've jumped too far into the void.
                    break

        # 🎉 Finally, the minimum jumps from index 0 to the promised land (last index)
        return minJumpsRequiredForEachIndex[0]