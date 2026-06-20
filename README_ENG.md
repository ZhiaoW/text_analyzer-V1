# Text Analyzer V1

## Introduction

Text Analyzer V1 is a small English text analysis project written in Python.

The program can analyze either manually entered English text or content read from a `.txt` file. It counts word frequencies and generates a simple analysis report.

This is my first Python project. I created it to:

1. Review and practise basic Python concepts, including functions, strings, lists, and dictionaries.
2. Learn how to divide a larger task into smaller modules and develop computational thinking.
3. Practise using GitHub, organising a project, and writing a README file.

---

## Features

- Removes common English punctuation
- Counts the total number of words
- Counts the number of unique words
- Finds the top N most common words
- Supports both manual text input and `.txt` files
- Saves the complete word-frequency results to a CSV file

---

## Project Structure

```text
text_analyzer-V1/
│
├── README.md
├── text_analyzer_v1.py
├── sample.txt
├── sample_output.csv
└── .gitignore
```

---

## How to Run

Open a terminal, move into the project folder, and run:

```bash
python text_analyzer_v1.py
```

Depending on your system, you may need to use:

```bash
python3 text_analyzer_v1.py
```

---

## How to Use

After running the program, you will see:

```text
Type 1 to enter text, or 2 to read a .txt file:
```

Enter `1` to type English text manually.

Enter `2` to read a `.txt` file. For example:

```text
sample.txt
```

The program will then ask:

```text
How many top words do you want to see?
```

Enter a number such as `5`, and the program will display the five most common words.

---

## Example Input

```text
Python is fun. Python is powerful.
Text Analyzer is a simple Python project.
```

---

## Example Output

```text
TEXT ANALYSIS REPORT

Total words: 11
Unique words: 8

Top 3 most common words:
1. python          3 times
2. is              2 times
3. fun             1 time

Word frequencies saved to: Text_Analyzer.csv
```

---

## CSV Output

After the program finishes, it generates a CSV file containing the frequency of every word.

Example:

| word   | count |
|--------|------:|
| python | 3     |
| is     | 2     |
| fun    | 1     |

---

## What I Learned

Through this project, I practised:

- Writing and calling Python functions
- Processing strings
- Using dictionaries to count word frequencies
- Using `for` loops
- Reading text files
- Writing CSV files
- Organising a simple Python project

---

## Future Improvements

Possible future improvements include:

- Supporting PDF files
- Supporting Chinese word segmentation
- Adding word-frequency visualisations
- Adding automated tests
- Improving punctuation and input handling

---

## Author

Created by ZhiaoW.
