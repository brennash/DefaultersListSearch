#!/bin/bash
BIN="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR="$(dirname "$BIN")"
LOGFILE=$DIR/log/defaulters_list.log

PS=$(ps ax | sed s/^' '*// | grep python | grep SearchEngine.py | cut -d' ' -f1)
echo $PS

