-- 조회
SELECT * FROM GENE10S.available_time;

select reservation_date, DATE(reservation_date) AS 'DATE(reservation_date)', reservation_time, TIME(reservation_time) AS 'TIME(reservation_time)' from available_time;

select reservation_date, timestamp(reservation_date) from available_time where reservation_date = '2024-03-08';

-- 인덱스
create index available_time_reservation_date_index
	on available_time (reservation_date);
    
drop index available_time_reservation_date_index on available_time;
    
create index available_time_reservation_time_index
	on available_time (reservation_time);
    
drop index available_time_reservation_time_index on available_time;