#18-02-2026 | #18-02-2026
''' to find delay time(penalty) of athletes.
    delay time is multiplied by 1.5 to get the penalty score.
    example: calculate_start_delays([120, 110, 125]) should return [8, 23, 0].
      here, 125 is the first. first - others multiplied by 1.5 to get the delay/penalty time, then rounding up '''

import math
def calculate_start_delays(jump_scores):
    first = max(jump_scores)
    jump_delay = []
    for i in range(len(jump_scores)):
        delay = (first - jump_scores[i]) * 1.5
        #the below line can be used to reduces line, but this line increase time complexity o(n)^2, because it find max in each iteration
        #delay = (max(jump_scores) - jump_scores[i]) * 1.5
        jump_delay.append(math.ceil(delay))
    return jump_delay
