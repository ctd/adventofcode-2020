.PHONY: all
all: python

.PHONY: python
python: .pipenv_installed.sentinel
	pipenv run time python -u solution.py

.pipenv_installed.sentinel: Pipfile Pipfile.lock
	pipenv install
	@touch "$@"
