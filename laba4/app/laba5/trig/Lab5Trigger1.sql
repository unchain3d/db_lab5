CREATE TRIGGER no_country_delete
BEFORE DELETE ON country
FOR EACH ROW
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'You have no permission to delete this';