import sys
sys.setrecursionlimit(10000)  #needed for my implementation of memoized DP approach
#will take a few more seconds loading the tests after test #8
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

    #base cases
    if len(source) == 0:
        return len(target) * cost_insert

    if len(target) == 0:
        return len(source) * cost_delete

    #if last characters match
    if source[-1] == target[-1]:
        return naive_recursive_edit_distance(
            source[:-1], target[:-1],
            cost_insert, cost_delete, cost_sub, cost_trans
        )

    ###Transformation Operations#####
    #insert operation
    insert_cost = cost_insert + naive_recursive_edit_distance(
        source, target[:-1],
        cost_insert, cost_delete, cost_sub, cost_trans
    )

    #delete operation
    delete_cost = cost_delete + naive_recursive_edit_distance(
        source[:-1], target,
        cost_insert, cost_delete, cost_sub, cost_trans
    )

    #substitute operation
    substitute_cost = cost_sub + naive_recursive_edit_distance(
        source[:-1], target[:-1],
        cost_insert, cost_delete, cost_sub, cost_trans
    )

    min_edit_distance = min(insert_cost, delete_cost, substitute_cost)

    #transposition operation
    if (len(source) > 1 and len(target) > 1 and source[-1] == target[-2] and source[-2] == target[-1]):
        transpose_cost = cost_trans + naive_recursive_edit_distance(
            source[:-2], target[:-2],
            cost_insert, cost_delete, cost_sub, cost_trans
        )
        min_edit_distance = min(min_edit_distance, transpose_cost)

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

    m = len(source)
    n = len(target)

    #DP table for dynamic programming
    dp = [[0]*(n+1) for _ in range(m+1)]

    #base cases
    for i in range(1, m+1):
        dp[i][0] = i * cost_delete

    for j in range(1, n+1):
        dp[0][j] = j * cost_insert

    #fill DP table
    for i in range(1, m+1):
        for j in range(1, n+1):

            if source[i-1] == target[j-1]:
                cost = dp[i-1][j-1]
            else:
                cost = dp[i-1][j-1] + cost_sub  #substituion operation

            insert_cost = dp[i][j-1] + cost_insert  #insert operation
            delete_cost = dp[i-1][j] + cost_delete  #delete operation

            dp[i][j] = min(cost, insert_cost, delete_cost)

            #transposition operation
            if (i > 1 and j > 1 and source[i-1] == target[j-2] and source[i-2] == target[j-1]):
                dp[i][j] = min(dp[i][j], dp[i-2][j-2] + cost_trans)

    dp_cost = dp[m][n]
    final_string = target

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
    if memo is None:
        memo = {}

    key = (source, target)

    if key in memo:
        return memo[key]

    #base cases
    if len(source) == 0:
        result = (len(target) * cost_insert, target)
        memo[key] = result
        return result

    if len(target) == 0:
        result = (len(source) * cost_delete, "")
        memo[key] = result
        return result

    #characters match
    if source[-1] == target[-1]:
        cost, string = memoized_edit_distance(
            source[:-1], target[:-1],
            cost_insert, cost_delete, cost_sub, cost_trans, memo
        )

        result = (cost, string + source[-1])
        memo[key] = result
        return result

    #insert opetation
    insert_cost, insert_string = memoized_edit_distance(
        source, target[:-1],
        cost_insert, cost_delete, cost_sub, cost_trans, memo
    )
    insert_cost += cost_insert
    insert_string = insert_string + target[-1]

    #delete operation
    delete_cost, delete_string = memoized_edit_distance(
        source[:-1], target,
        cost_insert, cost_delete, cost_sub, cost_trans, memo
    )
    delete_cost += cost_delete

    #substitute operation
    substitute_cost, substitute_string = memoized_edit_distance(
        source[:-1], target[:-1],
        cost_insert, cost_delete, cost_sub, cost_trans, memo
    )
    substitute_cost += cost_sub
    substitute_string = substitute_string + target[-1]

    #choose best operation
    min_cost = insert_cost
    final_string = insert_string

    if delete_cost < min_cost:
        min_cost = delete_cost
        final_string = delete_string

    if substitute_cost < min_cost:
        min_cost = substitute_cost
        final_string = substitute_string

    #transposition
    if (len(source) > 1 and len(target) > 1 and source[-1] == target[-2] and source[-2] == target[-1]):
        transpose_cost, transpose_string = memoized_edit_distance(
            source[:-2], target[:-2],
            cost_insert, cost_delete, cost_sub, cost_trans, memo
        )

        transpose_cost += cost_trans
        transpose_string = transpose_string + target[-2] + target[-1]

        if transpose_cost < min_cost:
            min_cost = transpose_cost
            final_string = transpose_string

    result = (min_cost, final_string)
    memo[key] = result

    return result