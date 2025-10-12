import mysql.connector
from dotenv import load_dotenv
import os

# Loads environment variables from .env file
#  -keeps database credentials secure and out of the codebase
load_dotenv()

# Database credentials from .env
db_config = {
    "host": os.getenv("DB_HOST"),        # Database server address 
    "port": int(os.getenv("DB_PORT")),   # Database port (converted to integer)
    "user": os.getenv("DB_USER"),        # Database username
    "password": os.getenv("DB_PASS"),    # Database password
    "database": os.getenv("DB_NAME")     # Specific database to connect to
}

def execute_sql_file(cursor, filename):
    """
    Reads and executes all SQL commands from a .sql file.
    
    This function:
    1. Opens and reads the SQL file
    2. Splits the content into individual SQL statements using semicolons as delimiters
    3. Executes each non-empty statement
    4. Automatically consumes any result sets to prevent 'unread result' errors
    
    Arguments:
        cursor: Database cursor object for executing SQL commands
        filename (str): Path to the SQL file to execute
    
    Raises:
        FileNotFoundError: If the specified SQL file doesn't exist
        mysql.connector.Error: For database-related errors
    """
    try:
        # Read the entire SQL file content
        with open(filename, "r") as file:
            sql_commands = file.read()
        
        # Splits SQL content into individual statements using semicolon delimiter
        # Filtesr out any empty statements that might result from the split
        statements = [stmt.strip() for stmt in sql_commands.split(";") if stmt.strip()]
        
        # Executes each SQL statement sequentially
        for statement in statements:
            # Execute the current SQL statement
            cursor.execute(statement)
            
            # Consume any results to prevent 'unread result' errors (which we came across)
            # This is necessary when moving from a SELECT query to another execution
            try:
                cursor.fetchall()  # Fetch all rows even if we don't use them
            except mysql.connector.errors.InterfaceError:
                # This exception is expected for non-SELECT queries (INSERT, UPDATE, etc.)
                # that don't return result sets - we can safely ignore it
                pass
            
            # Print confirmation with the first 50 characters of the executed statement
            print(f"✓ Executed: {statement[:50]}{'...' if len(statement) > 50 else ''}")
                
    except FileNotFoundError:
        print(f"❌ SQL file not found: {filename}")
        raise
    except Exception as e:
        print(f"❌ Error processing SQL file: {filename}")
        print(f"Error: {e}")
        raise

def main():
    """
    Main function that orchestrates the database connection and SQL execution.
    
    Flow:
    1. Establish database connection
    2. Create a buffered cursor (prevents unread result errors)
    3. Execute setup.sql for database initialization
    4. Execute queries.sql for data retrieval/operations
    5. Handle errors and ensure proper connection cleanup
    """
    # Initialize connection and cursor variables to ensure they exist in finally block
    conn = None
    cursor = None
    
    try:
        # Establish connection to the database using configuration from .env
        conn = mysql.connector.connect(**db_config)
        
        # Create a buffered cursor - this is crucial for preventing 'unread result' errors
        # A buffered cursor fetches and stores all result sets immediately
        cursor = conn.cursor(buffered=True) # Key fix from "unread result found" error
        print("✅ Connected to the database!")

        # Execute setup SQL file 
        print("\nRunning setup.sql...")
        execute_sql_file(cursor, "../sql/setup.sql")
        
        # Commit the transaction to save changes made by setup.sql
        conn.commit()
        print("✅ Database setup complete!")

        # Execute queries SQL file 
        print("\nRunning queries.sql...")
        execute_sql_file(cursor, "../sql/queries.sql")
        
        # Commit any changes made by queries.sql 
        conn.commit()
        print("✅ All queries executed successfully!")

    except mysql.connector.Error as err:
        # Handle database-specific errors 
        print(f"❌ Database error: {err}")
    except Exception as err:
        # Handle any other unexpected errors
        print(f"❌ Unexpected error: {err}")
    finally:
        # Cleanup section - always executed whether successful or not
        
        # Close cursor if it was created
        if cursor:
            cursor.close()
            
        # Close database connection if it was established and is still open
        if conn and conn.is_connected():
            conn.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    main()
