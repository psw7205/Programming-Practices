-- 스토어드 프로시저 (Stored Procedure) p415
-- 쿼리문의 집합. 함수와 비슷 
-- 스토어드 프로시저 기본 템플릿 정의 
/*
-- 이미 등록되어 있으면 삭제 : 초기화 
DROP PROCEDURE IF EXISTS 스토어드프로시저이름; 

DELIMITER $$  -- 시작 
CREATE PROCEDURE 프로시저이름()
BEGIN
-- SQL 프로그래밍 (IF, CASE, WHILE..)
END $$
DELIMITER; -- 끝 
*/

-- 프로시저 호출 명령 
/* CALL 프로시저이름(); */

-- 스토어드 프로시저 테스트 1
-- 변수를 선언하고 출력한다. 
DROP PROCEDURE IF EXISTS varTest; 

DELIMITER $$
	CREATE PROCEDURE varTest()
		BEGIN
        /*
			DECLARE deco text;
			SET deco = '** 출력 **';
			SELECT deco;
		*/
			SET @deco  = '** 출력 **';
			SELECT @deco;
		END $$
DELIMITER;

CALL varTest();

--  userID, name, addr FROM usertbl

-- 스토어드 프로시저 테스트 2 - select
DROP PROCEDURE IF EXISTS selectTest; 
DELIMITER $$
CREATE PROCEDURE selectTest()
	BEGIN
		SELECT userID AS 아이디, name AS 이름, addr AS 지역 
			FROM usertbl;
	END $$
DELIMITER;

CALL selectTest();

-- **********
-- 매개변수 
-- CREATE PROCEDURE 프로시저이름(	IN 매개변수이름1 자료형 ,
								IN 매개변수이름2 자료형) 

-- 프로시저 호출시 
-- CALL 프로시저이름(매개변수값1, 매개변수값2);
-- -----------
-- 스토어드 프로시저 테스트 3 - 매개변수 
DROP PROCEDURE IF EXISTS paraTest1; 

DELIMITER $$
CREATE PROCEDURE paraTest1(IN num INT(10))
BEGIN
	SELECT concat('입력값 = ' , num) AS '결과';
END $$
DELIMITER;

CALL paraTest1(100);

-- 스토어드 프로시저 테스트 - 2개의 매개변수 전달과 출력 
DROP PROCEDURE IF EXISTS paraTest2; 

DELIMITER $$
	CREATE PROCEDURE paraTest2(IN msg TEXT, IN userName CHAR(10))
		BEGIN
			SELECT concat(userName, ' 님, 화이팅!!! ' , msg ) 
            AS '메세지 출력';
		END $$
DELIMITER ;

CALL paraTest2('오늘도 좋은 하루', '홍길동');



-- **********
-- 스토어드 프로시저 테스트 - 제어문 
--  p283
-- 조건에 따라 분기 
/*
  IF 조건식 THEN 
	명령문1
  ELSE
    명령문2
  END IF;
*/  
DROP PROCEDURE IF EXISTS ifProc; 
DELIMITER $$
	CREATE PROCEDURE ifProc()
	BEGIN
	  DECLARE var1 INT;  
	  SET var1 = 20; 
      
	  IF var1 = 100 THEN 
		SELECT '100입니다.';
	  ELSE
		SELECT '100이 아닙니다.';
	  END IF;
	END $$
DELIMITER ;
CALL ifProc();

-- 매개변수에 따라서 다른 메세지 출력하기  --
/**
CALL ifProc2(20) => 100이 아닙니다.
CALL ifProc2(100) => 100입니다.
*/

DROP PROCEDURE IF EXISTS ifProc2; 
DELIMITER $$
	CREATE PROCEDURE ifProc2(IN myNum INT)
	BEGIN
	  IF myNum = 100 THEN 
		SELECT '100입니다.';
	  ELSE
		SELECT '100이 아닙니다.';
	  END IF;
	END $$
DELIMITER ;
CALL ifProc2(100);

-- 조건에 따라 분기 2
/*
  IF 조건식 THEN 
	명령문1
  ELSEIF 조건식 THEN 
	명령문2  
  ELSE
    명령문30718
  END IF;
*/ 
-- p286 


-- 다중 IF 1
DROP PROCEDURE IF EXISTS ifProc77; 
DELIMITER $$
CREATE PROCEDURE ifProc77()
BEGIN
    DECLARE point INT ;
    DECLARE credit CHAR(1);
    SET point = 77 ;
    
    IF point >= 90 THEN
		SET credit = 'A';
    ELSEIF point >= 80 THEN
		SET credit = 'B';
    ELSEIF point >= 70 THEN
		SET credit = 'C';
    ELSEIF point >= 60 THEN
		SET credit = 'D';
    ELSE
		SET credit = 'F';
    END IF;
    SELECT CONCAT('취득점수==>', point), CONCAT('학점==>', credit);
END $$
DELIMITER ;
CALL ifProc77();


-- 다중 IF 2

-- POint 전달값에 따라서 다른 메세지 출력하기  --
/**
CALL ifProc_para(95) => A
CALL ifProc_para(55) => F
*/

DROP PROCEDURE IF EXISTS ifProc_para;
 
DELIMITER $$
CREATE PROCEDURE ifProc_para(IN point INT)
BEGIN
    DECLARE credit CHAR(1);
    
    IF point >= 90 THEN
		SET credit = 'A';
    ELSEIF point >= 80 THEN
		SET credit = 'B';
    ELSEIF point >= 70 THEN
		SET credit = 'C';
    ELSEIF point >= 60 THEN
		SET credit = 'D';
    ELSE
		SET credit = 'F';
    END IF;
    
    SELECT CONCAT('  취득점수==>  ', point , '  학점==>  ', credit) 
			AS ' ***  성적표 ****';	
END $$
DELIMITER ;

CALL ifProc_para(90);
CALL ifProc_para(55);



-- ********************
/*
CASE 
		WHEN 조건식1 THEN
			명령문1;
		WHEN 조건식2 THEN
			명령문2;
            
		ELSE
			명령문3;
END CASE;
*/

DROP PROCEDURE IF EXISTS caseProc; 
DELIMITER $$
CREATE PROCEDURE caseProc()
BEGIN
    DECLARE point INT ;
    DECLARE credit CHAR(1);
    SET point = 77 ;
    CASE 
		WHEN point >= 90 THEN
			SET credit = 'A';
		WHEN point >= 80 THEN
			SET credit = 'B';
		WHEN point >= 70 THEN
			SET credit = 'C';
		WHEN point >= 60 THEN
			SET credit = 'D';
		ELSE
			SET credit = 'F';
    END CASE;
    SELECT CONCAT('취득점수==>', point), CONCAT('학점==>', credit);
END $$
DELIMITER ;
CALL caseProc();


DROP PROCEDURE IF EXISTS caseProc2; 
DELIMITER $$
CREATE PROCEDURE caseProc2(IN point INT)
BEGIN
    DECLARE credit CHAR(1);
    CASE 
		WHEN point >= 90 THEN
			SET credit = 'A';
		WHEN point >= 80 THEN
			SET credit = 'B';
		WHEN point >= 70 THEN
			SET credit = 'C';
		WHEN point >= 60 THEN
			SET credit = 'D';
		ELSE
			SET credit = 'F';
    END CASE;
    SELECT CONCAT('취득점수==> ', point , ' 학점==> ', credit);
END $$
DELIMITER ;
CALL caseProc2(77);


-- 사칙연산 -- case 활용 
-- CALL caseProc3(10,20,'+');
-- 10 + 20 = ?

-- CALL caseProc3(10,20,'*');
-- 10 * 20 = ?
 
 -- CALL caseProc3(10,20,'#'); -- 연산이 안되는 경우 
-- 10 # 20 = -99999
 
 
DROP PROCEDURE IF EXISTS caseProc3; 
DELIMITER $$
CREATE PROCEDURE caseProc3(IN num1 INT, IN num2 INT, IN choice CHAR(1))
BEGIN
    DECLARE result INT ;
    CASE 
		WHEN choice = '+' THEN
			SET result = num1 + num2;
		WHEN choice = '*' THEN
			SET result = num1 * num2;
		WHEN choice = '-' THEN
			SET result = num1 - num2;
		WHEN choice = '/' THEN
			SET result = num1 / num2;            
		ELSE
			SET result = NULL;
    END CASE;
    
    SELECT CONCAT(num1, choice, num2, ' = ', result) AS ' = 사칙연산 =';
END $$
DELIMITER ;

CALL caseProc3(10,20,'+');
CALL caseProc3(10,20,'#');

-- 반복문 WHILE
-- WHILE (조건식) DO
-- 		명령문
-- END WHILE;    
    
-- 1에서 100까지 구하기 
DROP PROCEDURE IF EXISTS whileProc1; 
DELIMITER $$
CREATE PROCEDURE whileProc1()
BEGIN
	DECLARE i INT; -- 1에서 100까지 증가할 변수
	DECLARE hap INT; -- 더한 값을 누적할 변수
    SET i = 1;
    SET hap = 0;
	WHILE (i <= 100) DO
		SET hap = hap + i;  
		SET i = i + 1;     
	END WHILE;
	SELECT hap;   
END $$
DELIMITER ;
CALL whileProc1();

-- ----------------
DROP PROCEDURE IF EXISTS whileProc0; 
DELIMITER $$
CREATE PROCEDURE whileProc0(IN n INT)
BEGIN
	DECLARE i INT; -- 1에서 100까지 증가할 변수-- 
	DECLARE hap INT; -- 더한 값을 누적할 변수
    SET i = 1;
    SET hap = 0;

	WHILE (i <= n) DO
		SET hap = hap + i;  -- hap의 원래의 값에 i를 더해서 다시 hap에 넣으라는 의미
		SET i = i + 1;      -- i의 원래의 값에 1을 더해서 다시 i에 넣으라는 의미
	END WHILE;
	SELECT concat(n, ' 까지의 합 = ', hap) ;   
END $$
DELIMITER ;
CALL whileProc0(10);


-- ITERATE
DROP PROCEDURE IF EXISTS whileProc2; 
DELIMITER $$
CREATE PROCEDURE whileProc2()
BEGIN
    DECLARE i INT; -- 1에서 100까지 증가할 변수
    DECLARE hap INT; -- 더한 값을 누적할 변수
    SET i = 1;
    SET hap = 0;

    myWhile: WHILE (i <= 100) DO  -- While문에 label을 지정
	IF (i%7 = 0) THEN
		SET i = i + 1;     
		ITERATE myWhile; -- 지정한 label문으로 가서 계속 진행
	END IF;
        
        SET hap = hap + i; 
        IF (hap > 1000) THEN 
		LEAVE myWhile; -- 지정한 label문을 떠남. 즉, While 종료.
	END IF;
        SET i = i + 1;
    END WHILE;

    SELECT hap;   
END $$
DELIMITER ;
CALL whileProc2();

-- 테이블에 활용 
DROP PROCEDURE IF EXISTS whileProc3; 
DELIMITER $$
CREATE PROCEDURE whileProc3(IN userName VARCHAR(10))
	BEGIN
		SELECT * FROM usertbl WHERE name = userName;	
	END $$
DELIMITER ;

CALL whileProc3('이승기');

SELECT * FROM usertbl;
desc userTbl;



