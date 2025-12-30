from cs50 import get_string

Text = get_string("Text: ")

# calculating letters
letters_count = 0
for letter in Text:
    if letter.isalpha():
        letters_count += 1

# calculating words
words_count = 1
for word in Text:
    if word == " ":
        words_count += 1

# calculating sentences
sentance_count = 0
for sentance in Text:
    if sentance == "!" or sentance == "." or sentance == "?":
        sentance_count += 1

# calculating grade
L = float(letters_count) / float(words_count) * 100
S = float(sentance_count) / float(words_count) * 100
grade = round(0.0588 * L - 0.296 * S - 15.8)

# calculating resulta
if grade < 1:
    print("Before Grade 1")
elif grade > 1 and grade < 16:
    print("Grade of the sentance is ", grade)
else:
    print("Grade of the sentance is 16+")
