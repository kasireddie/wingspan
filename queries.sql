-- Query (a)

select * from bird 
order by wingspan, 
(select token from food where food.food_id = main_food_id), 
(select token from habitat where habitat.habitat_id = main_habitat_id) desc 
limit 3;

-- Query (b)

select * from bird b1 where 
(select count(*) from bird b2 where b1.bird_name = b2.bird_name) > 1;

-- Query (c)

select * from points;