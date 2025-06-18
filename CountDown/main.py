import datetime, birthday

today=datetime.date.today()
next_birthday=datetime.date(2026, 5,16)
days_away=next_birthday-today
if today == next_birthday:
    print(birthday.random_message)
else:
    print(f"My next birthday is {days_away.days} days away!")
