SELECT HOUR(a.reservation_time) as time, COUNT(r.id) as cnt
FROM available_time a
LEFT JOIN reservation r 
ON a.repair_shop_id = r.repair_shop_id
	AND (
		(DATE(a.reservation_date) = DATE(r.departure_time) AND TIME(a.reservation_time) = TIME(r.departure_time))
			OR
		(DATE(a.reservation_date) = DATE(r.arrival_time) AND TIME(a.reservation_time) = TIME(r.arrival_time))
	)
WHERE a.repair_shop_id = 1 AND a.reservation_date = '2014-03-15'
GROUP BY a.reservation_time
ORDER BY a.reservation_time;