import sys
from stats import get_words
from stats import get_occurrence
from stats import sort_characters

def get_book_text(file):
	with open(file) as f:
		text = f.read()
	return text

def report(file, words, chars):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file.lstrip('./')}...")
	print("----------- Word Count ----------")
	print(f"Found {words} total words")
	print("--------- Character Count -------")
	for item in chars:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")


def main():
	sys_len = len(sys.argv)
	if sys_len != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	file = sys.argv[1]
	try:
		text = get_book_text(file)
	except FileNotFoundError:
		print("Error: file not found")
		sys.exit(1)
	except PermissionError:
		print("Error: permission denied")
		sys.exit(1)
	words = get_words(text)
	chars = get_occurrence(text)
	sorted_chars = sort_characters(chars)
	return report(file, words, sorted_chars)


if __name__ == "__main__":
	main()

