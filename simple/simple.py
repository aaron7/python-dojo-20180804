FORBIDDEN_IDEAS = ["AI", "A.I"]

def run():
    options = get_options()
    perform_voting(options)

def get_options():
    options = []
    print("Enter your amazing Dojo Ideas (Enter '-' when done):")
    while True:
        new_option = input()
        if new_option == "-":
            return options
        for bad_idea in FORBIDDEN_IDEAS:
            if bad_idea in new_option:
                print("Computer says No...")
        else:
            if new_option.strip():
                options.append(new_option)


def perform_voting(options):
    print("###############")
    print("Voting time!!!")
    print("###############")

    # Round 1
    votes = {}
    for option in options:
        vote = int(input("Votes for '{}': ".format(option)))
        votes[option] = vote

    # Round 2
    top3 = sorted(votes.items(), key=lambda kv: kv[1], reverse=True)[:3]

    print("############################################################")
    print('Second round of voting! One vote only - we will be watching.')
    print('The top 3 are: {}'.format(", ".join([i for i, _ in top3])))
    print("############################################################")

    votes = {}
    for option, _ in top3:
        vote = int(input("Final votes for '{}': ".format(option)))
        votes[option] = vote

    winner = sorted(votes.items(), key=lambda kv: kv[1], reverse=True)[:1][0][0]
    print('#########################################')
    print('The winner is ...  {}!'.format(winner))
    print('#########################################')

if __name__ == "__main__":
    run()
