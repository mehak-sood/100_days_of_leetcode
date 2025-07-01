-- CTE to find users whose first session was of type 'viewer'
with cte as (
    select user_id 
    from (
        select user_id, session_type, session_id,
               row_number() over(partition by user_id order by session_start asc) as rnk
        from twitch_sessions
    ) a
    where rnk = 1 and session_type = 'viewer'
)

-- Count the number of 'streamer' sessions for those users
select cte.user_id, count(t.session_id) as n_cnt
from cte
left join twitch_sessions t
  on cte.user_id = t.user_id
  and t.session_type = 'streamer'  -- Only count streamer sessions
group by 1
order by 2 desc, 1 asc;  -- Order by streamer session count desc, then user_id asc
