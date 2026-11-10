GLAB 927.1.2 – NLTK Email Processing
Project Description

This project demonstrates how to use NLTK (Natural Language Toolkit) to process email content using stemming and lemmatization in Python.

The application uses two sample emails and compares the results of stemming and lemmatization.

Technologies Used
Python
uv
NLTK
VS Code
Git and GitHub
Concepts
1. NLTK

NLTK is a Python library used for natural language processing. It helps process and analyze human language.

2. Tokenization

Tokenization splits a sentence into individual words or tokens.

3. Stemming

Stemming removes word endings to produce shorter word forms. The PorterStemmer algorithm is used in this project.

Example:

working → work
studies → studi

Stemming may produce words that are not valid dictionary words.

4. Lemmatization

Lemmatization converts words into their meaningful dictionary base forms using WordNetLemmatizer.

Example:

children → child
studies → study
tasks → task
Project Setup
Requirements
Python
uv
Internet connection for NLTK data downloads
Installation

Clone or download this repository.

Open the project folder in VS Code and run:

bash
uv sync


Run the Python application:

bash
uv run python src/glab_927_1_2/email_processing.py


Note: NLTK data resources may need to be downloaded when running the application on a new machine.

Project Structure
text
GLAB_927_1_2/
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── README.md
└── src/
    └── glab_927_1_2/
        ├── __init__.py
        └── email_processing.py

Task 4 – Reflection Questions
1. What is the difference between stemming and lemmatization?

Stemming removes prefixes or suffixes from words to create shorter forms. Lemmatization uses vocabulary and linguistic rules to find the meaningful base form of a word.

2. Which technique is more likely to return dictionary forms? Give an example.

Lemmatization is more likely to return dictionary forms. For example, children becomes child.

3. How could stemming support search or matching in business emails?

Stemming helps match different forms of words. For example, searching for work may also help identify emails containing working or worked.

4. What benefit might lemmatization offer in a text-analysis pipeline?

Lemmatization improves text analysis by converting words into meaningful base forms. It helps group related words together while preserving their meaning.

5. How did the pos argument change a result?

The pos argument specifies the part of speech. For example, running remains running with the default noun setting, but with pos="v", it becomes run.

Findings and Conclusion

This project helped me understand the differences between stemming and lemmatization.

Stemming produces shorter word forms, while lemmatization produces meaningful dictionary forms.

I also learned how to use NLTK for tokenization and text processing, and how to manage a Python project using uv.