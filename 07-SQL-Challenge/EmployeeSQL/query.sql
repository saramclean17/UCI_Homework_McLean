--1) List employee number, last name, first name, sex, and salary of each employee
SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
FROM employees AS e
JOIN salaries AS s ON e.emp_no=s.emp_no;


--2) List employees who were hired in 1986.
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';

--3)List manager info: department number, department name, the manager's employee number, last name, first name.
SELECT m.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name
FROM dept_manager AS m
JOIN employees AS e ON m.emp_no=e.emp_no
	JOIN dept_emp ON dept_emp.emp_no=e.emp_no
	JOIN departments AS d ON d.dept_no=m.dept_no;


--4)List employee department information: employee number, last name, first name, and department name.
CREATE VIEW emp_info AS --Create view to use for steps 6 & 7
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees AS e
JOIN dept_emp ON e.emp_no=dept_emp.emp_no
	JOIN departments AS d ON dept_emp.dept_no=d.dept_no;
	
--5)List all employees whose first name is "Hercules" and last names begin with "B."
SELECT first_name, last_name
FROM employees
WHERE first_name='Hercules' AND last_name LIKE 'B%';


--6)List all employees in the Sales department, including their employee number, 
--last name, first name, and department name.
SELECT emp_no, last_name, first_name, dept_name
FROM emp_info
WHERE dept_name = 'Sales';

--7)List all employees in the Sales and Development departments,
--including their employee number, last name, first name, and department name.
SELECT emp_no, last_name, first_name, dept_name
FROM emp_info
WHERE dept_name IN ('Sales', 'Development');


--8)In descending order, list the frequency count of employee last names.
SELECT last_name, COUNT(last_name) AS name_ct
FROM employees
GROUP BY last_name
ORDER BY name_ct DESC;