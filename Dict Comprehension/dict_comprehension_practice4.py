marks = {
    "Alice": 45,
    "Bob": 78,
    "Charlie": 60,
    "David": 30,
    "Eva": 90
}
new_marks={k:v for k,v in marks.items() if v>=50}
print(new_marks)