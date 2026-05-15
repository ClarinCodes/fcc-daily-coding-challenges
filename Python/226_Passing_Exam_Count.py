#24-03-2026 | 24-03-2026

'''
    Given: array of scores and passing score.
    Problem: count the number of students passed the exam.
'''

def passing_count(scores, passing_score):
    if scores is None or passing_score < 0:
        raise ValueError("Invalid input")
        
    count = 0
    for i in scores:
        if i >= passing_score:
            count += 1
    return count

def main():
    print(passing_count([90, 85, 75, 60, 50], 70))                       # return 3
    print(passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75))  # return 6
    print(passing_count([76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85))   # return 0

if __name__ == "__main__":
    main()
