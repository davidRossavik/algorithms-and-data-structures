"""
lcs.py
-------
Implementation of LCS (Longest Common Subsequence) in Python.
The method follows a dynamic programming solution. 
BOTTOM-UP (Iterative) version!!!

The main idea:
    1. Intializes two new two-dimentionals arrays 
        - one for storing length of subsequence (set the first row and column to zero)
        - and one for choices made
    2. For every cell:
        - Check if letter is equal (if so add 1 to the value diagonally up to the left) (retrieve the optimal solution for the previous two letters)
        - If not equal (bring the most optimal solution for sequences either up or to the left) (previous longest sequences)
        - Store every choice made at the indexes

Time Complexity:
    - lcs_length(): O(m*n) (two nested for-loops with length of both sequences)
    - print_lcs(): O(m + n) (cannot be more or less than m + n because at each step you take a step at either m or n. You need to take both) 
    - Combined: O(m*n)


Space Complexity:
    - lcs_length(): 2*O(m*n) = O(m*n) (creates two two-dim tables)
    - print_lcs(): O(m+n) (recursion uses a callstack with depth m+n)
    - Combined: O(m*n)

Author: David
Date: 13-10-2025
"""

def lcs_length(sequence1, sequence2):
    # Arrange two list as tables
    m, n = len(sequence1), len(sequence2)
    lengthTable = [[0]*(n+1) for _ in range(m+1)]
    decisionTable = [[0]*(n+1) for _ in range(m+1)]

    # Iterate through every cell
    for i in range(1, m+1):
        for j in range(1, n+1):

            # If we have the same letter add to the previous optimal length
            if sequence1[i-1] == sequence2[j-1]:
                lengthTable[i][j] = lengthTable[i-1][j-1] + 1
                decisionTable[i][j] = "↖"
            
            #If we dont, then take the max of either choice take away from s1 og take away from s2
            elif lengthTable[i-1][j] >= lengthTable[i][j-1]:
                lengthTable[i][j] = lengthTable[i-1][j]
                decisionTable[i][j] = "↑"
            else:
                lengthTable[i][j] = lengthTable[i][j-1]
                decisionTable[i][j] = "←"
    
    return lengthTable, decisionTable

"""
PRINT-LCS
----------
Function that follows the arrows from the bottom right to top left. 
Uses recursion to ask for the previous letter in the sequence until it meets the base case.
Then it appends every letter back in the correct order.
"""

def print_lcs(decisionTable, sequence1, i, j):
    # Base case - Top left (one of the strings empty)
    if i == 0 or j == 0:
        return ""
    
    # Same letter, we traverse diagonally and adds the letter (after the recursion has returned)
    if decisionTable[i][j] == "↖":
        return print_lcs(decisionTable, sequence1, i-1, j-1) + sequence1[i-1]
    
    # Traverse upwards, we "skip" the letter X[i-1] because it doesnt contribute to the common sequence
    elif decisionTable[i][j] == "↑":
        return print_lcs(decisionTable, sequence1, i-1, j)
    
    # Traverse to the left, we "skip" the letter Y[j-1] because it doesnt contribute to the lcs
    else:
        return print_lcs(decisionTable, sequence1, i, j-1)
    

if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    c, b = lcs_length(X, Y)
    result = print_lcs(b, X, len(X), len(Y))
    print("LCS-length:", c[len(X)][len(Y)])
    print("LCS:", result)