DROP PROCEDURE IF EXISTS AddAirportAndAirlineCompany;

DELIMITER //
CREATE PROCEDURE AddAirportAndAirlineCompany(
	IN airport_id INT,
    IN airport_plane INT,
    IN airport_name VARCHAR(45),
    IN airline_company_id INT,
    IN airline_company_name VARCHAR(45),
    IN airline_company_plane INT
)
BEGIN

    INSERT INTO airport (id, plane, name) VALUES (airport_id, airport_plane, airport_name);

    INSERT INTO airline_company (id, name, plane) VALUES (airline_company_id, airline_company_name, airline_company_plane);

    INSERT INTO airline_company_has_airport (airport_id, airline_company_id) VALUES (airport_id, airline_company_id);
END //
DELIMITER ;

CALL AddAirportAndAirlineCompany(100, 10, 'S', 100, 'R', 20)
