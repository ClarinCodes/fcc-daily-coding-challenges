#10-02-2026 | 10-02-2026

def compute_score(judge_scores, *penalties):

    scores = sorted(judge_scores)
    total_scores = scores[1:-1]
#subtracting the penalties from judge_scores
    final_scores = sum(total_scores) - sum(penalties)
    
    return final_scores
