words = ["eat","tea","tan","ate","nat","bat"]

d = {}

for word in words:
    key = "".join(sorted(word))

    if key not in d:
        d[key] = []

    d[key].append(word)

print(list(d.values()))