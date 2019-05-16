text_file = 'test.txt'
with open(text_file) as infile:
    lines=0
    words=0
    characters=0
    for line in infile:
        wordslist=line.split()
        lines=lines+1
        words=words+len(wordslist)
        characters += sum(len(word) for word in wordslist)
print("From " + text_file + "\n___________")
print("Lines =")
print(lines)
print()
print("Words =")
print(words)
print()
print("Characters =")
print(characters)
print(input())
