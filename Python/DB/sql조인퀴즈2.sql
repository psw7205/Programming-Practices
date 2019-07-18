use employees;


-- 1. 현재 근무 중인 직원 정보를 출력하시오.
-- 현재 근무 중은? to_date='9999-01-01'
-- Step1 : employees 테이블과 dept_emp 테이블 조인 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  이름   성   성별   입사일(hire_date)  현재 근무중 
  ?      ?    ?    ?           ?          9999-01-01 
*/

SELECT * from employees limit 5;
SELECT * from dept_emp limit 5;


 
 
-- 2. 현재 근무 중인 직원의 모든 정보(수행업무 포함) 를 출력하시오.
-- 현재 근무 중은? to_date='9999-01-01'
-- Step1 : employees 테이블과 title 테이블 조인 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  이름   성   성별   직무(title)  현재 근무중 
  ?      ?    ?    ?          ?     9999-01-01 
*/


-- 3. 현재 근무 중인 부서명를 출력하시오. (사원번호, 사원명, 부서코드, 부서명)
-- 3개의 테이블 조인 
-- Step1 : dept_emp , employees, departments 테이블에서 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  사원명  부서코드(dept_no)  부서명(dept_name)  현재 근무중 
  ?      ?        ?               ?             9999-01-01 

*/


-- 4. 가장오래 근무한 직원 10명의 현재 부서를 출력하시오.
-- 3개의 테이블 조인 
-- Step1 : dept_emp , employees, departments 테이블에서 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
-- Step3 : ORDER BY hire_date 정렬 옵션과 LIMIT 10 출력레코드 수 추가 

/*
사원번호  사원명  부서명(dept_name)  입사일(hire_date)
  ?      ?        ?               ?             

*/


-- 5. 부서별로 직원 수를 구하되 부서 이름이 나오게 출력하시오.
-- 2개의 테이블 조인 
-- Step1 : dept_emp , departments 테이블 조인
--		   SELECT는 dept_name, count(*) 이용
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
-- Step3 : GROUP_BY dept_name 그룹이름별로 갯수 생성 추가 
-- Step4 : ORDER BY count(*) desc => 직원수가 많은 부서부터 출력 

/*
사부서명(dept_name)  직원수(count(*))
   ?                   ?             
*/




-- 6. 부서별, 성별 직원 수를 구하시오




-- 7. 급여 평균이 가장 높은 부서 5개를 출력하시오. 




-- 8. 급여 평균이 가장 높은 부서를 제외하고, 급여 평균이 높은 부서를 5개를 출력하시오. 




-- 9. 급여를 많이 받는 부서장 리스트를 출력하시오



 
-- 10. 개발부(Development)에서 급여를 가장 많이 받는 직원 5명을 출력하시오.

