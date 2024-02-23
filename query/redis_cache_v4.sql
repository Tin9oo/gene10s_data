select HOUR(a.reservation_time) as res_time, COUNT(r.id) as cnt
FROM available_time a
	inner join reservation r
		ON a.repair_shop_id = r.repair_shop_id
WHERE a.repair_shop_id = 1 AND a.reservation_date = '2014-03-15'
GROUP BY res_time
ORDER BY res_time;

(
	select HOUR(a.reservation_time) as res_time, COUNT(r.id) as cnt
	FROM available_time a
	inner join reservation r
	ON a.repair_shop_id = r.repair_shop_id
	WHERE a.repair_shop_id = 1 AND a.reservation_date = '2024-02-24'
	GROUP BY res_time
	ORDER BY res_time
)
union
(
	select hour(a.reservation_time) as res_time, 0 as cnt
	from available_time a
    group by res_time
	order by res_time
);

select distinct hour(a.reservation_time) as res_time, 0 as cnt
	from available_time a
	order by res_time;
    
select hour(a.reservation_time) as res_time, 0 as cnt
	from available_time a
    group by res_time
	order by res_time;
    
    