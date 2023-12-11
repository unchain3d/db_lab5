CREATE TRIGGER no_modification_flight 
BEFORE UPDATE ON flight
FOR EACH ROW
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Modification is forbidden';