# Write your MySQL query statement below
select max(salary) as SecondHighestsalary
from employee
where salary<(select max(salary) from employee)