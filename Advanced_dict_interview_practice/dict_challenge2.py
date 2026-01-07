marks = {"A": 70, "B": 85, "C": 90, "D": 60}
highest_mark=max(marks.values())
for k,v in marks.items():
    if highest_mark==v:
        print(k,v)

