# Todo Cli

**A simple, fast, and modern Command Line Interface (CLI) application built with Python to manage your daily tasks directly from the terminal.**

[![PyPI](https://img.shields.io/pypi/v/todocli.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/todocli.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/todocli)][pypi status]
[![License](https://img.shields.io/pypi/l/todocli)][license]

[![Read the documentation at https://todocli.readthedocs.io/](https://img.shields.io/readthedocs/todocli/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/pradipta-web/todocli/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/pradipta-web/todocli/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/todocli/
[read the docs]: https://todocli.readthedocs.io/
[tests]: https://github.com/pradipta-web/todocli/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/pradipta-web/todocli
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

* **Add Tasks**: Easily add new tasks to your list (`todocli add`).
* **View List**: Check all your current tasks with a clean numbered view (`todocli list`).
* **Mark Completed**: Mark your finished tasks with a check status `[✓]` (`todocli done`).
* **Delete Tasks**: Remove tasks you no longer need (`todocli delete`).
* **Persistent Storage**: Automatically saves your tasks locally in a JSON file.

## Requirements

* **Python** >= 3.10 (kamu menggunakan Python 3.14)
* **Poetry** (untuk manajemen *dependency* dan *virtual environment*)

## Installation

You can install _Todo Cli_ via [pip] from [PyPI]:

```console
$ pip install todocli
```

## Usage

```console
$ poetry run todocli add "Belajar Python"
$ poetry run todocli list
$poetry run todocli done 1
$ poetry run todocli delete 1

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Todo Cli_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Author

**Kinervaaa**

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/pradipta-web/todocli/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/pradipta-web/todocli/blob/main/LICENSE
[contributor guide]: https://github.com/pradipta-web/todocli/blob/main/CONTRIBUTING.md
[command-line reference]: https://todocli.readthedocs.io/en/latest/usage.html
