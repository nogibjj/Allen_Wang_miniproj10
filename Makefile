install: 
	pip install --upgrade pip && pip install -r requirements.txt 

format: 
	black *.py mylib/*.py

lint: # pylint --disable=R,C --ignore-patterns=test_.*?py $(wildcard *.py)
	ruff check *.py mylib/*.py
test: 
	python -m pytest --nbval -cov=mylib -cov=main test_*.py --disable-warnings

all: install format lint test