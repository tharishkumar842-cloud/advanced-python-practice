exam1 = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}
exam2 = {"Alice": 88, "Bob": 75, "Charlie": 85, "Eva": 92}

total_scores = exam1.copy()
for k,v in exam2.items():
    if k in total_scores:
        total_scores[k] +=v
    else:
        total_scores[k] = v

print("Total Scores:", total_scores)

