-- Step 1: Create CTE to rank videos by number of user flags
with cte as (
    select 
        video_id, 
        dense_rank() over(order by count(flag_id) desc) as rnk
    from user_flags
    group by video_id
)

-- Step 2: Select all flags for the most flagged video(s)
select 
    video_id, 
    count(b.flag_id) as yt_reviewed  -- count of flags that were reviewed by YouTube
from (
    select * 
    from user_flags
    where video_id in (
        select video_id 
        from cte 
        where rnk = 1  -- only most-flagged video(s)
    )
) a
left join (
    select flag_id 
    from flag_review
    where reviewed_by_yt = 1  -- only flags reviewed by YouTube
) b 
on a.flag_id = b.flag_id
group by video_id;
