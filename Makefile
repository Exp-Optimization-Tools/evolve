# the executable for pip
PIP=pip3
# the executable for Python
PYTHON=python3

# run the command to install dependencies in the requirements.txt file.
install:
	${PIP} install -r requirements.txt

# run the command to execute the unit tests
test:
	${PYTHON} -m unittest discover src

# run the command to run the knapsack problem solver
knapsack:
	${PYTHON} knapsack.py

# run the command to run the f6 problem solver
f6:
	${PYTHON} f6.py
