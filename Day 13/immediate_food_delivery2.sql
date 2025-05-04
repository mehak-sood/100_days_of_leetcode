### **Problem 1174: Immediate Food Delivery II**

-- Calculate the percentage of customers who received delivery on their preferred date for their first order
with first_orders as (
    select customer_id, min(order_date) as first_order  -- Get first order date per customer
    from delivery
    group by 1
)

select 
    ifnull(
        round(
            sum(
                case when order_date = customer_pref_delivery_date then 1 else 0 end  -- Count if delivery matched preferred date
            ) / (select count(*) from first_orders) * 100,  -- Divide by total first orders
            2
        ), 0
    ) as immediate_percentage
from delivery d
join first_orders o
on d.customer_id = o.customer_id
and d.order_date = o.first_order;  -- Match only the first order rows
