INSERT INTO airline_company (id, name, plane) VALUES
(1, 'Mine', 10),
(2, 'Air France', 15),
(3, 'British Airways', 12),
(4, 'Lufthansa', 18),
(5, 'Emirates', 20),
(6, 'Delta Air Lines', 16),
(7, 'Qatar Airways', 14),
(8, 'Singapore Airlines', 17),
(9, 'Cathay Pacific', 13),
(10, 'American Airlines', 19);


INSERT INTO airport (id, plane, name) VALUES
(1, 20, 'FlyingSky'),
(2, 22, 'Heathrow Airport'),
(3, 25, 'Charles de Gaulle Airport'),
(4, 21, 'Frankfurt Airport'),
(5, 23, 'Dubai International Airport'),
(6, 20, 'Los Angeles International Airport'),
(7, 24, 'Haneda Airport'),
(8, 19, 'Changi Airport'),
(9, 18, 'Istanbul Airport'),
(10, 20, 'Suvarnabhumi Airport');


INSERT INTO luggage_constraints (id, max_weight, max_height, max_length, max_width) VALUES
(1, 20, 30, 50, 100),
(2, 25, 35, 55, 105),
(3, 30, 40, 60, 110),
(4, 22, 32, 52, 102),
(5, 28, 38, 58, 108),
(6, 26, 36, 56, 106),
(7, 27, 37, 57, 107),
(8, 29, 39, 59, 109),
(9, 23, 33, 53, 103),
(10, 24, 34, 54, 104);


INSERT INTO client (id, surname, name, birthday, phone) VALUES
(1, 'Smith', 'John', '2004-10-10', '38062222490'),
(2, 'Johnson', 'Sarah', '1990-08-15', '380644445566'),
(3, 'Williams', 'Michael', '1985-12-30', '380655556677'),
(4, 'Brown', 'Jessica', '1998-05-25', '380666667788'),
(5, 'Jones', 'William', '1982-11-20', '380677778899'),
(6, 'Miller', 'Emily', '1993-09-10', '380688889900'),
(7, 'Davis', 'David', '1989-04-05', '380699990011'),
(8, 'Garcia', 'Olivia', '1995-07-12', '380600001122'),
(9, 'Rodriguez', 'Daniel', '1987-02-18', '380611112233'),
(10, 'Wilson', 'Emma', '1992-06-08', '380622223344'),
(11, 'Martinez', 'Alex', '1984-03-17', '380633334455');


INSERT INTO flight (id, duration, starting_point, destination_point, luggage_constraints_id, next_connected_flight_id) VALUES
(1, 2, 1, 1, 1, 1),
(2, 3, 1, 2, 2, 2),
(3, 4, 2, 3, 3, 3),
(4, 2, 3, 4, 4, 4),
(5, 5, 4, 5, 5, 5),
(6, 6, 5, 6, 6, 6),
(7, 4, 6, 7, 7, 7),
(8, 3, 7, 8, 8, 8),
(9, 5, 8, 9, 9, 9),
(10, 6, 9, 10, 10, 10),
(11, 7, 10, 1, 1, 1);


INSERT INTO plane_ticket (seat, price, client_id, flight_id) VALUES
(101, 50, 1, 1),
(102, 60, 2, 2),
(103, 70, 3, 3),
(104, 80, 4, 4),
(105, 90, 5, 5),
(106, 100, 6, 6),
(107, 110, 7, 7),
(108, 120, 8, 8),
(109, 130, 9, 9),
(110, 140, 10, 10),
(111, 150, 11, 11);


INSERT INTO client_history (id, info, client_id) VALUES
(1, 'GAMMA', 1),
(2, 'BETA', 2),
(3, 'DELTA', 3),
(4, 'GAMMA', 4),
(5, 'EPSILON', 5),
(6, 'ZETA', 6),
(7, 'ETA', 7),
(8, 'THETA', 8),
(9, 'IOTA', 9),
(10, 'KAPPA', 10),
(11, 'LAMBDA', 11);


INSERT INTO country (name) VALUES
('USA'),
('Germany'),
('Spain'),
('Italy'),
('Russia'),
('China'),
('Japan'),
('Australia'),
('Canada'),
('Brazil'),
('India');


INSERT INTO city (name, country_name) VALUES
('New-York', 'USA'),
('Berlin', 'Germany'),
('Madrid', 'Spain'),
('Rome', 'Italy'),
('Moscow', 'Russia'),
('Beijing', 'China'),
('Tokyo', 'Japan'),
('Sydney', 'Australia'),
('Toronto', 'Canada'),
('Sao Paulo', 'Brazil'),
('Mumbai', 'India');


INSERT INTO street_adress (name, city_name, city_country_name, airport_id) VALUES
('Wall Street', 'New-York', 'USA', 1),
('Brandenburg Gate', 'Berlin', 'Germany', 2),
('Puerta del Sol', 'Madrid', 'Spain', 3),
('Colosseum', 'Rome', 'Italy', 4),
('Red Square', 'Moscow', 'Russia', 5),
('Forbidden City', 'Beijing', 'China', 6),
('Senso-ji Temple', 'Tokyo', 'Japan', 7),
('Sydney Opera House', 'Sydney', 'Australia', 8),
('CN Tower', 'Toronto', 'Canada', 9),
('Ibirapuera Park', 'Sao Paulo', 'Brazil', 10);
