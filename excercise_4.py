
# def word_filter_counter(text, filter_words):
#     text = text.lower()
#     word_counts = {}
#     for word in text:
#         if word in filter_words:
#             if word in word_counts:
#                 word_counts[word] += 1
#             else:
#                 word_counts[word] = 1
        
#     return word_counts
# print(
#     word_filter_counter("Hello world, hello!", ["hello"])
# )  
import re
def word_filter_counter(text, filter_words):
# Convert the text to lowercase for case-insensitive comparison
    text_lower = text.lower()

# Initialize a dictionary to store word counts
    word_counts = {}

    words = re.findall(r'\b\w+\b', text_lower)

# Iterate through the words and count occurrences
    for word in words:
        if word in filter_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts        
# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}