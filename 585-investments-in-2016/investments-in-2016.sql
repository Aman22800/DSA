# Write your MySQL query statement below
#part 1
-- select tiv_2015
-- from insurance
-- group by tiv_2015
-- having count(*)>1

#part 2
-- select lat,lon
-- from insurance
-- group by lat,lon
-- having count(*)>1

select round(sum(tiv_2016),2) as tiv_2016
from insurance
where tiv_2015 in (
    select tiv_2015
    from insurance
    group by tiv_2015
    having count(*)>1
) 
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1)
