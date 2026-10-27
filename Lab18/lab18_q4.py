test_dict = {
    "Gfg": [5, 7, 7, 7, 7],
    "is": [6, 7, 7, 7],
    "Best": [9, 9, 6, 5, 5]
}

max_key = ""
max_count = 0

for key in test_dict:
    count = len(set(test_dict[key]))

    if count > max_count:
        max_count = count
        max_key = key

print(max_key)