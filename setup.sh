#!/bin/sh

zip -r wayterm.zip src/ help logo __init__.py __main__.py
cat shebang.txt wayterm.zip > wayterm
chmod +x wayterm
rm wayterm.zip
