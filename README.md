# Logging setup with waitress and flask

## How to use

1. Install dependencies waitress and flask.
   Venv:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install flask
$ python -m pip install waitress
```

Poetry:

```bash
$ poetry init
$ poetry install
```

2. Run
   If using a regular venv

```bash
$ python run waitress-serve --host 127.0.0.1 app:app
```

With Poetry:

```bash
$ poetry run waitress-serve --host 127.0.0.1 app:app
```
