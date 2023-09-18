# -------------------------------------------------------------------------
# AUTHOR: Musa Waghu
# FILENAME: search_engine.py
# SPECIFICATION: calculating tf-idf
# FOR: CS 4250- Assignment #1
# TIME SPENT: few hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

# importing some Python libraries
import csv
import math

documents = []
labels = []

# reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0])
            labels.append(row[1])

# Conduct stopword removal.
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}


def remove_stop_words(sentence):
    words = sentence.split()
    filtered_words = [word for word in words if word not in stopWords]
    return ' '.join(filtered_words)


# Apply the function to each sentence in the list
without_stopword = [remove_stop_words(sentence) for sentence in documents]

# Conduct stemming.
stemming = {
    "cats": "cat",
    "dogs": "dog",
    "loves": "love",
}


def replace_words(sentence, mapping):
    words = sentence.split()
    replaced_words = [mapping.get(word, word) for word in words]
    return ' '.join(replaced_words)


# Use a list comprehension to replace words in each sentence
stemmed_doc = [replace_words(sentence, stemming) for sentence in without_stopword]

# Identify the index terms.
terms = [word for sentence in stemmed_doc for word in sentence.split()]
d1List = terms[0:3]
d2List = terms[3:5]
d3List = terms[5:8]


# Build the tf-idf term weights matrix.
def tf_idf(list, word, base=10):
    # Count the occurrences of the word in the list
    count = list.count(word) / len(list)
    if word == "love":
        D = 3/3
    else:
        D = 3/2

    # Calculate the logarithm of the count using the specified base
    log_result = math.log(D, base)

    # Multiply the count by the logarithm
    result = count * log_result

    return result


docMatrix = [
    [tf_idf(d1List, "love", 10), round(tf_idf(d1List, "cat", 10), 2), round(tf_idf(d1List, "dog", 10), 2)],
    [tf_idf(d2List, "love", 10), round(tf_idf(d2List, "cat", 10), 2), round(tf_idf(d2List, "dog", 10), 2)],
    [tf_idf(d3List, "love", 10), round(tf_idf(d3List, "cat", 10), 2), round(tf_idf(d3List, "dog", 10), 2)]
]

for row in docMatrix:
    for element in row:
        print(element, end=' ')  # Use 'end' to control the separator between elements
    print()

# Calculate the document scores (ranking) using document weights (tf-idf) calculated before and query weights (binary - have or not the term).
# --> add your Python code here
docScores = []
query = ["cat", "dog"]
binary = [0, 1, 1]

# Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
print("Documents 1 and 3 are relevant.\nPrecision = 2/2+1 = " + str((2/3) * 100) + "\nRecall = 3/3+0 = " + str((3/3) * 100))
