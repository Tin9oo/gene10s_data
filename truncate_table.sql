SET FOREIGN_KEY_CHECKS = 0; -- 외래 키 제약 조건 비활성화

TRUNCATE TABLE available_time; -- 테이블 잘라내기
TRUNCATE TABLE reservation; -- 테이블 잘라내기
TRUNCATE TABLE coupon; -- 테이블 잘라내기
-- DELETE FROM reservation
-- ORDER BY id
-- LIMIT 1000; -- 삭제할 레코드 수

SET FOREIGN_KEY_CHECKS = 1; -- 외래 키 제약 조건 다시 활성화