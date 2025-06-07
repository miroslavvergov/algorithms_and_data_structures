"""
Title: Detect a cycle in a Linked List using Floyd's Tortoise and Hare Algorithm
Author: Miroslav Vergov
Date: 06/06/2025
Description:
    This script implements Floyd's Cycle Detection Algorithm to find a node cycle in a Linked List.
"""
class Node:
    """
    A simple singly-linked list node.
    """
    __slots__ = ('val', 'next')

    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    """
    Phase 1: Detects a cycle using two pointers.
    Returns the meeting node inside the loop if a cycle exists, else None.
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next          # move by 1 step
        fast = fast.next.next     # move by 2 steps
        if slow is fast:
            return slow
    return None

def find_cycle_start(head, meeting_node):
    """
    Phase 2: Finds the entry point of the cycle.
    Reset one pointer to head and move both at speed 1; their meeting point is the cycle start.
    """
    ptr1 = head
    ptr2 = meeting_node
    while ptr1 is not ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1

def cycle_length(meeting_node):
    """
    Phase 3: Computes the length of the cycle.
    Walk around the loop until you return to the meeting node.
    """
    current = meeting_node.next
    length = 1
    while current is not meeting_node:
        current = current.next
        length += 1
    return length

def floyd_cycle_detection(head):
    """
    Detects a cycle in the linked list starting at 'head'.
    Returns a tuple (start_node, length), or (None, 0) if no cycle is found.
    """
    meeting = has_cycle(head)
    if not meeting:
        return None, 0

    start = find_cycle_start(head, meeting)
    length = cycle_length(meeting)
    return start, length

# Example usage:
if __name__ == "__main__":
    # Create a list: 1 -> 2 -> 3 -> 4 -> 5
    nodes = [Node(i) for i in range(1, 6)]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    # Introduce a cycle: 5 -> 3
    nodes[-1].next = nodes[2]

    entry, size = floyd_cycle_detection(nodes[0])
    if entry:
        print(f"Cycle detected! Entry at node with value {entry.val}, length = {size}")
    else:
        print("No cycle detected.")
