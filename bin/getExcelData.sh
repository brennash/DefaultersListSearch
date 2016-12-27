#!/bin/bash
BIN="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR="$(dirname "$BIN")"
LOGFILE=$DIR/log/defaulters_list.log

wget -q http://www.payeanytime.ie/en/press/defaulters/defaulters-list1-september2016.xls -O $DIR/data/201609_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/defaulters-list2-september2016.xls -O $DIR/data/201609_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/defaulters-list1-june2016.xls -O $DIR/data/201606_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/defaulters-list2-june2016.xls -O $DIR/data/201606_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/defaulters-list1-march2016.xls -O $DIR/data/201603_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/defaulters-list2-march2016.xls -O $DIR/data/201603_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-december2015.xls -O $DIR/data/201512_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-december2015.xls -O $DIR/data/201512_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-september2015.xls -O $DIR/data/201509_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-september2015.xls -O $DIR/data/201509_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-june2015.xls -O $DIR/data/201506_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-june2015.xls -O $DIR/data/201506_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-march2015.xls -O $DIR/data/201503_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-march2015.xls -O $DIR/data/201503_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-dec2014.xls -O $DIR/data/201412_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-dec2014.xls -O $DIR/data/201412_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-sept2014.xls -O $DIR/data/201409_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-sept2014.xls -O $DIR/data/201409_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-june2014.xls -O $DIR/data/201406_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-june2014.xls -O $DIR/data/201406_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-march2014.xls -O $DIR/data/201403_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-march2014.xls -O $DIR/data/201403_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-december2013.xls -O $DIR/data/201312_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-december2013.xls -O $DIR/data/201312_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-sept2013.xls -O $DIR/data/201309_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-sept2013.xls -O $DIR/data/201309_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-june2013.xls -O $DIR/data/201306_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-june2013.xls -O $DIR/data/201306_2.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list1-march2013.xls -O $DIR/data/201303_1.xls
wget -q http://www.payeanytime.ie/en/press/defaulters/archive/defaulters-list2-march2013.xls -O $DIR/data/201303_2.xls
