words = {"apple": 3, "banana": 2, "orange": 5, "grape": 2}

new_words={k:v for k,v in words.items() if v>2}
print(new_words)