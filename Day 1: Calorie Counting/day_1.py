f = open('day_1_input.txt')
elves = []
elf_current = 0

while True:
    currentLine = f.readline()
    if not currentLine:
        break
    if currentLine != "\n":
        elf_current += int(currentLine)
    else:
        elves.append(elf_current)
        elf_current = 0

elves_sorted = sorted(elves, reverse=True)

#task 1
print(max(elves))

#task 2
print(sum(elves_sorted[0:3]))
f.close()