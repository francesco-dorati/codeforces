n = int(input())
words = []

for _ in range(n):
	word = input()

	if len(word) > 10:
		words.append(f'{word[0]}{len(word)-2}{word[-1]}')
	else:
		words.append(word)

for word in words:
	print(word)

