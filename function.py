def most_frequent(string):
    frequencies = {}
    for letter in string:
        frequencies[letter] = frequencies.get(letter, 0) + 1
    sorted_letters = sorted(frequencies, key=frequencies.get, reverse=True)
    for letter in sorted_letters:
        print(letter, ":", frequencies[letter])
input_string = ("mississippi")
most_frequent(input_string)

