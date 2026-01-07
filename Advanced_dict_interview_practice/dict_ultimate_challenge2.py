data = {
    "Alice": [80, 90, 75],
    "Bob": [70, 85],
    "Charlie": [95, 88, 92],
    "David": []
}
avg_score={}
for k,v in data.items():
    if not v: # skips empty list
        continue
    avg_score[k]=sum(v)/len(v)

print("Average score is",avg_score)

above_85={k:v for k,v in avg_score.items() if v>=85}
print("Students with the above average  marks is",above_85)

highest=max(avg_score.values())
for k,v in avg_score.items():
    if highest==v:
        print("top student", k,v)



