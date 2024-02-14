import os
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def get_most_used_words(directory):
    # Initialize a Counter to keep track of word frequencies
    word_freq_counter = Counter()

    # Define a set of stopwords to filter out common words
    stop_words = set(stopwords.words('english'))

    # Iterate through each file in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            print("Processing document:", file_path)  # Print progress

            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

                # Tokenize the text into words
                words = word_tokenize(content.lower())  # Convert to lowercase for case-insensitivity

                # Filter out stopwords
                filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

                # Update word frequencies
                word_freq_counter.update(filtered_words)

    # Get the most common words and their frequencies
    most_common_words = word_freq_counter.most_common(10)  # Change the number as needed

    return most_common_words

# Example usage
directory_path = r"C:\Users\redzo\DIsights\documents"
result = get_most_used_words(directory_path)

# Print the result
for word, frequency in result:
    print(f"{word}: {frequency} times")
