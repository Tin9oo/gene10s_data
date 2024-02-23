-- 조회
SELECT * FROM reservation limit 30;

select * from reservation where id = 1;

select count(*) from reservation;

explain analyze select
	departure_time, DATE(departure_time) AS 'DATE(departure_time)', TIME(departure_time) AS 'TIME(departure_time)',
	arrival_time, DATE(arrival_time) AS 'DATE(arrival_time)', TIME(arrival_time) AS 'TIME(arrival_time)'
from reservation;

select
	departure_time, DATE(departure_time) AS 'DATE(departure_time)', TIME(departure_time) AS 'TIME(departure_time)',
	arrival_time, DATE(arrival_time) AS 'DATE(arrival_time)', TIME(arrival_time) AS 'TIME(arrival_time)'
from reservation
where departure_time like '%-%';

select departure_time, count(*) as cnt from reservation
group by departure_time
order by cnt desc;


select departure_time, count(departure_time) from reservation group by departure_time;

-- 인덱스
create index reservation_departure_time_index
	on  reservation (departure_time);
    
drop index reservation_departure_time_index on reservation;
    
create index reservation_arrival_time_index
	on reservation (arrival_time);
    
drop index reservation_arrival_time_index on reservation;

create index reservation_departure_time_arrival_time_index
	on reservation(departure_time, arrival_time);
    
drop index reservation_departure_time_arrival_time_index on reservation;

alter table reservation
	add dep_date DATE as (DATE(departure_time)) virtual,
    add index idx_dep_date (dep_date);
    
alter table reservation
	add dep_time TIME as (TIME(departure_time)) virtual,
    add index idx_dep_time (dep_time);
    
alter table reservation
	add arr_date DATE as (DATE(arrival_time)) virtual,
    add index idx_arr_date (arr_date);
    
alter table reservation
	add arr_time TIME as (TIME(arrival_time)) virtual,
    add index idx_arr_time (arr_time);
    
drop index idx_dep_date on reservation;
    
alter table reservation
    drop dep_date;

alter table reservation
	drop index idx_dep_time
    drop dep_time;

alter table reservation
	drop index idx_arr_date
    drop arr_date;

alter table reservation
	drop index idx_arr_time
    drop arr_time;
    
-- 값 변경

SET SQL_SAFE_UPDATES = 0;

UPDATE reservation
SET
	departure_time = CASE
			WHEN MINUTE(departure_time) < 30 THEN DATE_FORMAT(departure_time, '%Y-%m-%d %H:00:00')
			ELSE DATE_FORMAT(DATE_ADD(departure_time, INTERVAL 30 MINUTE), '%Y-%m-%d %H:30:00')
		END,
    arrival_time = CASE
			WHEN MINUTE(arrival_time) < 30 THEN DATE_FORMAT(arrival_time, '%Y-%m-%d %H:00:00')
			ELSE DATE_FORMAT(DATE_ADD(arrival_time, INTERVAL 30 MINUTE), '%Y-%m-%d %H:30:00')
		END
WHERE id = 1;

SET SQL_SAFE_UPDATES = 1;
