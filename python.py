inputWord = input("enter your word: ", )

word = inputWord.replace(" ", "").lower()

print(word)

reversedWord = word[::-1]
# List[start:end:step]
print(word == reversedWord)