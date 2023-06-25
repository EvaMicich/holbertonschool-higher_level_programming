#!/usr/bin/python3
"""make a pascal triangle"""

def pascal_triangle(n):
    if n <= 0:
        return []
    # Initialize a list with one list, containing only one '1'
    result = [[1]]
    for i in range(1, n):
        # Generate next row
        row = [1]
        # Add the adjusted element from the previous row
        for j in range(1, i):
            row.append(result[i-1][j-1] + result[i-1][j])
        # Append '1' at the end of each row
        row.append(1)
        # Append the row to the result
        result.append(row)
    return result
