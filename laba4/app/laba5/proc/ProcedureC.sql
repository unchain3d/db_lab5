DROP PROCEDURE IF EXISTS InsertPackage;
DELIMITER //
CREATE PROCEDURE InsertPackage()
BEGIN
    INSERT INTO airport (plane, name) VALUES 
( 20, 'Noname1'),
( 22, 'Noname2'),
( 25, 'Noname3'),
( 21, 'Noname4'),
( 23, 'Noname5'),
( 20, 'Noname6'),
( 24, 'Noname7'),
( 19, 'Noname8'),
( 18, 'Noname9'),
( 20, 'Noname10');
END //
DELIMITER ;

CALL InsertPackage()