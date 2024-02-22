SELECT * FROM GENE10S.car;

explain select *
from car c
join car_image i
	on c.sell_name = i.sell_name
where customer_id = 9;