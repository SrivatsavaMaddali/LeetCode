Select Name from Employee where Id in
(
    Select ManagerId from Employee 
    group by ManagerId having count(*) >= 5
)
#takes some more time​
