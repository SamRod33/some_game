MODULES = player character
OBJECTS = $(MODULES:=.py)
MAIN = bounce.py

play:
	python $(MAIN)

test:
	python test.py 

player-test:
	python player_test.py

docs:
	rm -rf _docs
	pdoc --html -o ./_docs $(OBJECTS)

clean:
	rm -rf *__pycache__ _docs