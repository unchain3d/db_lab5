DROP PROCEDURE IF EXISTS FUNCS;
DELIMITER //
CREATE PROCEDURE FUNCS( OUT value1 INT , OUT value2 int, OUT value3 INT, out value4 INT)
BEGIN
    SELECT MAX(plane), MIN(plane), SUM(plane), AVG(plane)
    INTO value1, value2, value3, value4
    FROM airport;
END //
DELIMITER ;

CALL FUNCS(@maxPlane, @minPlane, @sumPlane, @avgPlane);
SELECT @maxPlane AS MaxPlane, @minPlane AS MinPlane, @sumPlane AS SumPlane, @avgPlane AS AvgPlane;


