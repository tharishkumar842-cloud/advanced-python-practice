marks = {"Math": 90, "Science": 85, "English": 78, "History": 88}
highest = max(marks.values())
for k,v in marks.items():
    if v==highest:
        print(v,k)
