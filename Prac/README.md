# UniRide Database Design

UniRide is a university-based carpooling platform designed to connect student drivers and passengers for safe, affordable, and efficient campus transport. This repository contains the relational database design for UniRide, including the Entity-Relationship Diagram (ERD), business rules, and normalization steps.

## Project Overview

The database models key entities such as:
- **Student** (supertype for Driver and Passenger)
- **Driver** and **Passenger** (specialized roles)
- **Vehicle** (registered by drivers)
- **Trip** (rides offered by drivers)
- **Route** (predefined travel paths)
- **Location** (start/end points for routes)
- **Booking** (links passengers to trips)

## Relationships

- One Student may be a Driver or Passenger
- One Driver owns many Vehicles and offers many Trips
- Each Trip uses one Vehicle and follows one Route
- Passengers book Trips via the Booking entity (resolving the many-to-many relationship)

## Design Highlights

- Follows normalization principles (up to 3NF)
- Uses derived attributes (e.g., average rating)
- Enforces referential integrity with primary and foreign keys
- Designed for scalability, clarity, and real-world alignment

## Tools Used

- **draw.io (diagrams.net)** for ERD creation
- **MySQL Workbench** for schema validation and SQL generation
- **VSCode** for python application script configuration 

## Contents

- `ERD.png` – Entity Relationship Diagram
- `schema.sql` – SQL table definitions
- `business_rules.md` – Formalized business logic
- `normalization.md` – Step-by-step normalization breakdown

---

Feel free to fork, clone, or contribute as we continue building UniRide into a fully functional student transport solution.
