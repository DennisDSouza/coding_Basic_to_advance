s = "([])"

stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack.pop() != pairs[ch]:
            print("Invalid")
            break
else:
    print("Valid")