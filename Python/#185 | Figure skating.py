#10-02-2026 | 10-02-2026

def compute_score(judge_scores, *penalties):
  ''' to remove largest and lowest element in the judge_scores list. '''
    judge_scores.sort()
    del judge_scores[0]
    del judge_scores[-1]
    judge_scores = sum(judge_scores)
    penalties = sum(penalties)
''' subtracting the penalties from judge_scores gives the connon answer'''
    total_scores = judge_scores - penalties

    return total_scores
