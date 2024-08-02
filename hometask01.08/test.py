result = 0
ls = ['a', 'e', 'i', 'o', 'u']
with open('about_me.txt', 'r') as file:
    text = file.read()
text = text.lower()

for i in ls:
    print(f"{i}: {text.count(i)}")
    result += text.count(i)

print(result)
