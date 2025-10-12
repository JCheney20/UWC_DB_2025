CREATE DATABASE IF NOT EXISTS uniride_db;
USE uniride_db;

CREATE TABLE STUDENT (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    student_email VARCHAR(150) UNIQUE NOT NULL,
    rating_avg DECIMAL(2,1)
);

CREATE TABLE PASSENGER (
    passenger_id INT PRIMARY KEY,
    preferences TEXT
);

CREATE TABLE DRIVER (
    driver_id INT PRIMARY KEY,
    vehicle_id INT,
    license_nr VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE VEHICLE (
    vehicle_id INT PRIMARY KEY,
    driver_id INT,
    vehicle_make VARCHAR(50) NOT NULL,
    vehicle_model VARCHAR(50) NOT NULL,
    seat_count INT NOT NULL,
    plate_nr VARCHAR(20) UNIQUE NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES DRIVER(driver_id)
);

CREATE TABLE ROUTE (
    route_id INT PRIMARY KEY,
    start_location VARCHAR(100) NOT NULL,
    end_location VARCHAR(100) NOT NULL,
    distance DECIMAL(8,2) NOT NULL
);

CREATE TABLE TRIP (
    trip_id INT PRIMARY KEY,
    driver_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    route_id INT NOT NULL,
    trip_time DATETIME NOT NULL,
    price_pp DECIMAL(8,2) NOT NULL,
    trip_status ENUM('scheduled', 'in-progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    FOREIGN KEY (driver_id) REFERENCES DRIVER(driver_id),
    FOREIGN KEY (vehicle_id) REFERENCES VEHICLE(vehicle_id),
    FOREIGN KEY (route_id) REFERENCES ROUTE(route_id)
);

CREATE TABLE BOOKING (
    booking_id INT PRIMARY KEY,
    trip_id INT NOT NULL,
    passenger_id INT NOT NULL,
    status ENUM('confirmed', 'pending', 'cancelled') DEFAULT 'pending',
    FOREIGN KEY (trip_id) REFERENCES TRIP(trip_id) ON DELETE CASCADE,
    FOREIGN KEY (passenger_id) REFERENCES PASSENGER(passenger_id)
);

-- Insert Data

INSERT INTO STUDENT (student_id, student_name, student_email, rating_avg) VALUES 
(1, 'Lerato Moloi', '435672@uwc.ac.za', 4.7),
(2, 'Thabo van der Merwe', '435698@uwc.ac.za', 4.2),
(3, 'Nompilo Zulu', '432679@uwc.ac.za', 3.9),
(4, 'Kagiso Botha', '435234@uwc.ac.za', 4.8),
(5, 'Zanele Pretorius', '432896@uwc.ac.za', 4.1),
(6, 'Sipho Jacobs', '431890@uwc.ac.za', 3.7),
(7, 'Anathi Ndlovu', '432674@uwc.ac.za', 4.5);

INSERT INTO PASSENGER (passenger_id, preferences) VALUES 
(101, 'Aircon, front seat'),
(102, 'Window seat, quiet ride'),
(103, 'Music allowed, chatty driver'),
(104, 'No smoking, child seat if available'),
(105, 'Extra luggage space'),
(106, 'Quickest route preferred'),
(107, 'Scenic route, no highways');

INSERT INTO DRIVER (driver_id, vehicle_id, license_nr) VALUES 
(201, 301, '880123456789'),
(202, 302, '880987654321'),
(203, 303, '880555444333'),
(204, 304, '880111222333'),
(205, 305, '880666777888'),
(206, 306, '880999000111'),
(207, 307, '880222333444');

INSERT INTO VEHICLE (vehicle_id, driver_id, vehicle_make, vehicle_model, seat_count, plate_nr) VALUES 
(301, 201, 'Toyota', 'Quest', 7, 'CA 123-456'),
(302, 202, 'Volkswagen', 'Polo Vivo', 5, 'BR 30 RJ GP'),
(303, 203, 'Ford', 'Ranger', 5, 'CF 10 VD GP'),
(304, 204, 'BMW', '3 Series', 5, 'ND 902-230'),
(305, 205, 'Toyota', 'Corolla', 5, 'BCD 457 MP'),
(306, 206, 'Mercedes-Benz', 'C-Class', 5, 'BJW 598 NC'),
(307, 207, 'Nissan', 'NP200', 5, 'BOKKE WP');

INSERT INTO ROUTE (route_id, start_location, end_location, distance) VALUES 
(401, 'UCT Upper Campus', 'University of Western Cape', 6.2),
(402, 'Cape Town CBD', 'University of Stellenbosch', 3.5),
(403, 'Rondebosch', 'Cavendish Square', 4.8),
(404, 'Sea Point', 'University of Western Cape', 5.2),
(405, 'Observatory', 'Kirstenbosch Gardens', 7.1),
(406, 'University of Western Cape', 'Constantia', 8.3),
(407, 'Camps Bay', 'University of Stellenbosch', 22.4);

INSERT INTO TRIP (trip_id, driver_id, vehicle_id, route_id, trip_time, price_pp, trip_status) VALUES 
(501, 201, 301, 401, '2024-01-03 07:30:00', 45.00, 'completed'),
(502, 202, 302, 402, '2024-05-06 09:15:00', 120.00, 'completed'),
(503, 203, 303, 403, '2024-03-10 08:00:00', 35.00, 'completed'),
(504, 204, 304, 404, '2024-05-15 06:45:00', 85.00, 'scheduled'),
(505, 205, 305, 405, '2024-05-21 07:30:00', 25.00, 'scheduled'),
(506, 206, 306, 406, '2024-09-25 10:00:00', 55.00, 'scheduled'),
(507, 207, 307, 407, '2024-10-28 08:15:00', 40.00, 'in-progress');

INSERT INTO BOOKING (booking_id, trip_id, passenger_id, status) VALUES 
(601, 501, 101, 'confirmed'),
(602, 501, 102, 'confirmed'),
(603, 502, 103, 'cancelled'),
(604, 503, 104, 'pending'),
(605, 504, 105, 'pending'),
(606, 505, 106, 'cancelled'),
(607, 506, 107, 'confirmed'),
(608, 507, 101, 'confirmed'),
(609, 501, 103, 'confirmed'),
(610, 502, 104, 'pending');
