name = input()

words = name.split()

reverse_word = [word[::-1] for word in words]
res = ' '.join(reverse_word)
print(res)