from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 🧠 Memory palace for our recursion — stores min jumps required from each index
        # -1 means "I haven't thought that far ahead yet"
        minJumpsRequiredForEachIndex = [-1] * len(nums)

        # 🧠 The inner recursive brain of the operation — calculates the min jumps from a given index
        def getMinJumpsRequired(currentIndex: int = 0) -> int:
            # 🎯 Base Case: If we’ve made it to or past the last index, we’re home. No more jumps. Feet up.
            if currentIndex >= len(nums) - 1: 
                return 0
            
            # 🧐 Haven’t computed from here yet? Time to think...
            if minJumpsRequiredForEachIndex[currentIndex] == -1:
                # 🏆 Start with a hilariously large number — aka “Infinity Lite™️”
                minJumpsRequired = 10_000_000  

                # 💃 From here, try all possible jumps we’re allowed to make
                for steps in range(1, nums[currentIndex] + 1):
                    # 🧗 Recursively explore every jump path like we’re on a hike with no map
                    currentJumpsRequired = 1 + getMinJumpsRequired(currentIndex + steps)
                    
                    # 😩 Only keep the jump count that doesn’t make us want to cry
                    minJumpsRequired = min(minJumpsRequired, currentJumpsRequired)

                # 📝 Memoize it — so we never have to suffer this path again
                minJumpsRequiredForEachIndex[currentIndex] = minJumpsRequired

            # 🧾 Return the best (least painful) path from here
            return minJumpsRequiredForEachIndex[currentIndex]
        
        # 🎬 Lights, camera, recursion! Let the JumpQuest™️ begin at index 0
        return getMinJumpsRequired()