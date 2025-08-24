# Input: strs = ["flower","flow","flight"]
strs = ["flower","flow","flight"]
result = ""

prefix = strs[0]

for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]  
    if prefix == "":
        break
result = prefix


print(result)