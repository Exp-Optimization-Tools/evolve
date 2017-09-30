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

# run the command to start the application
start:
	${PYTHON} .
