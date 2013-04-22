#!/bin/sh

zip wayterm.zip __init__.py __main__.py wayterm.py wayterm_api.py wayterm_color.py wayterm_reader.py help logo
cat shebang.txt wayterm.zip > wayterm
chmod +x wayterm
