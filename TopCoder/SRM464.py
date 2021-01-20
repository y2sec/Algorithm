# SRM464D2 ColorfulBoxesAndBalls

# numRed = 2
# numBlue = 3
# onlyRed = 100
# onlyBlue = 400
# bothColors = 300

# numRed = 5
# numBlue = 5
# onlyRed = 464
# onlyBlue = 464
# bothColors = 464

# numRed = 1
# numBlue = 4
# onlyRed = 20
# onlyBlue = -30
# bothColors = -10

numRed = 9
numBlue = 1
onlyRed = -1
onlyBlue = -10
bothColors = 4

only = numRed * onlyRed + numBlue * onlyBlue
both = 0

if numRed > numBlue:
    both += numBlue * 2 * bothColors
    both += (numRed - numBlue) * onlyRed
else:
    both += numRed * 2 * bothColors
    both += (numBlue - numRed) * onlyBlue

print(max(only, both))
