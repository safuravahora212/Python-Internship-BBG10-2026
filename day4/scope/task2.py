def make_greeting(language):
    def greet(name):
        if language == "hindi":
            print("Namaste,", name)
        else:
            print("Hello,", name)
    return greet

# Use
hindi_greet = make_greeting("hindi")
hindi_greet("safa")

english_greet = make_greeting("english")
english_greet("safa")