# web2md-converter

Simple Python based webpage to markdown converter for the command-line.

##  Dependencies

- python313 (tested)
- beautifulsoup4
- markdownify
- pybase64
- argh
- requests

## Installation (Linux)

### Quick

copy, paste and execute these one-by-one in your shell:

_step 1: cloning repo enabling virtual environment_
```sh
mkdir ~/Python \
&& cd ~/Python \
&& git clone https://github.com/deckmoss/web2md-converter \
&& python3 -m venv web2md-converter/venv_web2md \
&& source web2md-converter/venv_web2md/bin/activate
```
_step 2: installing package requirements into venv_
```sh
python3 -m pip install --upgrade pip \
&& python3 -m pip install -r web2md-converter/requirements.txt
```

### Step-by-step

1. a) open your prefered directory

```sh
mkdir ~/Python
```

1. b) change to it

```
cd ~/Python
```

3. clone git repository

```sh
git clone https://github.com/deckmoss/web2md-converter
```

4. create new python venv

```sh
python3 -m venv web2md-converter/venv_web2md
```

5. activate python venv

```sh
source web2md-converter/venv_web2md/bin/activate
```

7. initialize pip

```sh
python3 -m pip install --upgrade pip
```

8. install pip requirements from preserved file

```sh
python3 -m pip install -r web2md-converter/requirements.txt
```

_Optional:_

9. Deactivate venv if you do not want to execute web2md-converter right now.

```sh
deactivate
```

## Installation (NixOS)

### Quick

copy, paste and execute these one-by-one in your shell:

```sh
&& cd ~/Python \
&& git clone https://github.com/deckmoss/web2md-converter \
&& cd web2md-converter; \
nix-shell
```

### Step-by-step

1. a) open your prefered directory

```sh
mkdir ~/Python
```

1. b) change to it

```
cd ~/Python
```

3. clone git repository

```sh
git clone https://github.com/deckmoss/web2md-converter
```

4. create nix-shell user environment from preserved file
 
```sh
cd web2md-converter && nix-shell
```

## Usage

### Activation (non-NixOS)
_Optional:_ When inactive you must re-activate project's **venv** at first.

```sh
source web2md-converter/venv_web2md/bin/activate 
```

### Activation (NixOS)

create nix-shell user environment from preserved file
 
```sh
cd web2md-converter && nix-shell
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

## Deactivation (non-NixOS)

```sh
deactivate
```

## Deactivation (NixOS)

Escape the user environment with:

**CTRL + D**
