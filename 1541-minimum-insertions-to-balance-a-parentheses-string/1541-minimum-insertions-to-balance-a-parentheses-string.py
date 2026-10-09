class Solution:
  def minInsertions(self, s: str) -> int:
    neededRight = 0  # Number of right parentheses needed (each '(' requires two ')' )
    missingLeft = 0  # Number of missing opening parentheses '('
    missingRight = 0  # Number of missing right parentheses ')'

    for c in s:
      if c == '(':
        # If we need an odd number of right brackets right now, 
        # we are missing one ')' to close a previous odd state.
        if neededRight % 2 == 1:
          missingRight += 1
          neededRight -= 1
        neededRight += 2
      else:  # c == ')'
        neededRight -= 1
        # If neededRight drops below 0, we have an extra ')' without an opening '('
        if neededRight < 0:
          missingLeft += 1
          neededRight += 2

    return neededRight + missingLeft + missingRight
