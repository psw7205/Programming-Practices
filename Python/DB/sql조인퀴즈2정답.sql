use employees;

SELECT * from employees limit 5;
SELECT * from dept_emp limit 5;
SELECT * from titles limit 5;

-- 1. 현재 근무 중인 직원 정보를 출력하시오.
-- 현재 근무 중은? to_date='9999-01-01'
-- Step1 : employees 테이블과 dept_emp 테이블 조인 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  이름   성   성별   입사일(hire_date)  현재 근무중 
  ?      ?    ?    ?           ?          9999-01-01 
*/

SELECT E.EMP_NO AS '사원번호', 
	   concat(E.first_name,'  ', E.last_name) AS '사원 이름',
       E.gender AS '성별',
       E.hire_date AS '입사일',
       DE.TO_DATE AS '현재근무중'
  FROM EMPLOYEES E
       INNER JOIN DEPT_EMP DE 
       ON DE.EMP_NO=E.EMP_NO
 WHERE DE.TO_DATE = '9999-01-01'
 LIMIT 10;
 
 
 
-- 2. 현재 근무 중인 직원의 모든 정보(수행업무 포함) 를 출력하시오.
-- 현재 근무 중은? to_date='9999-01-01'
-- Step1 : employees 테이블과 title 테이블 조인 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  이름   성   성별   직무(title)  현재 근무중 
  ?      ?    ?    ?          ?     9999-01-01 
*/

SELECT E.emp_no, E.first_name, E.last_name, T.TITLE, T.TO_DATE
  FROM EMPLOYEES E
        INNER JOIN TITLES T 
        ON T.EMP_NO = E.EMP_NO
 WHERE T.TO_DATE = '9999-01-01'
 LIMIT 10;

-- 3. 현재 근무 중인 부서명를 출력하시오. (사원번호, 사원명, 부서코드, 부서명)
-- 3개의 테이블 조인 
-- Step1 : dept_emp , employees, departments 테이블에서 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  사원명  부서코드(dept_no)  부서명(dept_name)  현재 근무중 
  ?      ?        ?               ?             9999-01-01 

*/

SELECT E.EMP_NO, E.FIRST_NAME, 
		D.DEPT_NO, D.DEPT_NAME, DE.TO_DATE
  FROM DEPT_EMP DE
       INNER JOIN EMPLOYEES E ON E.EMP_NO=DE.EMP_NO
	   INNER JOIN DEPARTMENTS D ON D.DEPT_NO=DE.DEPT_NO
WHERE DE.TO_DATE = '9999-01-01';


-- 4. 가장오래 근무한 직원 10명의 현재 부서를 출력하시오.
-- 3개의 테이블 조인 
-- Step1 : dept_emp , employees, departments 테이블에서 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
-- Step3 : ORDER BY hire_date 정렬 옵션과 LIMIT 10 출력레코드 수 추가 

/*
사원번호  사원명  부서명(dept_name)  입사일(hire_date)
  ?      ?        ?               ?             

*/
SELECT E.EMP_NO, E.FIRST_NAME, E.LAST_NAME, D.DEPT_NAME, E.HIRE_DATE
  FROM DEPT_EMP DE
	  INNER JOIN EMPLOYEES E ON E.EMP_NO=DE.EMP_NO
	  INNER JOIN DEPARTMENTS D ON D.DEPT_NO=DE.DEPT_NO
 WHERE DE.TO_DATE = '9999-01-01'  
 ORDER BY HIRE_DATE, E.FIRST_NAME 
 LIMIT 10 ;

-- 5. 부서별로 직원 수를 구하되 부서 이름이 나오게 출력하시오.
-- 2개의 테이블 조인 
-- Step1 : dept_emp , departments 테이블 조인
--		   SELECT는 dept_name, count(*) 이용
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
-- Step3 : GROUP_BY dept_name 그룹이름별로 갯수 생성 추가 
-- Step4 : ORDER BY count(*) desc => 직원수가 많은 부서부터 출력 

/* 직원수가 가장 많은 순서 -> 가장 적은 순서로 정렬 
부서명(dept_name)  직원수(count(*))
   ?                   ?             
*/
SELECT DEPT_NAME, COUNT(*) 
  FROM DEPT_EMP DE
		INNER JOIN DEPARTMENTS D 
        ON D.DEPT_NO=DE.DEPT_NO
 WHERE DE.TO_DATE='9999-01-01'  
 GROUP BY DEPT_NAME
 ORDER BY COUNT(*) DESC;

-- 6. 부서별, 성별 직원 수를 구하시오
-- 3개의 테이블 조인 
-- Step1 : dept_emp , departments, EMPLOYEES 테이블 조인
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
-- Step3 : GROUP_BY 로 dept_name, gender 그룹핑 
-- Step4 : ORDER BY 부서명, 성별 

SELECT D.DEPT_NAME, E.GENDER, COUNT(*) 
  FROM DEPT_EMP DE
		INNER JOIN DEPARTMENTS D ON D.DEPT_NO=DE.DEPT_NO
		INNER JOIN EMPLOYEES E ON E.EMP_NO=DE.EMP_NO
 WHERE DE.TO_DATE='9999-01-01'  
 GROUP BY D.DEPT_NAME, E.GENDER
 ORDER BY D.DEPT_NAME, E.GENDER;
 
 

-- 7. 급여 평균이 가장 높은 부서 5개를 출력하시오. 
-- 3개의 테이블 조인 
-- Step1 : dept_emp , departments, SALARIES 테이블 조인
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
-- 		dept_emp.TO_DATE='9999-01-01' AND SALARIES.TO_DATE='9999-01-01'
-- Step3 : GROUP_BY 로 dept_name 그룹핑 
-- Step4 : ORDER BY AVG(SALARIES.SALARY) DESC
SELECT * FROM SALARIES LIMIT 3;

SELECT D.DEPT_NAME, AVG(SALARY) SA
  FROM DEPT_EMP DE
	  INNER JOIN DEPARTMENTS D ON D.DEPT_NO=DE.DEPT_NO
	  INNER JOIN SALARIES S ON S.EMP_NO=DE.EMP_NO
WHERE DE.TO_DATE='9999-01-01' AND S.TO_DATE='9999-01-01' 
GROUP BY D.DEPT_NAME
ORDER BY SA DESC
LIMIT 5;



-- 8. 급여 평균이 가장 높은 부서를 제외하고, 급여 평균이 높은 부서를 5개를 출력하시오. 

SELECT D.DEPT_NAME, AVG(SALARY) SA
  FROM DEPT_EMP DE
	  INNER JOIN DEPARTMENTS D ON D.DEPT_NO=DE.DEPT_NO
	  INNER JOIN SALARIES S ON S.EMP_NO=DE.EMP_NO
WHERE DE.TO_DATE='9999-01-01' AND S.TO_DATE='9999-01-01'  
GROUP BY D.DEPT_NAME
ORDER BY SA DESC
LIMIT 1, 5;  -- 2~6 등 


-- 9. 급여를 많이 받는 부서장 리스트를 출력하시오
SELECT * FROM DEPT_EMP LIMIT 5;
SELECT * FROM DEPT_MANAGER LIMIT 5;
SELECT * FROM SALARIES LIMIT 5;
SELECT * FROM EMPLOYEES LIMIT 5;

SELECT DM.EMP_NO, E.FIRST_NAME, E.LAST_NAME, S.SALARY
  FROM DEPT_MANAGER DM
	   INNER JOIN SALARIES S ON S.EMP_NO = DM.EMP_NO
	   INNER JOIN EMPLOYEES E ON E.EMP_NO = DM.EMP_NO
 WHERE S.TO_DATE = '9999-01-01'
 ORDER BY SALARY DESC;


-- 10. 개발부(Development)에서 급여를 가장 많이 받는 직원 5명을 출력하시오.
SELECT E.*, SALARY
  FROM DEPT_EMP DE
	   INNER JOIN EMPLOYEES E ON E.EMP_NO = DE.EMP_NO
	   INNER JOIN SALARIES S ON S.EMP_NO = DE.EMP_NO
 WHERE DE.TO_DATE = '9999-01-01' AND DEPT_NO='D005'
 ORDER BY SALARY DESC
 LIMIT 5;

