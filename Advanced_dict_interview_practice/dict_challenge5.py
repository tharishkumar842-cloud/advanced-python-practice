marks = {"A": 70, "B": 85, "C": 90, "D": 60}
average = 76.25  # previous python code result
above_avg={k:v for k,v in marks.items() if v>average}

print("The students with the above average  marks is",above_avg)