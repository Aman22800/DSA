# Write your MySQL query statement below
with cte as
(select *, dense_rank() over(partition by departmentid order by salary desc) r
from employee)

select d.name as Department , c.name as Employee , c.salary as Salary
from cte c
right join department d
on c.departmentid=d.id
where r<=3
