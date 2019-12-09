min = 146810
max = 612564

def check_value(intStr):
    last = intStr[0]
    foundPair = False
    for c in intStr[1:]:
        if c < last:
            return False
        if c == last:
            foundPair = True
        last = c
    return foundPair

matches = 0
for i in range(min, max):
    if check_value(str(i)):
        matches += 1
print('First case', matches)

def check_value_harder(intStr):
    last = intStr[0]
    foundPair = False
    comboCount = 1
    for c in intStr[1:]:
        if c < last:
            return False
        if c == last:
            comboCount += 1
        else:
            if comboCount == 2:
                foundPair = True
            comboCount = 1
        last = c
    if comboCount == 2:
        foundPair = True
    return foundPair

matches = 0
for i in range(min, max):
    if check_value_harder(str(i)):
        matches += 1
print('Second part', matches)