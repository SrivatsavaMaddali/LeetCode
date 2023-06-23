# Write your MySQL query statement below
# select name from Employee
# where id in (
#     select managerId 
#     from (
#     select managerId, count(id) as cnt
# from Employee
#     group by managerId ) as a
#     where a.cnt>=5
# )
Select Name from Employee where Id in
(
    Select ManagerId from Employee 
    group by ManagerId having count(*) >= 5
)