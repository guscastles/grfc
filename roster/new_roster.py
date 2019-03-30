"""
A module for regenerating the dates for the fruit roster.
"""
from datetime import timedelta, date


START_OF_THE_SEASON = date(2019, 3, 30)
"""Start of the season date"""
HOLIDAYS = [date(2019, 4, 20)]
"""Holidays to be excluded from the roster"""


def next_date(initial_date):
    """Date generator, starting from the initial date."""
    more_days = 0
    while True:
        yield initial_date + timedelta(days=more_days)
        more_days += 7


def create_roster(data, date_generator):
    """Creates the rostes using the existing data, but reassigning the
    dates created by the date generator.
    """
    roster_days = []

    while len(roster_days) < 18:
        day = next(date_generator)
        if day not in HOLIDAYS:
            roster_days.append(day)

    new_values = list(zip(*data))[0:2] + [tuple(roster_days)]
    return list(zip(*new_values))


if __name__ == '__main__':
    import roster.roster as rt
    print(create_roster(rt.select_all_records(), next_date(START_OF_THE_SEASON)))
