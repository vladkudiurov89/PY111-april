def check_brackets(brackets_row: str) -> bool:
	"""Check whether input string is a valid bracket sequence
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise"""

	bracket = 0
	for i in brackets_row:
		if i == '(':
			bracket += 1
		else:
			bracket -= 1
			if bracket <= -1:
				return False

	return False if bracket != 0 else True

