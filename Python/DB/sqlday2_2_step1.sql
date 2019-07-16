-- 변수 생성과 출력 
-- p234
USE sqldb;

-- SET @변수명 = 초기값;
-- SELECT @변수명;

SET @a = 1; 
SET @b = 10; 
SET @c = 'mySQL'; 
SET @d = 'sqlLite'; 

-- 출력 
SELECT @a,@b,@c,@d;
SELECT @a,@b, @a+@b, @a*@b;
SELECT @c,@d, @c+@d;

-- 테이블과 변수 함께 사용하기 
SELECT * FROM usertbl;

SET @deco = '***';
SELECT @deco;
SELECT userID AS '아이디', 
		@deco AS ' ', 
		addr AS '지역' 
		FROM usertbl;

/* 퀴즈
 usertbl 테이블에서 키가 180 넘는 레코드만 추출한 후 아래와 같은 
 형태로 출력하여라 
 
           이름    키   
 가수이름 => 김경호   ?  cm
 가수이름 => 이승기   ?  cm 
 
 */
SET @deco1 = '가수 이름 =>'; 
SET @deco2 = ' cm';

SELECT @deco1 AS ' ', 
		name AS '이 름',
        height As '키',
		@deco2 AS ' '
		FROM usertbl
        WHERE height>180;

-- 데이터 형변환 CASTING  -- 
-- p236
/*
CAST ( .. AS 데이터형식)
CONVERT ( .. AS 데이터형식)

데이터형식 :
 BINARY, CHAR(), DATE , TIME, 
 SIGNED INTEGER, UNSIGNED INTEGER
*/

USE sqldb;
-- 평균구매 개수가 실수 => 정수 
SELECT * FROM buyTbl;
-- 실수형으로 결과값 리턴 
SELECT AVG(amount) AS '평균 구매 개수' FROM buyTbl ;

-- 양의 정수형으로 결과값 리턴 
SELECT 
	CAST(AVG(amount) AS SIGNED INTEGER) 
	AS '평균 구매 개수'  
	FROM buyTbl ;
-- 또는
SELECT 
	CONVERT(AVG(amount) , SIGNED INTEGER) 
	AS '평균 구매 개수'  
	FROM buyTbl ;

-- 실수형숫자 => 문자 
SELECT CAST( 23.5 AS CHAR(10));
-- 문자 => 양의 정수 
SELECT CAST( '2nd' AS SIGNED INTEGER); -- 2
SELECT CAST( '2nd123' AS SIGNED INTEGER); -- 2

-- 날짜 자료형 종류 
-- p232
-- DATE, TIME, DATETIME

-- 문자열 => 날짜형 
SELECT CAST('2020-12-12' AS DATE) AS DATE;
SELECT CAST('2019-12-25 12:12:12' AS DATETIME);
SELECT CAST('12:12:12' AS TIME) AS TIME;

-- 현재 시간과 날짜 출력 
-- now() : 내장함수로 현재의 날짜와 시간을 표시 
SELECT now();
SELECT CAST(now() AS DATE) AS '오늘 날짜';
SELECT CAST(now() AS TIME) AS '등록 시간';

SELECT 	now(), 
		CAST(now() AS DATE) AS '등록 날짜', 
		CAST(now() AS TIME) AS '등록 시간';


-- 여러 문자열을 하나의 문자열로 표시 p241
-- CONCAT(EXP...) : 문자열을 함께 출력할 때 사용 
-- CONCAT_WS(구분자, 문자열1, 문자열2 ...) : 문자열을 구분자와 함께 표시 

SET @userName = '슈가';
SELECT CONCAT('거기 누구 없소... ', '-- 이하이' ) AS '결과';
SELECT CONCAT('거기 누구 없소... ', @userName ) AS '결과';
SELECT 
	CONCAT_WS(' / ', '방탄소년단','블랙핑크','레드벨벳') 
	AS '아이돌 그룹';

-- 보기 좋은 출력 : p238
-- 단가  X  수량 = 입금액 

-- 적용전 -- 
SELECT * FROM buyTbl;

SELECT 
	num , price AS '가격', 
    amount AS '수량', 
    price*amount AS '구매액' -- 새로 추가된 컬럼명 
	FROM buyTbl 
	LIMIT 5;
-- CONCAT()이용해서 하나의 컬럼에 2개의 컬럼값 표시 
SELECT 	num, 
		CONCAT(	CAST(price AS CHAR(7)), ' X ', 
				CAST(amount AS CHAR(7)) ,' = ' )  
			AS '단가X수량',
		price*amount AS '구매액' 
		FROM buyTbl ;

/* 퀴즈 - CONCAT() 활용 
 usertbl 테이블에서 키가 175 넘는 레코드만 추출한 후 아래와 같은 형태로 출력하여라.  
        이름          키   
 가수이름 => 김경호   ?  cm
 가수이름 => 이승기   ?  cm 
 
 */
 