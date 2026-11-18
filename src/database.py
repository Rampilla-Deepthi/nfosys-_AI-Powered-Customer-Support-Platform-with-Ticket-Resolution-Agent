
import sqlite3

def create_table():

    conn = sqlite3.connect("supportpilot.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            description TEXT,
            category TEXT,
            ticket_type TEXT,
            priority TEXT,
            severity TEXT,
            resolution TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_ticket(subject, description, category, ticket_type,
                priority, severity, resolution):

    conn = sqlite3.connect("supportpilot.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets
        (subject, description, category, ticket_type,
         priority, severity, resolution, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (subject, description, category, ticket_type,
          priority, severity, resolution, "Pending"))

    ticket_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return ticket_id


def update_ticket_status(ticket_id, status):

    conn = sqlite3.connect("supportpilot.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tickets SET status = ? WHERE id = ?",
        (status, ticket_id)
    )

    conn.commit()
    conn.close()

def get_all_tickets():

    conn = sqlite3.connect("supportpilot.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets ORDER BY id DESC")

    tickets = cursor.fetchall()

    conn.close()

    return tickets
