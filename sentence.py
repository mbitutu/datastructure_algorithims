import re

def word_frequency(sentence):
    word_count = {}
    words = re.findall(r'\b\w+\b', sentence.lower())

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Testing the function
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
