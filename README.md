# [🎮✨ Jump Game II — But Make It a Quest 🏃‍♂️💥](https://leetcode.com/problems/jump-game-ii?envType=study-plan-v2&envId=top-interview-150)

**Difficulty:** Medium 🧠💪 <br>
**Topics Covered:** Array 🧮, Dynamic Programming ♻️, Greedy 💰
<hr>

You are given a 0-indexed array of integers $\textbf{nums}$ of length $\textbf{n}$.  
You start your journey standing bravely at `nums[0]` — your launchpad to greatness 🚀.

Each element `nums[i]` tells you how far you can jump forward from that spot.  
Think of it like a magical pair of sneakers at index `i` that lets you leap up to `nums[i]` steps forward 👟➡️

### 🧠 Your Mission (should you choose to accept it):

From each index `i`, you can jump to any position between `i+1` and `i + nums[i]`  
(as long as you stay within bounds, of course — no jumping into the void! 🕳️)

Your goal?  
🎯 **Reach the last index in as few jumps as humanly (or computationally) possible.**

> Because let’s be honest — no one likes unnecessary cardio. 😅

### 🎁 Return:

The **minimum number of jumps** required to reach the end of the array (a.k.a. `nums[n - 1]`).

✅ It’s guaranteed that a path to the end *always exists* — so you won’t get stranded mid-jump like a Wi-Fi drop.
<hr>

### 📌 Example:
- **Example 1:** <br>
**Input:** nums = `[2,3,1,1,4]` <br>
**Output:** 2 <br>
**Explanation:** Index 0 👣 → Index 1 🚀 → Index 4 🎯

- **Example 2:** <br>
**Input:** nums = `[2,3,0,1,4]` <br>
**Output:** 2
<hr>

### 🔒 Constraints
- $1 \leq \text{nums.length} \leq 10^4$ — Yep, you could have an array the size of a small city, no big deal! 🏙️
- $0 \leq \text{nums[i]} \leq 1000$ — Each jump is a little unpredictable, but hey, that’s the fun part, right? 🏃‍♂️💨
- It's guaranteed you can reach $\text{nums[n - 1]}$ — No worries, you won’t get stuck halfway like a bad Wi-Fi connection. You’ll get there! 🎯