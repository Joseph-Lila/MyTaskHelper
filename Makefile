fix: isort lint
	cat "Good luck!"

lint:
	pylint src/ tests/

isort:
	isort src/ tests/
