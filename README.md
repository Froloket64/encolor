# Encolor
**encolor** is a simple tool that adds color to terminal output. To select which patterns to colorize, you can use simple, but extensible (complete support for Python regex) syntax.

## Installation
### Pre-built
You can install **encolor** from [PyPI](https://pypi.org/) using `pip`:

``` sh
pip install encolor
```

### Compile
Alternatively, you can compile the project yourself.

``` sh
git clone https://github.com/Froloket64/encolor.git --depth 1 ~/encolor # You can change "~/encolor" to any other dir
pip install ~/encolor
```

## Usage
You can use the app from terminal:

``` sh
# Standalone
encolor -r "def: red, \(|\): gray" sub "def main():"

# With a pipe
echo "def main():" | encolor -r "def: red, \(|\): gray" sub
```

Or use the functions from within your Python code:

``` python
from encolor import gfx

print(gfx.colorize_ansi("def main():", "red"))
```

You can see syntax specification on the Github Wiki page.

For full documentation on module functionality, please refer to the source code (for now).
