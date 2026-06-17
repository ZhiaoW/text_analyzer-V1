
import csv


def clean_text(text):
    punc = ",.?!;:\'\"()[]{}<>"

    for i in punc:
        text = text.replace(i, "")
    return text


def word_counts(text):
    text = clean_text(text)
    text = text.lower()
    words = text.split()

    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts


def total_words(counts):
    total = 0
    for word in counts:
        total = total + counts[word]
    return total


def unique_word_count(counts):
    unique_count = 0
    for word in counts:
        unique_count = unique_count +1
    return unique_count


def most_common_word(counts):
    max_count = 0
    for word in counts:
        if counts[word] > max_count:
            max_count = counts[word]
            max_word = word
    return (max_word , max_count)

def top_n_word(counts , n):
    top_n_list = []
    counts_copy = counts.copy()

    for i in range(n):
        if len(counts_copy) == 0:
            break

        top_n_word, top_n_count = most_common_word(counts_copy)
        top_n_list.append((top_n_word,top_n_count))
        counts_copy.pop(top_n_word)
    return top_n_list


def text_analyzer(counts,n):
    print("TEXT ANALYSIS REPORT".center(40))
    print(f"Total word:    {total_words(counts)}")
    print(f"Unique word:    {unique_word_count(counts)}")

    top_n_list = top_n_word(counts , n)
    for word, count in top_n_list:
        print(f" Most common word:   {word} ({count} times)")


def read_txt_file(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def save_counts_to_csv(counts, output_txt):
    words = top_n_word(counts, len(counts))

    with open(output_txt, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["word", "count"])

        for word, count in words:
            writer.writerow([word, count])

def main():
    choice = input("Type 1 to enter text, or 2 to read a .txt file: ")

    if choice == "1":
        text = input("Enter your English text: ")
    elif choice == "2":
        path = input("Enter .txt file path: ")
        text = read_txt_file(path)
    else:
        print("Please enter 1 or 2.")
        return

    n = int(input("How many top words do you want to see? "))
    if n < 1:
        print("Please enter a positive number.")
        return

    counts = word_counts(text)
    output_path = "Text Analyzer.csv"

    text_analyzer(counts, n)
    save_counts_to_csv(counts, output_path)

    print(f"Frequency of words saved to {output_path}")

main()

