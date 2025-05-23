### **Problem 511: Game Play Analysis I*

-- Select player_id and their first login date
select player_id, min(event_date) as first_login
from activity 
group by player_id
