scores_file = open('scores.txt')

r_scores = {}

# populate dictionary of restaurants and their scores
for line in scores_file:
    line = line.rstrip()
    tokens = line.split(':')

    r_scores[tokens[0]] = tokens [1]

# create sorted list from dictionary
r_scores_alpha = sorted(r_scores.items())

# iterate over the sorted list and print each restaurant and its rating
for restaurant in r_scores_alpha:
    print restaurant[0], "is rated at", restaurant[1]
