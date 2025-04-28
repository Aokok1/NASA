import re
out=open("out1.txt")
original_string=out.read()
pattern = r'<tr  data-path="([^"]+)" data-name='
matches = re.findall(pattern, original_string)
print(matches)
with open('out2.txt', 'w', encoding='utf-8') as file:
    for match in matches[1:]:
        file.write(str(match)+'\n')