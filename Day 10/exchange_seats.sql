### **Problem 626: Exchange Seats**

-- Swap seat IDs in pairs; last seat remains unchanged if odd number of rows
select 
    (case 
        when id % 2 = 0 then id - 1                       -- Even ID: swap with previous
        when id % 2 != 0 and id = (select max(id) from seat) then id  -- Last odd ID: no swap
        else id + 1                                       -- Odd ID: swap with next
     end) as id,
    student
from seat
order by 1 asc;  -- Order by new swapped ID
