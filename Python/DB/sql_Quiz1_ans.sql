-- SQL 퀴즈
USE emplyees;
SELECT * FROM employees limit 5;
SELECT * FROM titles limit 5;
SELECT * FROM salaries limit 5;

-- 1. 직원 이름이 빠른 순(A, B, C …) 순으로 리스트를 출력하시오.
SELECT * 
  FROM EMPLOYEES
  ORDER BY FIRST_NAME, LAST_NAME;


-- 2. 직원 나이가 적은 순으로 출력하시오.
SELECT * 
	FROM EMPLOYEES 
	ORDER BY BIRTH_DATE DESC;


-- 3. 직원 중 나이가 가장 많은 사람의 나이는 몇 살 인가?
SELECT MIN(BIRTH_DATE) 
  FROM EMPLOYEES;

SELECT 	year(curdate()) , -- 현재년도 
		year(min(BIRTH_DATE)), -- 나이가많은 사람의 년도 
        year(curdate())-year(min(BIRTH_DATE)) 
  FROM EMPLOYEES;

-- TIMESTAMPDIFF(YEAR, 시간1, 시간2)
-- 시간2-시간1의 값을 년도로 표시   
SELECT TIMESTAMPDIFF(YEAR, MIN(BIRTH_DATE), NOW()) 
  FROM EMPLOYEES;


-- 4. 직원들의 업무(titles)에는 직원별로 업무가 저장되어 있다. 
-- 이 회사의 업무 종류 리스트를 구하시오.

SELECT DISTINCT TITLE 
  FROM TITLES;


-- 5. 이 회사의 업무 종류 개수를 구하시오.
SELECT COUNT(DISTINCT TITLE) 
  FROM TITLES;


-- 6. 가장 최근에 입사한 사람 100명만 출력하시오
SELECT * 
	FROM EMPLOYEES
	ORDER BY HIRE_DATE DESC 
	LIMIT 100;


-- 7. 급여가 가장 많은 사람 10명을 구하시오.
SELECT * 
	FROM SALARIES 
	ORDER BY SALARY DESC 
	LIMIT 10;


-- 8. 급여가 가장 많은 사람 10명을 제외하고 다음 10명을 구하시오.
--   즉, 11등부터 20등 까지…
-- LIMIT index-1, count

SELECT * 
	FROM SALARIES 
	ORDER BY SALARY DESC 
	LIMIT 10, 10;


-- 9. 입사한지 가장 오래된 사람의 이름은 무엇인가?
SELECT first_name, last_name 
  FROM EMPLOYEES
  ORDER BY HIRE_DATE
  LIMIT 1;

-- 10. 1999년에 입사한 직원 리스트를 구하시오.
SELECT *
  FROM EMPLOYEES
  WHERE YEAR(HIRE_DATE)=1999;

-- 11. 1999년에 입사한 직원 중 여자 직원(GENDER='F') 리스트를 구하시오.
SELECT *
  FROM EMPLOYEES
  WHERE YEAR(HIRE_DATE)=1999 AND GENDER='F';


-- 12. 1998년에 입사한 직원 중 남자 직원(M)은 몇 명인가?
SELECT COUNT(*)
  FROM EMPLOYEES
  WHERE YEAR(HIRE_DATE)=1999 AND GENDER='M';


-- 13. 1998년이나 1999년에 입사한 직원의 수를 구하시오.
SELECT COUNT(*)
  FROM EMPLOYEES
  WHERE YEAR(HIRE_DATE)=1998 OR YEAR(HIRE_DATE)=1999;



-- 14. 1995년부터 1999년까지 입사한 직원의 수를 구하시오.
SELECT COUNT(*)
  FROM EMPLOYEES
  WHERE YEAR(HIRE_DATE) BETWEEN 1995 AND 1999;


-- 15. 성(last_name)이 Senzako, Pettis, Henseler인 직원을 출력하시오.
SELECT *
  FROM EMPLOYEES
  WHERE LAST_NAME IN ('Senzako', 'Pettis', 'Henseler');
