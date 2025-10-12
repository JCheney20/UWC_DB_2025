-- 1. List all students
SELECT * FROM STUDENT;

-- 2. List all trips with prices between R30 and R60 scheduled after March 1, 2024
SELECT trip_id, driver_id, vehicle_id, route_id, trip_time, price_pp, trip_status
FROM TRIP
WHERE price_pp BETWEEN 30.00 AND 60.00
  AND trip_time > '2024-03-01'
  AND trip_status = 'scheduled';

-- 3. Find students with names containing the letter 'J'
SELECT student_id, student_name, student_email, rating_avg
FROM STUDENT
WHERE student_name LIKE '%J%';

-- 4. Students with rating >= 4.5 or confirmed bookings, excluding names starting with 'A'
SELECT s.student_id, s.student_name, s.student_email, s.rating_avg
FROM STUDENT s
WHERE (s.rating_avg >= 4.5 OR s.student_id IN (
    SELECT b.passenger_id FROM BOOKING b WHERE b.status = 'confirmed'
))
AND s.student_name NOT LIKE 'A%';

-- 5. Count bookings per trip status
SELECT 
    T.trip_status,
    COUNT(B.booking_id) AS booking_count,
    AVG(T.price_pp) AS average_price
FROM TRIP T
LEFT JOIN BOOKING B ON T.trip_id = B.trip_id
GROUP BY T.trip_status
ORDER BY booking_count DESC;

-- 6. Find drivers with no in-progress trips
SELECT driver_id FROM DRIVER
EXCEPT
SELECT driver_id FROM TRIP WHERE trip_status = 'in-progress'
ORDER BY driver_id;

-- 7. Students with ratings higher than average
SELECT student_id, student_name, student_email, rating_avg
FROM STUDENT
WHERE rating_avg > (SELECT AVG(rating_avg) FROM STUDENT WHERE rating_avg IS NOT NULL)
ORDER BY rating_avg DESC;

-- 8. Booking summary per passenger (confirmed/pending/cancelled)
SELECT
  P.passenger_id,
  P.preferences,
  COUNT(B.booking_id) AS total_bookings,
  (SELECT COUNT(*) FROM BOOKING B2 WHERE B2.passenger_id = P.passenger_id AND B2.status = 'confirmed') AS confirmed_count,
  (SELECT COUNT(*) FROM BOOKING B3 WHERE B3.passenger_id = P.passenger_id AND B3.status = 'pending') AS pending_count,
  (SELECT COUNT(*) FROM BOOKING B4 WHERE B4.passenger_id = P.passenger_id AND B4.status = 'cancelled') AS cancelled_count
FROM PASSENGER P
LEFT JOIN BOOKING B ON P.passenger_id = B.passenger_id
GROUP BY P.passenger_id, P.preferences
HAVING COUNT(B.booking_id) > 0
ORDER BY total_bookings DESC;

-- 9. Full view of trips with driver, vehicle, route, and bookings
SELECT 
    T.trip_id,
    T.trip_time,
    T.price_pp,
    T.trip_status,
    D.driver_id,
    V.vehicle_make,
    V.vehicle_model,
    V.seat_count,
    R.start_location,
    R.end_location,
    R.distance,
    COUNT(B.booking_id) AS total_bookings,
    (SELECT COUNT(*) 
     FROM BOOKING B2 
     WHERE B2.trip_id = T.trip_id AND B2.status = 'confirmed') AS confirmed_passengers
FROM TRIP T
JOIN DRIVER D ON T.driver_id = D.driver_id
JOIN VEHICLE V ON T.vehicle_id = V.vehicle_id
JOIN ROUTE R ON T.route_id = R.route_id
LEFT JOIN BOOKING B ON T.trip_id = B.trip_id
GROUP BY 
    T.trip_id, T.trip_time, T.price_pp, T.trip_status,
    D.driver_id, V.vehicle_make, V.vehicle_model, V.seat_count,
    R.start_location, R.end_location, R.distance
ORDER BY T.trip_time, total_bookings DESC;

-- 10. Scheduled trips ordered by time
SELECT 
    T.trip_id,
    T.trip_time,
    T.price_pp,
    T.trip_status,
    R.start_location,
    R.end_location,
    R.distance
FROM TRIP T
JOIN ROUTE R ON T.route_id = R.route_id
WHERE T.trip_status = 'scheduled'
ORDER BY T.trip_time ASC;

-- 11. Confirmed bookings with passenger and trip details
SELECT 
    B.booking_id,
    P.passenger_id,
    P.preferences,
    T.trip_id,
    T.trip_time,
    T.price_pp,
    T.trip_status,
    R.start_location,
    R.end_location,
    R.distance
FROM BOOKING B
JOIN PASSENGER P ON B.passenger_id = P.passenger_id
JOIN TRIP T ON B.trip_id = T.trip_id
JOIN ROUTE R ON T.route_id = R.route_id
WHERE B.status = 'confirmed'
ORDER BY T.trip_time;

-- 12. What is the revenue performance (trip count, total revenue, and average trip price) for trips with confirmed bookings, organized by vehicle type and trip status?
SELECT 
    V.vehicle_id,
    V.vehicle_make,
    V.vehicle_model,
    T.trip_status,
    COUNT(T.trip_id) AS trip_count,
    SUM(T.price_pp) AS total_revenue,
    AVG(T.price_pp) AS avg_trip_price
FROM VEHICLE V
JOIN TRIP T ON V.vehicle_id = T.vehicle_id
JOIN BOOKING B ON T.trip_id = B.trip_id
WHERE B.status = 'confirmed'
GROUP BY V.vehicle_id, V.vehicle_make, V.vehicle_model, T.trip_status
ORDER BY V.vehicle_make, V.vehicle_model, T.trip_status;
