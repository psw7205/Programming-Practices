
/* 02장 */


-- <실습 1> --

/* 
SETX PATH "C:\Program Files\MariaDB 10.3\bin;%PATH%" /M 
*/

-- </실습 1> --



-- <실습 2> --

/*
CD \employees 

mysql -u root -p 

source employees.sql ;

show databases ;

*/

-- </실습 2> --



-- <실습 3> --

-- </실습 3> --



-- <실습 4> --

/*
SETX  PATH  "C:\MariaDB\bin;%PATH%"  /M

CD  C:\MariaDB\bin

mysql_install_db.exe  --datadir=C:\MariaDB\data  --service=MySQL  --password=1234

sc  start  MySQL 

mysql  -u  root  

sc stop MySQL 

sc delete MySQL

rmdir /s /q C:\MariaDB
*/

-- </실습 4> --
