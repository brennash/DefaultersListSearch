#!/bin/bash
BIN="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR="$(dirname "$BIN")"
LOGFILE=$DIR/log/defaulters_list.log

echo 
python -u $DIR/src/SearchEngine.py $DIR/data &
python -u $DIR/src/App.py 

