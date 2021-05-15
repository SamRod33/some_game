MODULES = player character
OBJECTS = $(MODULES:=.py)
MAIN = bounce.py
TEST = test.py

play:
	python $(MAIN)

test:
	python $(TEST) 

docs:
	pdoc --html -o ./_docs $(OBJECTS)

clean:
	rm -rf *__pycache__ _docs