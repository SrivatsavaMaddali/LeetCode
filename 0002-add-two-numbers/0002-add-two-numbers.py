class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the result linked list with a dummy head node
        dummy = ListNode()
        result = dummy
        # Initialize the carry to 0
        carry = 0
        
        while l1 or l2 or carry:
            # Compute the sum of the current digits and the carry
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            # Compute the carry for the next digit
            carry = sum // 10
            # Compute the value of the current digit
            value = sum % 10
            # Create a new node for the current digit and append it to the result linked list
            result.next = ListNode(value)
            result = result.next
            # Move to the next digits in the input linked lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the result linked list, excluding the dummy head node
        return dummy.next
