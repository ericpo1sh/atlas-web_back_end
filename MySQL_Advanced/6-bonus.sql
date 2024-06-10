-- SQL script that creates a stored procedure ComputeAverageScoreForUser
--  that computes and store the average score for a student.
DELIMITER //
CREATE PROCEDURE AddBonus (
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)
BEGIN
  DECLARE project_id INT -- declaring variable to store project id
  SELECT ID INTO project_id
  FROM projects
  WHERE name = project_name -- checking from table projects.name if same as param
  IF project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project, score)
END //
DELIMITER ;
