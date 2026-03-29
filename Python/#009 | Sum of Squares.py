#19-08-2025 | 29-03-2026 

'''
    Given: N int.
    Problem: Return the sum of squared value from 1 to N
'''


def sum_of_squares(n):
    if not isinstance(n, int):
        return "Enter int"
    
    total = 0
    for i in range(1,n+1):
        total += i * i
    
    return total
 
def test_cases():
    print(sum_of_squares(5))    # 55
    print(sum_of_squares(10))   # 385
    print(sum_of_squares(25))   # 5525
    print(sum_of_squares(500))  # 41791750
    print(sum_of_squares(1000)) # 333833500
    print(sum_of_squares(2410)) # 4668744785
  
if __name__ == "__main__":
    test_cases()
