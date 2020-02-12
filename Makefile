install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest test_gcli.py
	python -m pytest -vv --cov=cli test_gcli.py
	#python -m pytest --nbval notebook.ipynb

lint:
	pylint --disable=R,C cli.py
deploy:
	#deploy here
all: install lint test deploy	
	