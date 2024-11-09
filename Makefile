install: 
	pip install --upgrade pip && pip install -r requirements.txt 

format: 
	black *.py mylib/*.py *.ipynb

lint: # pylint --disable=R,C --ignore-patterns=test_.*?py $(wildcard *.py)
	ruff check *.py mylib/*.py *.ipynb
test: 
	python -m pytest --nbval -cov=mylib -cov=main test_*.py *.ipynb --disable-warnings

all: install format lint test