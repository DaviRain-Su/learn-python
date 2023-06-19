
def display_list(lists):
    for item in lists:
        # item is list
        # `[docs/meet_problem.md]`
        if isinstance(item, list):
            for nested_item in item:
                print("Nested List:", nested_item)
        else:
            print(item)

movies = [
    "This Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    ["This Holy Grail", "The Life of Brian", "The Meaning of Life"]
]

display_list(movies)
