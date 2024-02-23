## 프로세스 목록
SHOW PROCESSLIST;

## 슬로우 쿼리 확인
SELECT query, exec_count, sys.format_time(avg_latency) AS "avg latency", rows_sent_avg, rows_examined_avg, last_seen
FROM sys.x$statement_analysis
ORDER BY avg_latency DESC;

## 성능 개선 대상 식별
SELECT DIGEST_TEXT AS query,
             IF(SUM_NO_GOOD_INDEX_USED > 0 OR SUM_NO_INDEX_USED > 0, '*', '') AS full_scan,
             COUNT_STAR AS exec_count,
             SUM_ERRORS AS err_count,
             SUM_WARNINGS AS warn_count,
             SEC_TO_TIME(SUM_TIMER_WAIT/1000000000000) AS exec_time_total, 
             SEC_TO_TIME(MAX_TIMER_WAIT/1000000000000) AS exec_time_max, 
             SEC_TO_TIME(AVG_TIMER_WAIT/1000000000000) AS exec_time_avg_ms, SUM_ROWS_SENT AS rows_sent,
             ROUND(SUM_ROWS_SENT / COUNT_STAR) AS rows_sent_avg, SUM_ROWS_EXAMINED AS rows_scanned,
             DIGEST AS digest
   FROM performance_schema.events_statements_summary_by_digest ORDER BY SUM_TIMER_WAIT DESC;

##  I/O 요청이 많은 테이블 목록
SELECT * FROM sys.io_global_by_file_by_bytes WHERE file LIKE '%ibd';

## 테이블별 작업량 통계 
SELECT table_schema, table_name, rows_fetched, rows_inserted, rows_updated, rows_deleted, io_read, io_write
FROM sys.schema_table_statistics
WHERE table_schema NOT IN ('mysql', 'performance_schema', 'sys');

## 최근 실행된 쿼리 이력 기능 활성화
UPDATE performance_schema.setup_consumers SET ENABLED = 'yes' WHERE NAME = 'events_statements_history';
UPDATE performance_schema.setup_consumers SET ENABLED = 'yes' WHERE NAME = 'events_statements_history_long';

## 최근 실행된 쿼리 이력 확인
SELECT * FROM performance_schema.events_statements_history;