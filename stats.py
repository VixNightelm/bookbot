def get_words(text):
	words = text.split()
	count = 0
	for w in words:
		count += 1
	return count

def get_occurrence(text):
	letters = {}
	for l in text:
		ch = l.lower()
		letters.setdefault(ch, 0)
		letters[ch] += 1
	return letters

def sort_on(item):
	return item["num"]


def sort_characters(chars):
	result = []
	for ch, count in chars.items():
		if ch.isalpha():
			result.append({"char": ch, "num": count})
	result.sort(reverse=True, key=sort_on)
	return result
