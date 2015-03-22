# Gabriel Ewing 8/1/2014

from pprint import pprint
import sys

rounds = input('Enter the number of rounds: ')

# error handling for case where norm cannot be achieved
if rounds < 4:
   print 'Not enough rounds for a norm. Exiting.'
   raw_input("Press enter to continue")
   sys.exit()

# list of opponents
opps = range(0, rounds)

# prompt for opponent ratings
for x in opps:
   opps[x] = input('Enter the rating of the round ' + str(x + 1) + ' opponent: ')

# dictionary with norm level and required score
levels = {'1200' : 1, '1400' : 1, '1600' : 1, '1800' : 1, '2000' : 1, '2200' : 1, '2400' : 1}

# Calculating required score. Outer loop is the norm level, inner loop is each opponent.
for level, score in levels.iteritems():
   for opponentRating in opps:
     # Case where norm level is more than 200 above opponent rating
     if int(level) - 200 > opponentRating:
       levels[level] = float(levels[level] + 1)
     # Case where norm level is between 200 and 0 points above opponent rating
     elif int(level) > opponentRating:
       levels[level] = float(levels[level] + .5) + float((int(level) - opponentRating))/400
     # Case where norm level is more than 400 points below opponent rating
     elif int(level) + 400 < opponentRating:
       levels[level] = float(levels[level])
     # Case where norm level is between 0 and 400 points below opponent rating
     else:
       levels[level] = float(levels[level] + .5) - float((opponentRating - int(level)))/800

# Print the results
print 'If you scored MORE than the following number of points, you made the norm at that level: '
pprint(levels)

raw_input("Press enter to continue")
