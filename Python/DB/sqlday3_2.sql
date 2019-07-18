-- 크로스 조인 (상호조인) 
-- p277
-- 키가 정의되어 있지 않아도 된다. 
-- 모든행이 반복됨 
-- 한쪽 테이블의 모든 행과 다른쪽 테이블의 모든 행이 조인됨 => 카티션곱
-- SELECT * 또는 컬럼명
--    FROM 테이블1 
--      CROSS JOIN 테이블2;

USE sqldb;

SELECT * FROM buyTbl
     CROSS JOIN userTbl
     LIMIT 20;

SELECT count(*) FROM buyTbl; -- 12
SELECT count(*) FROM userTbl; -- 10     
SELECT count(*) FROM buyTbl CROSS JOIN userTbl;  -- 120   

-- 셀프 조인(자체 조인) 
-- p278
-- INNER JOIN의 일종. 같은 테이블을 조인한다. 
-- 조직도등에 이용 
-- p280 

-- 테이블 생성 
-- sqlDB 안에 empTBL 테이블 생성 
-- empTBL.sql 파일 열기  
-- sqlDB/empTBL 

-- 직원의 상관의 구내번호를 찾아라 
-- 직원(emp), 상관(manager), 구내번호(empTel) 

-- 가로로 2번 컬럼이 반복되어 표시 
SELECT * 
   FROM empTBL A
     INNER JOIN empTBL B
        -- 중복되는 값의 컬럼명 지정 
        ON A.manager = B.emp;

-- 우대리 직원의 상관의 구내번호를 찾아라 
SELECT 	A.emp AS '직원', 
		A.manager AS '상관', 
		B.empTel AS '구내번호' 
		   FROM empTBL A
			 INNER JOIN empTBL B
				-- 중복되는 값의 컬럼명 지정 
				ON A.manager = B.emp
			WHERE A.emp = '우대리';

-- UNION / UNION ALL 
-- 쿼리의 결과를 합쳐서 보여준다. 
-- UNION 중복 허용 
-- UNION ALL 중복된 부분 삭제 

-- SELECT ... -- 쿼리1
-- UNION
-- SELECT ... -- 쿼리2

SELECT * FROM clubtbl; -- 동아리정보 
SELECT * FROM stdtbl; -- 학생정보 
-- 첫번째 쿼리의 컬럼 아래에 두번째 쿼리의 컬럼 내용이 추가된다. 
SELECT stdName AS '학생이름 + 동아리이름' FROM stdtbl
UNION
SELECT clubName AS ' 동아리이름' FROM clubtbl; 

-- NOT IN : 첫번째 쿼리의 결과중 두번째 쿼리에 해당하는 것을 제외 
-- IN : 두번째 쿼리의 결과만 조회 

-- SELECT 첫번째 쿼리 
		WHERE ... [NOT IN / IN ] ( SELECT 두번째 쿼리 )

-- SELECT * 또는 컬럼명 FROM 테이블1
--    WHERE 조건절1 NOT IN 또는 IN ( SELECT * 또는 컬럼명 FROM 테이블2 WHERE 조건절2) ;

-- 사용자중 전화가 없는 사람을 제외하고 싶다. NOT IN
-- 사용자중 전화가 없는 사람만 조회 IN

-- LEFT OUTER JOIN 으로 모두 출력, 2개의 테이블 모든 목록 출력  
USE sqlDB;
SELECT 	U.userID, U.name, 
		B.prodName, U.addr, 
        CONCAT(U.mobile1, U.mobile2)  AS '연락처'
   FROM userTbl U
      LEFT OUTER JOIN buyTbl B
         ON U.userID = B.userID 
   ORDER BY U.userID;
   
-- 전화가 없는 사람 제외 : NOT IN => 전화기가 있는 사람만 표시 
SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTbl
   WHERE name NOT IN ( SELECT name FROM userTbl WHERE mobile1 IS NULL) ;
   
-- 전화가 없는 사람만 표시 : IN
SELECT name FROM userTbl
   WHERE name IN ( SELECT name FROM userTbl WHERE mobile1 IS NULL) ;















     