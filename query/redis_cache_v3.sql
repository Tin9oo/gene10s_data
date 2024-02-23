 SELECT HOUR(a.reservation_time) as time, COUNT(r.id) as cnt
FROM available_time a
LEFT JOIN reservation r 
ON a.repair_shop_id = r.repair_shop_id
    AND (
		(r.departure_time like concat(a.reservation_date, '%') AND
		r.departure_time like concat('%', a.reservation_time))
		OR
		(r.arrival_time like concat(a.reservation_date, '%') AND
		r.arrival_time like concat('%', a.reservation_time))
     )
WHERE a.repair_shop_id = 1 AND a.reservation_date = '2014-03-15'
GROUP BY HOUR(a.reservation_time)
ORDER BY HOUR(a.reservation_time);
