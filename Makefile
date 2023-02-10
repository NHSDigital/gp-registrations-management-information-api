SHELL=/bin/bash -euo pipefail

.git/hooks/pre-commit:
	cp scripts/pre-commit .git/hooks/pre-commit

clean:
	rm -rf build
	rm -rf dist

_dist_include="pytest.ini poetry.lock poetry.toml pyproject.toml Makefile build/. tests specification"
dist:
	mkdir -p dist
	for f in $(_dist_include); do cp -r $$f dist; done

install:
	poetry install

test:
#	this target should be used for local unit tests ..  runs as part of the build pipeline
	make --no-print-directory -C sandbox test

smoketest:
#	this target is for end to end smoketests this would be run 'post deploy' to verify an environment is working
	poetry run pytest -v --junitxml=smoketest-report.xml -s -m smoketest
