-- 조인이란?
-- 두개이상의 테이블을 서로 묶어서 관리하는 기능 
-- 조인의 종류 
-- 내부 조인 
-- 외부 조인 
-- 크로스 조인 
-- 셀프 조인 

USE sqldb;

-- 테이블 구조 확인 
-- 외래키 확인 
-- buytbl에서 외래키가 userID인지  확인 
-- 외래키는 Key값이 MUL로 표시 
DESC usertbl;
DESC buytbl;

-- 2개의 테이블 조인 

-- INNER JOIN 1 --
-- SELECT * 또는 컬럼명 
--    FROM 테이블1
--      INNER JOIN 테이블2
--         ON 조인될조건-테이블1.컬럼명 = 테이블2.컬럼명 이용 
--				(서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];

-- 구매 경험이 있는 모든 레코드가 출력 
-- 구매 경험이 없는 레코드는 표시되지 않는다. => 아우터조인으로 해결 
-- userID 컬럼명이 2번 표시 
-- 왼쪽이 buyTbl, 오른쪽이 userTbl
SELECT * 
   FROM buyTbl
     INNER JOIN userTbl
        ON buyTbl.userID = userTbl.userID;

-- JYP 회원의  레코드 정보만 출력
SELECT * 
   FROM buyTbl
     INNER JOIN userTbl
        ON buyTbl.userID = userTbl.userID
		WHERE buyTbl.userID = 'JYP';

-- 명확하게 컬럼명 표시하기 
-- 테이블명.컬럼명으로 나열 
-- userID, prodName, amount, name, addr
SELECT 
  buyTbl.userID AS '아이디', buyTbl.prodName AS '상품명', 
  buyTbl.amount AS '수량',
  userTbl.name AS '이름', userTbl.addr AS '지역'
   FROM buyTbl
     INNER JOIN userTbl
        ON buyTbl.userID = userTbl.userID;

-- 테이블명에 별칭 지정하기 
-- INNER JOIN 2 --
-- SELECT * 또는 별칭.컬럼명 
--    FROM 테이블1 테이블별칭1
--      INNER JOIN 테이블2 테이블별칭2
--         ON 조인될조건-별칭1.컬럼명 = 별칭2.컬럼명 이용 
--				(서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];

SELECT 
  B.userID AS '아이디', B.prodName AS '상품명', 
  B.amount AS '수량',
  U.name AS '이름', U.addr AS '지역'
   FROM buyTbl B
     INNER JOIN userTbl U
        ON B.userID = U.userID;

-- 퀴즈 
-- 아래와 같이 2개의 테이블(usertbl, buytbl)을 조인한 후  
-- 표시되게 만들어 보세요 
/*
구매금액 = 수량*가격 

아이디  이름   지역   상품명   수량   가격   구매금액
  ?    ?      ?     ?      ?     ?       ?
 */

-- FORMAT(수식이나값, 소숫점자리수)
-- 3자리마다 콤마(,) 표시 

SELECT 
  B.userID AS '아이디', U.name AS '이름', U.addr AS '지역',
  B.prodName AS '상품명',   B.amount AS '수량',
  B.price AS '가격', format(B.amount * B.price, 0) AS '구매금액'  
   FROM buyTbl B
     INNER JOIN userTbl U
        ON B.userID = U.userID;

-- 3개의 테이블 조인하기 p270

-- DB 접속과 3개의 테이블 생성 
-- 학생(stdTbl), 학생동아리(stdclubTbl), 동아리(clubTbl)
USE sqlDB;

-- 학생(stdTbl) 테이블 생성 - 이름, 지역 
DROP TABLE IF EXISTS stdTbl;
CREATE TABLE stdTbl 
( stdName  VARCHAR(10) NOT NULL PRIMARY KEY,
  addr	  CHAR(4) NOT NULL
);
      
DESC stdTbl;

-- 동아리(clubTbl) 테이블 생성
-- 동아리명(clubName)과 동아리방(roomNo) 
DROP TABLE IF EXISTS clubTbl;
CREATE TABLE clubTbl 
( clubName  VARCHAR(10) NOT NULL PRIMARY KEY,
  roomNo    CHAR(4) NOT NULL
);

DESC clubTbl;

-- 학생동아리(stdclubTbl) 테이블 생성 
-- 외래키 2개 설정 
-- FOREIGN KEY(컬럼명) REFERENCES 외부테이블명(컬럼명)
DROP TABLE IF EXISTS stdclubTbl;
CREATE TABLE stdclubTbl
(  num int AUTO_INCREMENT NOT NULL PRIMARY KEY, 
   stdName    VARCHAR(10) NOT NULL,
   clubName    VARCHAR(10) NOT NULL,
FOREIGN KEY(stdName) REFERENCES stdTbl(stdName),
FOREIGN KEY(clubName) REFERENCES clubTbl(clubName)
);
DESC stdclubTbl;

-- 데이타 입력 후 테이블 확인 
INSERT INTO stdTbl 
	VALUES 
		('김범수','경남'), ('성시경','서울'), ('조용필','경기'), 
        ('은지원','경북'),('바비킴','서울');
        
INSERT INTO clubTbl 
	VALUES 
		('수영','101호'), ('바둑','102호'), 
		('축구','103호'), ('봉사','104호');
    
INSERT INTO stdclubTbl 
	VALUES 
		(NULL, '김범수','바둑'), (NULL,'김범수','축구'), 
        (NULL,'조용필','축구'), (NULL,'은지원','축구'), 
        (NULL,'은지원','봉사'), (NULL,'바비킴','봉사');

SELECT count(*) FROM stdTbl; -- 5
SELECT count(*) FROM clubTbl; -- 4
SELECT count(*) FROM stdclubTbl; -- 6




