#!/bin/bash
set +x 
sleep 5

#user=$(echo -n "felix" | md5sum | grep -Eo "\w+")
# password=$(echo -n "joergen" | md5sum | grep -Eo "\w+")
#query=$(sed s/USER/$user/g /share/db_init.sql | sed s/PASS/$password/g)
mysql -uroot -p"root" < /db_init.sql

touch /tmp/it_worked
touch /InitDBWORKED
