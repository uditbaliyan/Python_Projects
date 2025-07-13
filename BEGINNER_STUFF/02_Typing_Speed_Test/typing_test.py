import difflib
import random
import time

PRO_ACCURACY = 100
PRO_WPM = 60
GOOD_ACCURACY = 80


# Sample sentences (you can add more or load from a file)
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests help improve accuracy and speed.",
    "Python is a powerful programming language.",
    "Consistency is more important than perfection.",
    "Practice makes a man perfect.",
]


def get_random_sentence():
    return random.choice(SENTENCES)


def calculate_wpm(typed, elapsed_seconds):
    words = len(typed) / 5
    return words / (elapsed_seconds / 60)


def calculate_accuracy(original, typed):
    matcher = difflib.SequenceMatcher(None, original, typed)
    return matcher.ratio() * 100


def main():
    print("""\n🎯 Welcome to the Typing Speed Test!""")
    sentence = get_random_sentence()
    print("\nType the following sentence:\n")
    print(f"👉 {sentence}\n")

    input("Press Enter to start typing...")

    start = time.perf_counter()
    typed = input("> ")
    end = time.perf_counter()

    elapsed = end - start
    wpm = calculate_wpm(typed, elapsed)
    accuracy = calculate_accuracy(sentence, typed)

    print("\n⌛ Time Taken: {:.2f} seconds".format(elapsed))
    print("💨 WPM: {:.2f}".format(wpm))
    print("🎯 Accuracy: {:.2f}%".format(accuracy))

    if accuracy == PRO_ACCURACY and wpm >= PRO_WPM:
        print("🔥 You're a pro!")
    elif accuracy >= GOOD_ACCURACY:
        print("👍 Good job! Keep practicing.")
    else:
        print("💡 Try to focus on both speed and correctness.")


if __name__ == "__main__":
    main()
