-- SQL script that creates an index idx_name_first
-- on the table names and the first letter of name.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
  DECLARE avg_score FLOAT;
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE user_id = user_id;
  UPDATE users
  SET average_score = avg_score
  WHERE id = user_id
END //

DELIMITER ;
