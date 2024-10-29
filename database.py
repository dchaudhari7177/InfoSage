import sqlite3

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect('qa_system.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS qa_pairs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_qa_pair(question, answer):
    """Insert a question-answer pair into the database."""
    conn = sqlite3.connect('qa_system.db')
    c = conn.cursor()
    c.execute('INSERT INTO qa_pairs (question, answer) VALUES (?, ?)', (question, answer))
    conn.commit()
    conn.close()

def fetch_qa_history():
    """Fetch all question-answer pairs from the database."""
    conn = sqlite3.connect('qa_system.db')
    c = conn.cursor()
    c.execute('SELECT * FROM qa_pairs')
    qa_pairs = c.fetchall()
    conn.close()
    return qa_pairs

def fetch_qa_by_id(qa_id):
    """Fetch a specific question-answer pair by ID."""
    conn = sqlite3.connect('qa_system.db')
    c = conn.cursor()
    c.execute('SELECT * FROM qa_pairs WHERE id = ?', (qa_id,))
    qa_pair = c.fetchone()
    conn.close()
    return qa_pair

def delete_qa_pair(qa_id):
    """Delete a question-answer pair from the database by ID."""
    conn = sqlite3.connect('qa_system.db')
    c = conn.cursor()
    c.execute('DELETE FROM qa_pairs WHERE id = ?', (qa_id,))
    conn.commit()
    conn.close()

init_db()
