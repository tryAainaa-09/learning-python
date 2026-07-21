"""
Asset Management System - Database Setup
Uses Python's built-in sqlite3 module.

This creates the EXACT same structure as asset_management_schema.sql —
sqlite3 just executes the same SQL statements under the hood.
"""

import sqlite3
from pathlib import Path

DB_NAME = "asset_management.db"


def get_connection():
    """Open a connection with foreign key enforcement turned on."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row  # lets you access columns by name
    return conn


def create_tables(conn):
    """Create all tables. Same DDL as the .sql file, just run via Python."""
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS asset_group (
            asset_group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name     TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS asset_status (
            status_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            status_name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS asset (
            asset_id        INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_tag       TEXT NOT NULL UNIQUE,
            serial_number   TEXT,
            model           TEXT NOT NULL,
            brand           TEXT NOT NULL,
            asset_group_id  INTEGER NOT NULL,
            purchase_date   DATE,
            warranty_expiry DATE,
            remarks         TEXT,
            status_id       INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (asset_group_id) REFERENCES asset_group(asset_group_id),
            FOREIGN KEY (status_id)      REFERENCES asset_status(status_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            user_id    TEXT PRIMARY KEY,
            full_name  TEXT NOT NULL,
            email      TEXT NOT NULL UNIQUE,
            department TEXT,
            location   TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignment (
            assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id      INTEGER NOT NULL,
            user_id       TEXT NOT NULL,
            assign_date   DATE NOT NULL,
            return_date   DATE,
            status        TEXT NOT NULL DEFAULT 'Assigned'
                          CHECK (status IN ('Assigned', 'Returned')),
            FOREIGN KEY (asset_id) REFERENCES asset(asset_id),
            FOREIGN KEY (user_id)  REFERENCES user(user_id)
        )
    """)

    # Indexes
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_asset_status ON asset(status_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_asset_group ON asset(asset_group_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_assignment_asset ON assignment(asset_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_assignment_user ON assignment(user_id)")

    conn.commit()


def seed_lookup_data(conn):
    """Insert the fixed lookup values (groups + statuses)."""
    cursor = conn.cursor()

    groups = [(1, 'Laptop'), (2, 'Desktop'), (3, 'Monitor'),
              (4, 'Printer'), (5, 'Phone'), (6, 'Network')]
    cursor.executemany(
        "INSERT OR IGNORE INTO asset_group (asset_group_id, group_name) VALUES (?, ?)",
        groups
    )

    statuses = [(1, 'Available'), (2, 'Assigned'), (3, 'Repair'),
                (4, 'Disposed'), (5, 'Lost')]
    cursor.executemany(
        "INSERT OR IGNORE INTO asset_status (status_id, status_name) VALUES (?, ?)",
        statuses
    )

    conn.commit()


def seed_sample_data(conn):
    """Insert the sample records from the original notes (run once)."""
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO user (user_id, full_name, email, department, location)
        VALUES ('EMP001', 'Khairi', 'khairi@company.com', 'IT', 'HQ')
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO asset
            (asset_tag, serial_number, model, brand, asset_group_id,
             purchase_date, warranty_expiry, remarks, status_id)
        VALUES
            ('AQE-LTP-24001', '1TJ9X14', 'Latitude 3440', 'Dell', 1,
             '2024-01-05', '2027-01-05', 'New', 2)
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO assignment
            (asset_id, user_id, assign_date, return_date, status)
        VALUES (1, 'EMP001', '2024-01-05', NULL, 'Assigned')
    """)

    conn.commit()


def init_db():
    """Run this once to set up the database file from scratch."""
    conn = get_connection()
    create_tables(conn)
    seed_lookup_data(conn)
    seed_sample_data(conn)
    conn.close()
    print(f"Database ready at: {Path(DB_NAME).resolve()}")


if __name__ == "__main__":
    init_db()
