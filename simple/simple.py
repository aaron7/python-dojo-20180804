
def run():
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
        if new_option:
            options.append(new_option)

def perform_voting(options):
    print(options)
    # Iterates over options and accepts votes
    pass


if __name__ == "__main__":
    run()
