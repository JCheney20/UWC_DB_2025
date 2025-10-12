# UniRide Database Design

UniRide is a university-based carpooling platform designed to connect student drivers and passengers for safe, affordable, and efficient campus transport. This repository contains the relational database design for UniRide, including the Entity-Relationship Diagram (ERD), business rules, and normalization steps.

## File Structure
```bash
Prac 3 - uniride_app/
├── [`app/`](app/)
│ ├── [`.env`](app/.env)
│ └── [`uniride_db_app.py`](app/uniride_db_app.py)
│
├── [`sql/`](sql/)
│ ├── [`queries.sql`](sql/queries.sql)
│ └── [`setup.sql`](sql/setup.sql)
│
└── README.md
```

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
- **Visual Studio Code** for Python application script creation and testing

## Contents

- `ERD.png` – Entity Relationship Diagram
- `schema.sql` – SQL table definitions
- `business_rules.md` – Formalized business logic
- `normalization.md` – Step-by-step normalization breakdown

## Implementation
1. Create a folder with a relevant name (uniride_app) and follow file structure as mentioned above.
2. Set up the .env file accordingly -> [`.env`](app/.env)
3. Set up the python file accordingly -> [`uniride_db_app.py`](app/uniride_db_app.py)
4. Set up the SQL files -> [`setup.sql`](sql/setup.sql) and [`queries.sql`](sql/queries.sql)
5. Open the shell terminal within VSCode. 
6. Create virtual environment to run pythin commands in terminal 
```bash
python -m venv venv
venv\Scripts\activate #activate environment
```
7. Install dependencies
```bash
pip install mysql-connector-python python-dotenv faker
pip freeze > requirements.txt #stores all packages in a file for reference
```
8. Run the python script in the terminal
```bash
python uniride_db_app.py
```

