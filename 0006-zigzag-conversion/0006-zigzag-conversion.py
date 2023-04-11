class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of empty strings for each row
        rows = ['' for _ in range(numRows)]
        
        # Initialize variables
        cur_row = 0
        going_down = False
        
        # Traverse through the string character by character
        for c in s:
            # Add the character to the current row
            rows[cur_row] += c
            
            # If we're at the top or bottom row, change direction
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down a row depending on direction
            cur_row += 1 if going_down else -1
        
        # Concatenate all rows to form the resulting zigzag pattern string
        return ''.join(rows)
