FORBIDDEN_IDEAS = ["AI", "A.I"]

def main():
    options = get_options()
    perform_voting(options)

def get_options():
    # Gathers options from stdin and returns list
    options = []
    print("Enter your amazing Dojo Idea (Enter 'FINISH' when done):")
    while True:
        new_option = input()
        if new_option == "FINISH":
            return options
        for bad_idea in FORBIDDEN_IDEAS:
            if bad_idea in new_option:
                print("Computer says No...")
        else:
            if new_option.strip():
                options.append(new_option)


def perform_voting(options):
    # Iterates over options and accepts votes
    votes = {}
    for option in options:
        print(option)
        vote = int(input('Vote for this idea? '))
        votes[option] = vote
    
    top3 = sorted(votes.iteritems(), key=lambda (k,v): (v,k), reverse=True)[:3]
    print(top3)

    print('Second round of voting')
    votes = {}    
    for option, _ in top3:
        print(option)
        vote = int(input('Vote for this idea? '))
        votes[option] = vote
        
    print('Most voted idea is')
    print(sorted(votes.iteritems(), key=lambda (k,v): (v,k), reverse=True)[:1][0])


if __name__ == "__main__":
    main()
