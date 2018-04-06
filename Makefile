
all:

style-check:
	python3 -m black --diff --check pdf2images bin tests
	python3 -m flake8 --ignore E501,E203,F401,W503,W504 --radon-max-cc 13 pdf2images bin tests
