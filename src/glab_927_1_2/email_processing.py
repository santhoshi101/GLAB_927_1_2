import nltk

# Display installed NLTK version
print("NLTK Version:", nltk.__version__)

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")

print("NLTK setup completed successfully!")



# TASK 2: STEMMING

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

email_content = (
    "Our team will be working on the upcoming "
    "project deadlines. Please ensure that all "
    "deliverables are submitted before the end "
    "of the week."
)

# Create PorterStemmer object
stemmer = PorterStemmer()

# Convert email to lowercase
normalized_email = email_content.lower()

# Tokenize the email
tokens = word_tokenize(normalized_email)

# Apply stemming
stemmed_words = []

for word in tokens:
    stemmed_words.append(stemmer.stem(word))

# Join stemmed words
stemmed_email = " ".join(stemmed_words)

# Print results
print("\nTASK 2: STEMMING")
print("Original Email:", email_content)
print("Stemmed Email:", stemmed_email)



# TASK 3: LEMMATIZATION

from nltk.stem import WordNetLemmatizer

email_content_lemma = (
    "The team members are working on their "
    "tasks diligently. Please ensure that "
    "every report is submitted promptly."
)

# Create lemmatizer object
lemmatizer = WordNetLemmatizer()

# Convert email to lowercase
normalized_email_lemma = email_content_lemma.lower()

# Tokenize the email
lemma_tokens = word_tokenize(normalized_email_lemma)

# Apply lemmatization
lemmatized_words = []

for word in lemma_tokens:
    lemmatized_words.append(lemmatizer.lemmatize(word))

# Join lemmatized words
lemmatized_email = " ".join(lemmatized_words)

# Print results
print("\nTASK 3: LEMMATIZATION")
print("Original Email:", email_content_lemma)
print("Lemmatized Email:", lemmatized_email)


# TASK 4: COMPARISON

words = ["running", "studies", "working", "children", "connections"]

print("\nTASK 4: STEMMING VS LEMMATIZATION")

print(f"{'Original':<15} {'Stemmed':<15} {'Lemmatized':<15}")
print("-" * 45)

for word in words:
    stem_result = stemmer.stem(word)
    lemma_result = lemmatizer.lemmatize(word)

    print(f"{word:<15} {stem_result:<15} {lemma_result:<15}")

# Verb lemmatization experiment
print("\nVERB LEMMATIZATION")
print("running:", lemmatizer.lemmatize("running", pos="v"))
print("working:", lemmatizer.lemmatize("working", pos="v"))

