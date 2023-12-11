DROP PROCEDURE IF EXISTS InsertIntoAirport;
DELIMITER //
CREATE PROCEDURE InsertIntoAirport(
    IN a_plane INT, IN a_name VARCHAR(45)
)
BEGIN
    INSERT INTO airport (plane, name) VALUES (a_plane, a_name);
END //
DELIMITER ;

CALL InsertIntoAirport(500, 'Oki')