-- 데이타베이스 생성 
CREATE DATABASE tableDB;

DESC bbsTbl;
SELECT * FROM bbsTBL;


-- *** 테이블 수정 ***
-- p 328

SELECT * FROM userTBL;

-- 기존 테이블에서 새로운 컬럼 추가 

-- ALTER TABLE 테이블명
-- 	ADD 컬럼명 데이터형( CHAR(), INT, VARCHAR(), DATE, DATETIME ... )
-- 		[DEFAULT 디폴트값] -- 기본값 설정 
-- 		[NULL/NOT NULL]; -- Null 허용함

-- 새로운 컬럼 추가 1
ALTER TABLE userTbl
	ADD homepage VARCHAR(30)  -- 열추가
		DEFAULT 'http://google.com' -- 디폴트값
		NULL; -- Null 허용함
        
SELECT * FROM userTBL;
        
-- 새로운 컬럼 추가 2        
ALTER TABLE userTbl
	ADD age INT(3) -- 열추가
		NULL; -- Null 허용함        

SELECT * FROM userTBL;

-- 기존 컬럼 삭제 1 - 키가 없는 경우 
-- ALTER TABLE 테이블명
-- 	DROP COLUMN 컬럼명;

ALTER TABLE userTBL
	DROP COLUMN age;
    
SELECT * FROM userTBL;

-- 기존 컬럼 삭제 2 - 키가 있는 경우 
-- 주의사항 : 외래키 -> 기본키 순으로 먼저 삭제한 후 컬럼 삭제 진행 

-- STEP1 : 키삭제 
-- ALTER TABLE 테이블명
-- DROP PRIMARY KEY 또는 FOREIGN KEY 테이블명_ibfk_1; 

-- STEP2 : 컬럼 삭제 
--  ALTER TABLE 테이블명
-- 	DROP COLUMN 컬럼명;

DESC userTbl;
DESC buyTbl;

-- userTbl 테이블에 PRIMARY KEY 삭제 
-- 오류 발생 : FOREIGN KEY가 설정되어 있어 오류 발생 

-- ALTER TABLE userTbl
-- 	DROP PRIMARY KEY; 

DESC buyTbl;

-- 외래키 삭제  buyTbl
ALTER TABLE buyTbl
	DROP FOREIGN KEY buytbl_ibfk_1;
    
DESC buyTbl;  
SELECT * FROM buyTbl; 

-- PRIMARY KEY 삭제 userTbl
ALTER TABLE userTbl
	DROP PRIMARY KEY; 
    
DESC userTbl;  
SELECT * FROM userTbl;     

-- 컬럼 삭제 mobile1, mobile2
ALTER TABLE userTbl
	DROP COLUMN  mobile1;
    
ALTER TABLE userTbl
	DROP COLUMN mobile2;
    
DESC userTbl;  
SELECT * FROM userTbl; 

-- 컬럼 수정 
-- 컬럼명1을 컬럼명2로 수정 
-- ALTER TABLE 테이블명 
-- 	CHANGE COLUMN 컬럼명1 컬럼명2 데이타형 [NULL 또는 NOT NULL] ;
    
ALTER TABLE userTbl
	CHANGE COLUMN name uName VARCHAR(20) NULL ;
    
DESC userTbl;  
SELECT * FROM userTbl; 

-- 테이블 구조 변경 퀴즈 
-- 1) employees 테이블에서 10개의 레코드를 복사하여 새로운 테이블 생성 
-- emp_no, first_name, last_name, gender
/*
  CREATE TABLE 테이블명1 ( SELECT 컬럼명1... FROM 테이블명2);
*/
CREATE TABLE test2
	(	SELECT 
			emp_no, first_name, last_name, gender 
			FROM employees
			LIMIT 10);
     
SELECT * FROM test2; 

-- 2) 새로운 컬럼 추가 
--  State 컬럼 추가 - 디폴트값으로 ?

ALTER TABLE test2
	ADD State VARCHAR(30)  -- 열추가
		DEFAULT 'Hawaii' -- 디폴트값
		NULL; -- Null 허용함
SELECT * FROM test2; 

-- 3) 기존 컬럼 삭제 
--     gender 
ALTER TABLE test2
	DROP COLUMN gender;
SELECT * FROM test2; 

-- 4) 컬럼 수정 
-- last_name => family_name 으로 컬럼명 수정 

ALTER TABLE test2
	CHANGE COLUMN last_name family_name VARCHAR(20);
    
SELECT * FROM test2; 



