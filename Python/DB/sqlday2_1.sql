-- 테이블 생성 1 - 새로운 테이블 구조 
-- CREATE TABLE 테이블명 (컬럼명 자료형);
-- 테이블 생성 2
--  기존 테이블에서 컬럼 추출을 해서 생성 
--  기존 테이블의 데이타도 함께 복사 
-- p207 
-- CREATE TABLE 새테이블명 (SELECT */컬럼명 FROM 테이블명);
USE sqlDB;
SELECT * FROM buytbl;
-- 새로운 테이블 생성 
CREATE TABLE buytbl_a 
	(SELECT userID, prodName, price FROM buytbl);
SELECT * FROM buytbl_a;

-- 기존 테이블에서  데이타 5개만 추출해서 새로운 테이블로 구성 
CREATE TABLE buytbl_b 
	(SELECT userID, prodName, price FROM buytbl LIMIT 5);
SELECT * FROM buytbl_b;   

-- GROUP BY
-- SELECT .. FROM 테이블명 GROUP BY 컬럼명;
SELECT * FROM buytbl;

-- 합계 구하기 SUM(컬럼명)
-- 평균 구하기 AVG(컬럼명)

-- buytbl 테이블에서 price의 전체 합계와 평균구하기 
SELECT SUM(price), AVG(price) FROM buytbl;

-- 각 종목의 가격 합계, 평균를 groupName을 기준으로 정렬하여 표시하기 
SELECT groupName, SUM(price), AVG(price) 
	FROM buytbl GROUP BY groupName ORDER BY groupName;

-- AS 별칭이름;
-- 컬럼명을 대신하는 별칭 이름 표시
-- SELECT 컬럼명 AS 별칭명 FROM 테이블명;    
SELECT 	prodName AS '제품명',
		price AS '가격',
		amount AS '수량'
		FROM buytbl;

-- 함수 결과 필드명에 별칭 주기         
SELECT groupName AS '종목', 
		SUM(price) AS '합계', 
        AVG(price) AS '평균'
		FROM buytbl 
        GROUP BY groupName;

-- 퀴즈 : 사용자별로 구매합계 구하기 
/*
사용자아이디별 총구매액 표시 - GROUP BY, SUM(), AS
총구매액은? SUM(price*amount)
출력양식 
사용자아이디  총구매액  
BBK 		?
EJW			?
..
*/
SELECT * FROM buytbl;

-- 첫번째 userID만 표시 
SELECT 	userID AS '사용자아이디', 
		SUM(price*amount) AS '총 구매액'
		FROM buytbl;

-- 사용자별로 총구매액 표시 
SELECT 	userID AS '사용자아이디', 
		SUM(price*amount) AS '총 구매액'
		FROM buytbl
        GROUP BY userID;        
        
-- ***
-- 집계함수 p211
SELECT * FROM buytbl;

SELECT 	MAX(price) AS '최대값', 
		MIN(price) AS '최소값',
        COUNT(price) AS '갯수'
		FROM buytbl;
        
-- 	WITH ROLLUP
-- 소합계 p214
SELECT num, groupName, SUM(price*amount) AS 비용
	FROM buytbl
    GROUP BY groupName;
    
SELECT num, groupName, SUM(price*amount) AS 비용
	FROM buytbl
    GROUP BY groupName, num
    WITH ROLLUP;

-- CRUD 
-- 레코드 삽입 
-- INSERT INTO 테이블명 (컬럼명1, 컬럼명2... ) VALUES(값1, 값2 .. )
-- INSERT INTO 테이블명 VALUES(값1, 값2 .. )
INSERT INTO buyTbl 
	VALUES(NULL, 'EJW', '파이썬' , '서적', 3000,   30);
INSERT INTO buyTbl (num, prodName, price, amount, userID) 
	VALUES(NULL, '파이썬3', 1000, 10, 'EJW');
 
SELECT * FROM  buyTbl;   

-- 테이블 삭제 p222
/*
DELETE FROM 테이블명; 
DROP TABLE 테이블명;
TRUNCATE TABLE 테이블명;
*/ 

-- buytbl_a 가 없다면 테이블 생성 
CREATE TABLE IF NOT EXISTS buytbl_a
	(SELECT userID, prodName, price FROM buytbl);
CREATE TABLE IF NOT EXISTS buytbl_b
	(SELECT userID, prodName, price FROM buytbl);   
CREATE TABLE IF NOT EXISTS buytbl_c
	(SELECT userID, prodName, price FROM buytbl);   
    
SELECT * FROM buytbl_a;
SELECT * FROM buytbl_b;
SELECT * FROM buytbl_c;

-- 구조는 그대로. 데이타만 삭제 
DELETE FROM buytbl_a;
SELECT * FROM buytbl_a;

-- 테이블 목록을 DB에서 삭제 
DROP TABLE buytbl_b;
SELECT * FROM buytbl_b;

-- 구조는 그대로. 데이타만 삭제 
TRUNCATE TABLE buytbl_c;
SELECT * FROM buytbl_c;

-- DB안에 등록된 테이블 목록 확인하기 
SHOW TABLES;

-- 데이타베이스 생성, 목록확인, 삭제 
CREATE DATABASE IF NOT EXISTS sqlDB1;

SHOW DATABASES;

DROP DATABASE IF EXISTS sqlDB1; 

-- 레코드 수정과 삭제  
/*
UPDATE 테이블명 SET 컬럼명=값 WHERE 절;
DELETE FROM 테이블명 WEHRE 절 
*/
SELECT * FROM buytbl;

UPDATE buytbl SET amount=10 WHERE num = 1;
SELECT * FROM buytbl;

UPDATE buytbl SET amount=100 WHERE groupName='전자';
SELECT * FROM buytbl;

-- 레코드의 price 가격 모두를 150%
-- WHERE 절이 생략된 경우에는 모든 레코드에서 업데이트가 진행 
UPDATE buytbl SET price=price*1.5;
SELECT * FROM buytbl;

-- 특정 레코드 삭제 
-- DELETE FROM .. WHERE .. 
-- WHERE 절 생략시 레코드 모두 삭제 






 