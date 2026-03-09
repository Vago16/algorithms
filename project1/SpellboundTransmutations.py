import sys

###############################################################################
# Naive Recursive (Divide-and-Conquer) Approach
###############################################################################
def naive_recursive_edit_distance(source, target, cost_insert, cost_delete, cost_sub, cost_trans):
    """
    Naive recursive implementation for computing the edit distance.
    (Returns only the cost.)

    Parameters:
      source (str): The source string to transform.
      target (str): The target string we want to end up with.
      cost_insert (int): The cost for performing an insertion operation.
      cost_delete (int): The cost for performing a deletion operation.
      cost_sub (int): The cost for performing a substitution operation.
      cost_trans (int): The cost for performing a transposition operation.

    Returns:
      int: The minimum edit distance (total cost) to transform `source` into `target`.
    """

    # source: the original string you want to edit
    # target: the final string you want to match
    # cost_insert: cost for adding a character
    # cost_delete: cost for removing a character
    # cost_sub: cost for replacing one character with another
    # cost_trans: cost for swapping adjacent characters

    # ... Implementation here ...
    min_edit_distance = 0  # placeholder

    return min_edit_distance


###############################################################################
# Iterative (Bottom-Up) DP Approach with Backtracking
###############################################################################
def iterative_edit_distance(source, target, cost_insert, cost_delete, cost_sub, cost_trans):
    """
    Iterative DP solution to compute the edit distance and reconstruct
    the final transformed string via backtracking.

    Parameters:
      source (str): The source string to transform.
      target (str): The target string we want to end up with.
      cost_insert (int): The cost for performing an insertion operation.
      cost_delete (int): The cost for performing a deletion operation.
      cost_sub (int): The cost for performing a substitution operation.
      cost_trans (int): The cost for performing a transposition operation.

    Returns:
      tuple of (int, str):
        - The minimum edit distance (int).
        - The final transformed string (str) obtained from backtracking,
          which should match `target` if everything is correct.
    """

    # source: the original string you want to transform
    # target: the desired string to transform into
    # cost_insert: cost for adding a character
    # cost_delete: cost for removing a character
    # cost_sub: cost for substituting one character for another
    # cost_trans: cost for transposing (swapping) two adjacent characters

    # ... Implementation here ...

    dp_cost = 0         # This would be computed from the DP table
    final_string = ""   # This would be reconstructed from backtracking

    return dp_cost, final_string


###############################################################################
# Memoized (Top-Down) DP Approach with Backtracking
###############################################################################
def memoized_edit_distance(source, target, cost_insert, cost_delete, cost_sub, cost_trans, memo=None):
    """
    Top-down DP solution with memoization that computes both the edit distance
    and reconstructs the final transformed string via backtracking.

    Parameters:
      source (str): The source string to transform.
      target (str): The target string we want to end up with.
      cost_insert (int): The cost for performing an insertion operation.
      cost_delete (int): The cost for performing a deletion operation.
      cost_sub (int): The cost for performing a substitution operation.
      cost_trans (int): The cost for performing a transposition operation.
      memo (dict, optional): A cache (memoization dictionary) used to store
        previously computed edit distances for subproblems. Defaults to None.

    Returns:
      tuple of (int, str):
        - The minimum edit distance (int).
        - The final transformed string (str) obtained through recursive
          backtracking, which should match `target`.
    """

    # source: the original string you want to edit
    # target: the final string you want
    # cost_insert: cost for adding a character
    # cost_delete: cost for removing a character
    # cost_sub: cost for substituting one character for another
    # cost_trans: cost for swapping two adjacent characters
    # memo: a dictionary to remember computed results for specific
    #       (subsource, subtarget) pairs, improving efficiency

    # ... Implementation here ...

    min_cost = 0
    final_string = ""

    return min_cost, final_string
