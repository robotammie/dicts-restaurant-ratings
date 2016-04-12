import sys


if len(sys.argv) != 2:
    print "ERROR: function requires a single file name to pull restaurant data from."

else:
    r_scores = {}

    scores_file = open(sys.argv[1])

    # populate dictionary of restaurants and their scores
    for line in scores_file:
        line = line.rstrip()
        tokens = line.split(':')

        r_scores[tokens[0]] = tokens [1]

    # request user input
    while True:
        user_input = raw_input("Add additional restaurants? y/n ")
        
        if user_input != "y":
            break
        
        restaurant = raw_input("Restaurant Name: ")
        rating = raw_input("Rating: ")

        r_scores[restaurant] = rating


    # create sorted list from dictionary
    r_scores_alpha = sorted(r_scores.items())

    # iterate over the sorted list and print each restaurant and its rating
    for restaurant in r_scores_alpha:
        print restaurant[0], "is rated at", restaurant[1]
