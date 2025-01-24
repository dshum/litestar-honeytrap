dev:
	pdm run litestar --app=app.main:app run --port 8081 --reload

run:
	pdm run litestar --app=app.main:app run --port 8000

test:
	pdm run pytest tests

test-verbose:
	pdm run pytest tests -s --verbose

coverage:
	pdm run pytest --cov=app tests
	pdm run coverage html -d .htmlcov

flush-messages:
	pdm run litestar --app=app.main:app messages flush

create-messages:
	pdm run litestar --app=app.main:app messages create --count=100