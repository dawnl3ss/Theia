#!/bin/bash

if [ "$(command -v python)" == "" ]; then
  echo "wget is required to use this"
  echo "download using:"
  echo "  arch:   sudo pacman -S python"
  echo "  debian: sudo apt install python"
  exit 1
fi

python theia.py "$@"
