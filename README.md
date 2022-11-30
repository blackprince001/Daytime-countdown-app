# Daytime Countdown Application

**Tired of the conventional way our watches and armageddon devices tell time?** I can certainly say I am. That is why we have this Daytime Countdown Application. No hours, no mins, just seconds, seconds you have until the day ends. The fun part is that it just lives on your terminal.

## Quick Start

- Clone the repository

    ```bash
    git clone https://github.com/blackprince001/Daytime-countdown-app
    ```

- Move into the directory

    ```bash
    cd Daytime-countdown-app
    ```

- Set up a virtual environment with Venv on Vscode or any python environment manager you have installed, and it will automatically install the dependencies. This project uses [Poetry](https://python-poetry.org/docs) to handle dependency installs and virtual environments.

- Setup a virtualenv in the prject directory using the command below.

    ```console
    poetry shell
    ```

- To simply install project dependencies, run the command below.

  ```console
  poetry install --sync
  ```

- The simplicity of this application did not allow the inclusion of unit testing, ie. I was too lazy to write tests.
  
- Poetry will handle everything for you while you sit back and enjoy some hot choco. That will all for this section.

## Screenshots

- ![Alt text](docs/images/Screenshot%20from%202022-11-30%2020-13-34.png)

- ![Alt text](docs/images/Screenshot%20from%202022-11-30%2020-13-44.png)

## Project Structure

```console
.
├── daytime_countdown_app
│   ├── __init__.py
│   ├── main.py
│   └── style-main.css
├── docs
│   └── images
│       ├── Screenshot from 2022-11-30 20-13-34.png
│       └── Screenshot from 2022-11-30 20-13-44.png
├── poetry.lock
├── poetry.toml
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py

4 directories, 10 files
```
