marks = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 90),
    ("Alice", 88),
    ("Bob", 75),
    ("Eva", 92),
    ("Charlie", 85),
    ("David", 60)
]
new={}
for k,v in marks:
    if k in new:
        new[k]+=v
    else:
        new[k]=v

print("total scores", new)

above_average={}
total=sum(new.values())
length=len(new)
average=total/length
print("average marks",average)

for k,v in new.items():
    if v>average:
        above_average[k]=v
print("the above average students are",above_average)

highest=max(new.values())
for k,v in new.items():
    if highest==v:
        print("top student", k,v)






