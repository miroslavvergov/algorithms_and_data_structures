"""
Title: Find the Duplicate Number using Floyd's Tortoise and Hare Algorithm
Author: Miroslav Vergov
Date: 06/06/2025
Description:
    This script implements Floyd's Cycle Detection Algorithm to find the duplicate number in an array.
    The array represents a linked list where each value points to the index of the next node.
    The presence of a duplicate creates a cycle, and the algorithm detects the entry point of this cycle.
"""

def find_duplicate(nums):
    """
    Finds the duplicate number in the list nums using Floyd's Tortoise and Hare algorithm.

    Parameters:
    nums (List[int]): The input list containing n + 1 integers.

    Returns:
    int: The duplicate number.
    """
    # Phase 1: Finding the intersection point of the two runners.
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]          # Move slow pointer by 1 step
        fast = nums[nums[fast]]    # Move fast pointer by 2 steps
        if slow == fast:
            break

    # Phase 2: Finding the entrance to the cycle.
    slow = nums[0]                 # Reset slow pointer to the start
    while slow != fast:
        slow = nums[slow]          # Move both pointers by 1 step
        fast = nums[fast]
    return slow

# Example usage:
if __name__ == "__main__":
    nums = [3, 1, 3, 4, 2]
    duplicate = find_duplicate(nums)
    print(f"The duplicate number is: {duplicate}")
