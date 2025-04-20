from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 🧠 The inner recursive brain of the operation — it calculates the minimum jumps from any index
        def getMinJumpsRequired(currentIndex: int = 0) -> int:
            # 🎯 Base Case: If we've reached or gone past the last index, we chill. No more jumps needed.
            if currentIndex >= len(nums) - 1: 
                return 0

            # 🏆 Start with a hilariously large number because we believe in disappointment.
            minJumpsRequired = 10_000_000  # Because infinity was too mainstream.

            # 🕺 Try every possible move from current index. Dance through the jump options.
            for steps in range(1, nums[currentIndex] + 1):
                # 🧗 Recursively try jumping `steps` ahead and count how many jumps it takes to win.
                currentJumpsRequired = 1 + getMinJumpsRequired(currentIndex + steps)
                # 🧐 Keep the jump count with the least regret.
                minJumpsRequired = min(minJumpsRequired, currentJumpsRequired)

            # 🤕 Return the minimum pain it took from this path
            return minJumpsRequired
        
        # 🎬 Kick off our JumpQuest™️ from index 0
        return getMinJumpsRequired()