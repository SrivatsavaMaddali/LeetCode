SELECT ROUND(t1.cnt1 / t2.cnt2, 2) AS fraction
FROM
  (SELECT COUNT(distinct a1.player_id) AS cnt1
  FROM Activity a1
  JOIN Activity a2 ON a1.player_id = a2.player_id
  WHERE DATEDIFF(a2.event_date, a1.event_date) = 1
  #players with diff in login dates=1
   and 
  (a1.player_id,a1.event_date) IN
   (select player_id,min(event_date)
     from Activity
     group by player_id)) t1 #and the first date is the first login of the player
     
  ,(SELECT COUNT(DISTINCT player_id) AS cnt2
  FROM Activity) t2; #This query is to count the number of players
