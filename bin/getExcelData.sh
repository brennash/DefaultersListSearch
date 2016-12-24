#!/bin/bash
BIN="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR="$(dirname "$BIN")"
LOGFILE=$DIR/log/defaulters_list.log


wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-december2015.xls -O $DIR/data/201512_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-december2015.xls -O $DIR/data/201512_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-september2015.xls -O $DIR/data/201509_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-september2015.xls -O $DIR/data/201509_2.xls
