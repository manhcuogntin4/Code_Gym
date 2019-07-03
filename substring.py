def occurrences (string, look_for):
    start = 0
    matches = 0

    while True:
        start = string.find(look_for,start)
        if start < 0:
            break

        start += len(look_for)
        matches += 1

    return matches
print(occurrences('abrabra', 'abra'))