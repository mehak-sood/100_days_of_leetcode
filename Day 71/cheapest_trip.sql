-- Create a view for one-stop flights
with one_stop as (
    select distinct 
        o.origin,  -- Starting airport
        s1.destination,  -- Final destination after one stop
        (o.cost + s1.cost) as trip_cost  -- Total cost via the intermediate stop
    from da_flights o 
    join da_flights s1
        on o.destination = s1.origin  -- Ensure flight connection matches
),

-- Create a view for two-stop flights
two_stops as (
    select distinct 
        o.origin,  -- Original start
        o.destination as stop1,  -- First stop
        s1.destination as stop2,  -- Second stop
        s2.destination as destination,  -- Final destination
        (o.cost + s1.cost + s2.cost) as trip_cost  -- Total cost of the 3-leg journey
    from da_flights o 
    join da_flights s1
        on o.destination = s1.origin
    join da_flights s2
        on s1.destination = s2.origin
),

-- Combine direct, one-stop, and two-stop flights into a unified list
all_flights as (
    (
        select origin, destination, cost as trip_cost
        from da_flights  -- Direct flights
    )
    union
    (
        select * from one_stop  -- One-stop flights
    )
    union
    (
        select origin, destination, trip_cost from two_stops  -- Two-stop flights
    )
)

-- Select the cheapest option for each origin-destination pair
select 
    origin, 
    destination, 
    min(trip_cost) as cheapest_flight  -- Minimum cost among all possible routes
from all_flights
group by 1, 2;
