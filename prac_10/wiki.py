import wikipedia


def main():
    """Search for a phrase and print the summary of the first result."""
    print("Welcome to Wikipedia Searcher!")
    search_phrase = input("Enter a search phrase: ")
    while search_phrase != "":  # while search phrase is not empty string
        try:  # try to print the summary of the first result
            print(wikipedia.summary(search_phrase))
        except wikipedia.exceptions.DisambiguationError as e:  # if there is a disambiguation error
            print(e.options)  # print the options of the disambiguation error
        search_phrase = input("Enter a search phrase: ")


main()
