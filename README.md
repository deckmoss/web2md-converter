# web2md-converter

Simple Python based webpage to markdown converter for the command-line.

##  Dependencies

- python313 (tested)
- beautifulsoup4
- markdownify
- pybase64
- argh
- requests

## Installation

1.a open your prefered directory

```sh
mkdir ~/Python
```

1.b change to it

```
cd ~/Python
```

3. clone git repository

```sh
git clone https://github.com/deckmoss/web2md-converter
```

4. create new python venv

```sh
python -m venv web2md-converter/pyvenv
```

5. activate python venv

```sh
source web2md-converter/pyvenv/bin/activate
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

## Usage

_Optional:_ When inactive you must re-activate project's **venv** at first.

```sh
source web2md-converter/pyvenv/bin/activate 
```


```sh
python web2md-converter/web2md-converter.py "<URL>" "<DIV TARGET-CLASS>"
```

**Example:**
```sh
python web2md-converter/web2md-converter.py "https://deckmoss.github.io/diy/unleash_ram/" "inner-post content"
```

**Output:**
```txt
Markdown content saved to output.md
```

As you can see, web2md-converter's outputed a file called output.md into that directory from which you have executed web2md-converter from.
