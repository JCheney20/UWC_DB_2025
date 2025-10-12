import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database credentials from .env
db_config = {
    "host": os.getenv("DB_HOST"), # Database server address 
    "port": int(os.getenv("DB_PORT")), # Database port (converted to integer)
    "user": os.getenv("DB_USER"), # Database username
    "password": os.getenv("DB_PASS"), # Database password
    "database": os.getenv("DB_NAME") # Specific database to connect to
}

def execute_sql_file(cursor, filename):
    #Reads and executes all SQL commands from a .sql file.
    try:
        with open(filename, "r") as file:
            sql_commands = file.read()
        
        statements = [stmt.strip() for stmt in sql_commands.split(";") if stmt.strip()]
        
        for statement in statements:
            cursor.execute(statement)
            # Consume any results
            try:
                cursor.fetchall()
            except mysql.connector.errors.InterfaceError:
                # No result set - this is normal for non-SELECT queries
                pass
            print(f"✓ Executed: {statement[:50]}{'...' if len(statement) > 50 else ''}")
                
    except FileNotFoundError:
        print(f"❌ SQL file not found: {filename}")
        raise
    except Exception as e:
        print(f"❌ Error processing SQL file: {filename}")
        print(f"Error: {e}")
        raise

def main():
    # Main function manages database connection and SQL execution
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(buffered=True)  # This is the key fix
        print("✅ Connected to the database!")

        # Run setup
        print("\nRunning setup.sql...")
        execute_sql_file(cursor, "../sql/setup.sql")
        conn.commit()
        print("✅ Database setup complete!")

        # Run queries
        print("\nRunning queries.sql...")
        execute_sql_file(cursor, "../sql/queries.sql")
        conn.commit()
        print("✅ All queries executed successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Database error: {err}")
    except Exception as err:
        print(f"❌ Unexpected error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    main()
