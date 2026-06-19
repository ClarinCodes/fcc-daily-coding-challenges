# 19-06-2026 | 19-06-2026

from datetime import datetime, timedelta
from math import ceil

def get_rental_cost(rented, returned, tier):
    pricing = {
        1: (4.99, 3.99),
        3: (3.99, 2.99),
        7: (2.99, 0.99),
    }

    base_cost, late_fee = pricing[tier]

    rented_dt = datetime.fromisoformat(rented.replace("Z", "+00:00"))
    returned_dt = datetime.fromisoformat(returned.replace("Z", "+00:00"))

    # Due at 12:00 PM UTC on the last rental day
    due_date = rented_dt.date() + timedelta(days=tier)
    due_dt = datetime.combine(
        due_date,
        datetime.min.time().replace(hour=12),
        tzinfo=rented_dt.tzinfo
    )

    if returned_dt <= due_dt:
        late_days = 0
    else:
        seconds_late = (returned_dt - due_dt).total_seconds()
        late_days = ceil(seconds_late / 86400)

    total = base_cost + late_days * late_fee
    return f"${total:.2f}"
