DROP TRIGGER IF EXISTS before_update_feedback;
DROP TRIGGER IF EXISTS before_insert_feedback;
DELIMITER //
CREATE TRIGGER before_update_feedback
BEFORE UPDATE ON feedback
FOR EACH ROW
BEGIN
    IF NOT EXISTS(SELECT * FROM client WHERE id = NEW.client_id ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Client does not exist';
    END IF;
END;
//
CREATE TRIGGER before_insert_feedback
BEFORE INSERT ON feedback
FOR EACH ROW
BEGIN
    IF NOT EXISTS(SELECT * FROM client WHERE id = NEW.client_id ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Client does not exist';
    END IF;
END;
//
DELIMITER ;