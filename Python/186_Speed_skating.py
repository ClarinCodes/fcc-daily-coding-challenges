#12-02-2026 | 14-02-2026

'''given: two arrays (skater1 and skater2), their lap time
  problem: compare the skaters time to find the maximum gap between them
  return: the position of max gap
  example: largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23]) 
            should return 1.'''


def largest_difference(skater1, skater2):
    #abs - always make +ve values (3-5=2 instead of -2)
    diff = [abs(skater1[i]-skater2[i]) for i in range(len(skater1))]
    max_diff = max(diff)
    # (not index,so index+1)
    gap_diff = diff.index(max_diff)+1

    return gap_diff
