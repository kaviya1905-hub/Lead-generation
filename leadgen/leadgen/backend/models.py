from database import get_db_connection
# Insert company
def insert_company(company_name, city, country, persona, industry):
    db = get_db_connection()
    db.execute(
        "INSERT INTO companies(company_name, city, country, persona, industry) VALUES (?,?,?,?,?)",
        (company_name, city, country, persona, industry)
    )
    db.commit()
    db.close()

from database import get_db_connection

def get_companies(persona, industry):
    conn = get_db_connection()
    cursor = conn.execute("""
        SELECT company_name, city, country 
        FROM companies 
        WHERE lower(persona)=lower(?) 
          AND lower(industry)=lower(?)
    """, (persona, industry))

    companies = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return companies
