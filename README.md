# learn-python

ToDo: 
https://www.geeksforgeeks.org/python-programming-language-tutorial/
Hier weiter machen: Learn Python Variables

## Table of contents
- [Python tutorials](#Python-tutorials)
- [IDEs](#IDEs)
- [How to](#How-to)
    - [VSCode](#VSCode)
    - [Virtual Environment](#Virtual-Environment)
    - [Install packages](#Install-packages)
- [Flask](#Flask)

## Python tutorials
- https://www.geeksforgeeks.org/python-programming-language-tutorial/

## IDEs
- [Anaconda - Python derivat for scientific stuff](https://www.anaconda.com/download)
- [Jupyter Notebook Cloud Editor](https://jupyter.org/)

## How to

### VSCode

#### VSCode - Install VSCode
https://code.visualstudio.com/docs/python/python-tutorial

#### VSCode - How to start a new project
- Python installieren
    - Unter Windows die PATH bzw. Umgebungsvariable für mindestens den aktuellen Benutzer einrichten.
- VSCode -> Python Extension installieren
- Virtual Environment (venv) erstellen (python -m venv .venv)
- VSCode: Command Palette (Ctrl+Shift+P): Python: Select Interpreter
- Python packages installieren: python -m pip install numpy

#### VSCode: Select Python Interpreter
Command Palette (Ctrl+Shift+P): Python: Select Interpreter

#### Debugging in VSCode
- https://code.visualstudio.com/docs/editor/debugging#_logpoints
- https://code.visualstudio.com/docs/python/debugging

Tip: Use Logpoints instead of print statements: Developers often litter source code with statements to quickly inspect variables without necessarily stepping through each line of code in a debugger. In VS Code, you can instead use Logpoints. A Logpoint is like a breakpoint except that it logs a message to the console and doesn't stop the program. For more information, see Logpoints in the main VS Code debugging article.print

Source: <https://code.visualstudio.com/docs/python/python-tutorial#_run-python-code> 

A Logpoint is a variant of a breakpoint that does not "break" into the debugger but instead logs a message to the console. Logpoints are especially useful for injecting logging while debugging production servers that cannot be paused or stopped.

Source: <https://code.visualstudio.com/docs/editor/debugging#_logpoints> 

### Virtual Environment

#### venv - Virtual Environment
- https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment
- https://code.visualstudio.com/docs/python/environments
- https://docs.python.org/3/library/venv.html
- https://www.pythonguis.com/tutorials/python-virtual-environments/

#### Create a virtual environment with terminal

##### macOS/Linux:
You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs.
```bash
python3 -m venv .venv
python -m venv .venv
```

##### Windows:
On Windows you can use:
```bash
py -3 -m venv .venv
python -m venv .venv
```
#### Select and activate an environment
- https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment

##### Linux:
`source .venv/bin/activate`

##### Windows:
`.venv\Scripts\activate`

### Install packages

#### Windows (may require elevation):

```bash
py -m pip install numpy
python -m pip install numpy
```

#### Linux (Debian):
```bash
apt-get install python3-tk
python3 -m pip install numpy
```

## Flask (Micro Webapplication Framework)

### Flask Tutorials
- https://code.visualstudio.com/docs/python/tutorial-flask
- https://github.com/microsoft/python-sample-vscode-flask-tutorial

- https://marketsplash.com/how-to-use-flask-with-bootstrap/
- https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-de
- https://www.geeksforgeeks.org/flask-projects/
- https://www.geeksforgeeks.org/flask-tutorial/

### Install Flask
```bash
pip install flask

python # proof your installation
import flask
```