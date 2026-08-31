class Solution:

  def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    min_dist = float('inf')
    max_dist = -1
    first_idx = -1
    prev_idx = -1
    curr_idx = 1

    prev_node = head
    curr_node = head.next

    while curr_node and curr_node.next:
      next_node = curr_node.next

      # Check for local maxima or local minima
      if (
          curr_node.val > prev_node.val
          and curr_node.val > next_node.val
      ) or (
          curr_node.val < prev_node.val
          and curr_node.val < next_node.val
      ):
        if first_idx == -1:
          first_idx = curr_idx
        else:
          min_dist = min(min_dist, curr_idx - prev_idx)
          max_dist = curr_idx - first_idx

        prev_idx = curr_idx

      prev_node = curr_node
      curr_node = next_node
      curr_idx += 1

    if min_dist == float('inf'):
      return [-1, -1]

    return [min_dist, max_dist]
