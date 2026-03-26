#26-03-2026 | 26-03-2026

'''
    Given: day, showtime in str and number_of_tickets in int.
    Problem: calculate ticket price using these rules, 
                  - Weekend (Friday - Sunday): $12.00 per ticket.
                  - Weekday (Monday - Thursday): $10.00 per ticket.
                  - Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
                  - Tuesdays: all tickets are $5.00 each.
    Return: return the total cost in str foramt "$D.CC".
'''

from datetime import datetime

def get_movie_night_cost(day, showtime, number_of_tickets):
    if day == "Tuesday":
        return f"${5 * number_of_tickets:.2f}"

    weekend = ["Friday", "Saturday", "Sunday"]
    if day in weekend:
        cost = 12 * number_of_tickets
    else:
        cost = 10 * number_of_tickets


    t = datetime.strptime(showtime, "%I:%M%p")
    if (t.hour * 60 + t.minute) < (17 * 60):
        cost -= 2 * number_of_tickets

    return f"${cost:.2f}"

def test_cases():
    print(get_movie_night_cost("Saturday", "10:00pm", 1))  # "$12.00"
    print(get_movie_night_cost("Sunday", "10:00am", 1))    # "$10.00"
    print(get_movie_night_cost("Tuesday", "7:20pm", 2))    # "$10.00"
    print(get_movie_night_cost("Wednesday", "5:40pm", 3))  # "$30.00"
    print(get_movie_night_cost("Monday", "11:50am", 4))    # "$32.00"
    print(get_movie_night_cost("Friday", "4:30pm", 5))     # "$50.00"
    print(get_movie_night_cost("Tuesday", "11:30am", 1))   # "$5.00"

if __name__ == "__main__":
    test_cases()
