SELECT * FROM GENE10S.reservation;

SELECT r.id, r.departure_time, r.arrival_time, r.progress_stage
FROM  reservation r
INNER JOIN customer c ON r.customer_id = c.id;