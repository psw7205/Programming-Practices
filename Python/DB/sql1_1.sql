-- 한줄주석 
/*
 여러줄 
 주석 
*/

-- ************
-- 데이타베이스 변경하기 
-- USE 데이타베이스명 
USE world;
USE employees;

-- 현재 데이타베이스안의 테이블 확인하기 
-- SHOW tables;
SHOW TABLES;

-- 테이블 정보 조회 
SHOW TABLE STATUS;

-- 테이블 구조 확인하기 
-- DESC 테이블명;
-- describe 테이블명;
DESC salaries;

-- 특정 레코드 표시 
-- SELECT ... FROM 테이블명;
SELECT * FROM employees LIMIT 5;
SELECT * FROM employees;

-- 10개의 레코드만 csv 저장하기 
SELECT * FROM employees LIMIT 10;

-- first_name, last_name 컬럼명으로 10개의 레코드 추출 
SELECT * FROM city LIMIT 10;

/*
1) world 데이타베이스로 변경하기
2) city 테이블의 구조 확인하기.
  몇개의 컬럼명으로 이루어져 있을까요?
3) city 테이블에서 10개만 레코드 출력하기 
4) 3번의 테이블 목록을 city_10.csv 파일로 저장하기 
5) city 테이블에서 'CountryCode' 컬럼명이 NLD인 
   레코드만 출력한 후 city_nld.txt 파일로 저장하기 
*/
USE world;
DESC city;
SELECT * FROM city LIMIT 10;
SELECT * FROM city WHERE CountryCode = 'NLD';




