import sqlite3
import os
from datetime import datetime

class LocalDatabaseManager:
    """
    Handles secure database connections, schema creation, 
    and transaction execution for scraped business leads.
    """
    def __init__(self, db_name="leads_vault.db"):
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        """Creates the leads table securely if it doesn't exist yet."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customer_leads (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    budget REAL,
                    captured_at TEXT
                )
            """)
            conn.commit()
        print(f"[{datetime.now()}] Database architecture verified/initialized.")

    def insert_lead_securely(self, name, email, budget):
        """Inserts data safely using parameterized queries to prevent SQL injection."""
        query = """
            INSERT OR IGNORE INTO customer_leads (client_name, email, budget, captured_at)
            VALUES (?, ?, ?, ?)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query, (name, email, budget, timestamp))
                conn.commit()
                if cursor.rowcount > 0:
                    print(f"[SQL Success] New lead archived: {email}")
                else:
                    print(f"[SQL Notice] Duplicate email skipped: {email}")
        except sqlite3.Error as e:
            print(f"[SQL Error] Failed to write database transaction: {e}")

if __name__ == "__main__":
    # Test simulation
    db = LocalDatabaseManager()
    db.insert_lead_securely("John Doe", "john.doe@uk_startup.com", 2500.00)
    db.insert_lead_securely("Jane Smith", "jane@tech_leads.net", 410.50)
    db.insert_lead_securely("John Doe", "john.doe@uk_startup.com", 2500.00) # Duplicate check
