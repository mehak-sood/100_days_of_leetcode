### **Problem 1683: Invalid Tweets**

-- Select tweet IDs where the tweet content is longer than 15 characters
select tweet_id 
from tweets
where length(content) > 15;
