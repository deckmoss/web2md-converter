# web2md-converter

Simple Python based webpage to markdown converter for the command-line.

## Table of Contents

- **Dependencies:**
  - [Python/PIP](#dependencies)
- **Linux:**
  - **Using venv:**
    - [Quick Installation](#variant-a-quick)
    - [Step-By-Step Installation](#variant-b-step-by-step)
  - **Using pipenv [RECOMMENDED]**
    - [Quick Installation](#pipenv-quick-installation)
    - [Pipenv Usage](#usage)
- **NixOS:**
  - [Quick Installation](#variant-a-quick-1)
  - [Step-By-Step Installation](#variant-b-step-by-step-1)
- **Usage, non-Pipenv:**
  - [Usage](#usage-1)


## Dependencies

- python313 (tested)
- beautifulsoup4
- markdownify
- pybase64
- argh
- requests

## Installation (Linux)

### Variant A: Quick

copy, paste and execute this line on your shell:

_all steps at once: cloning repo activating virtual environment, installing package requirements into virtual environment_
_(example dir `~/Python`)_
```sh
mkdir ~/Python \
&& cd ~/Python \
&& git clone https://github.com/deckmoss/web2md-converter \
&& python3 -m venv web2md-converter/venv_web2md \
&& source web2md-converter/venv_web2md/bin/activate; \
python3 -m pip install --upgrade pip \
&& python3 -m pip install -r web2md-converter/requirements.txt
```

### Variant B: Step-by-step

1. a) open your prefered directory
_(example dir `~/Python`)_
```sh
mkdir ~/Python
```

1. b) change to it
_(example dir `~/Python`)_
```
cd ~/Python
```

2. clone git repository

```sh
git clone https://github.com/deckmoss/web2md-converter
```

3. create new python venv

```sh
python3 -m venv web2md-converter/venv_web2md
```

4. activate python venv

```sh
source web2md-converter/venv_web2md/bin/activate
```

5. initialize pip

```sh
python3 -m pip install --upgrade pip
```

6. install pip requirements from preserved file

```sh
python3 -m pip install -r web2md-converter/requirements.txt
```

_Optional:_

7. Deactivate venv if you do not want to execute web2md-converter right now.

```sh
deactivate
```

## Pipenv

### Pipenv Quick Installation

_(example dir `~/Python`)_
```sh
mkdir ~/Python \
&& cd ~/Python \
&& git clone https://github.com/deckmoss/web2md-converter \
&& python3 -m pip install --upgrade pip \
&& python3 -m pip install pipenv \
&& cd web2md-converter \
&& pipenv install
```

### Usage

Pipenv allows us to run the web2md-converter without activating the virtual environment like in the other variants. 

```sh
pipenv run python3 /path/to/web2md-converter/web2md-converter.py "URL" "DIV CLASS"
```

**Example:**

```sh
pipenv run python3 web2md-converter/web2md-converter.py "https://deckmoss.github.io/diy/unleash_ram/" "inner-post content"
```

## Installation (NixOS)

### Variant A: Quick

copy, paste and execute this line on your shell:
_(example dir `~/Python`)_
```sh
mkdir ~/Python \
&& cd ~/Python \
&& git clone https://github.com/deckmoss/web2md-converter; \
nix-shell web2md-converter/shell.nix
```

### Variant B: Step-by-step

1. a) open your prefered directory
_(example dir `~/Python`)_
```sh
mkdir ~/Python
```

1. b) change to it
_(example dir `~/Python`)_
```
cd ~/Python
```

2. clone git repository

```sh
git clone https://github.com/deckmoss/web2md-converter
```

3. create nix-shell user environment from preserved file
 
```sh
nix-shell web2md-converter/shell.nix
```

## Usage

### Activate virtual environment (non-NixOS)
_Optional:_ When inactive you must re-activate project's **venv** at first.

1. Change directory to the parent of the local repo
_(example dir `~/Python`)_
```sh
cd ~/Python
```
2. activate venv
```sh
source web2md-converter/venv_web2md/bin/activate 
```

### Activate virtual environment (NixOS)

create nix-shell user environment from preserved file

1. Change directory to the parent of the local repo
_(example dir `~/Python`)_
```sh
cd ~/Python
```

2. run nix-shell command
```sh
nix-shell web2md-converter/shell.nix
```

### Execution (all)
```sh
python3 web2md-converter/web2md-converter.py "<URL>" "<DIV TARGET-CLASS>"
```

**Example:**
```sh
python3 web2md-converter/web2md-converter.py "https://deckmoss.github.io/diy/unleash_ram/" "inner-post content"
```

**Output:**
```txt
Markdown content saved to output.md
```

As you can see, web2md-converter's outputed a file called output.md into that directory from which you have executed web2md-converter from.

## Deactivation of virtual environment (non-NixOS)

```sh
deactivate
```

## Deactivation of virtual environment (NixOS)

Escape the user environment with:

**CTRL + D**
