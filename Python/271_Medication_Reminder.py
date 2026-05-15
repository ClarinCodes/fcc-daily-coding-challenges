#08-05-2026 | 08-05-2026

'''
    Problem:
            Calculate the time until the next medication is due based on the current time.

    Args:
            medications (list): A list of [medication_name (str), last_taken_time (str)].
            current_time (str): Current time in "HH:MM" format.

    Return:
            str: The next medication and time remaining in the format "{name} in {H}h {M}m".
'''


def medication_reminder(medications, current_time):

    c_time = int(current_time.split(":")[0]) * 60 + int(current_time.split(":")[1])

    schedules = {
        "Deployxitrin": ["08:00", "16:00"],
        "Debuggamanizole": ["07:00", "13:00", "21:00"]
        }

    interval = { "Mergeflictamine": 4 * 60 }

    min_gap = float("inf")
    result = ""

    for name, last_taken in medications:

        # fixed schedule
        if name in schedules:

            for t in schedules[name]:
                h, m = t.split(":")
                t_time = int(h) * 60 + int(m)

                if t_time <= c_time:
                    t_time += 24 * 60  # next day

                gap = t_time - c_time

                if gap < min_gap:
                    min_gap = gap
                    result = name

        # interval meds
        else:
            last = int(last_taken.split(":")[0]) * 60 + int(last_taken.split(":")[1])
            next_time = last + interval[name]

            while next_time <= c_time:
                next_time += interval[name]

            gap = next_time - c_time

            if gap < min_gap:
                min_gap = gap
                result = name

    return f"{result} in {min_gap // 60}h {min_gap % 60}m"



def test_cases():
    assert medication_reminder(
        [["Deployxitrin", "08:00"],
         ["Debuggamanizole", "07:00"],
         ["Mergeflictamine", "10:00"]],
        "11:00"
    ) == "Debuggamanizole in 2h 0m"

    assert medication_reminder(
        [["Deployxitrin", "08:00"],
         ["Debuggamanizole", "13:00"],
         ["Mergeflictamine", "14:00"]],
        "14:55"
    ) == "Deployxitrin in 1h 5m"

    assert medication_reminder(
        [["Deployxitrin", "08:00"],
         ["Debuggamanizole", "13:00"],
         ["Mergeflictamine", "14:00"]],
        "17:15"
    ) == "Mergeflictamine in 0h 45m"

    assert medication_reminder(
        [["Deployxitrin", "08:00"],
         ["Debuggamanizole", "07:00"],
         ["Mergeflictamine", "09:00"]],
        "12:59"
    ) == "Debuggamanizole in 0h 1m"

    assert medication_reminder(
        [["Deployxitrin", "08:00"],
         ["Debuggamanizole", "21:00"],
         ["Mergeflictamine", "03:00"]],
        "06:55"
    ) == "Debuggamanizole in 0h 5m"

    assert medication_reminder(
        [["Deployxitrin", "08:00"],
         ["Debuggamanizole", "07:00"],
         ["Mergeflictamine", "07:30"]],
        "08:00"
    ) == "Mergeflictamine in 3h 30m"


if __name__ == "__main__":
    test_cases()
    print("All tests passed!")