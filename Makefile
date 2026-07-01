run:
	python main.py
test:
	SDL_VIDEODRIVER=dummy pytest tests/ -v
build:
	pyinstaller --onefile --windowed main.py
