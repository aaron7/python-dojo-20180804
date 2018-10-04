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
    pass

if __name__ == "__main__":
    main()
