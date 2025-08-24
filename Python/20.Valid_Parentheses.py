s = "()[]{}"
pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}
stack = []

for c in s:
    if c in pairs.values():
        stack.append(c)
    elif c in pairs:
        if not stack or pairs[c] != stack.pop():
            return False 
return not stack