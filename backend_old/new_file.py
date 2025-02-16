import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="recipe_database"
)

mycursor = db.cursor()

# Creating table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS RECIPE_TABLE (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(50), 
        category VARCHAR(50), 
        no_Of_Likes INT UNSIGNED DEFAULT 0
    )
""")

# Creating comments table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS COMMENTS (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        recipe_id INT, 
        comment_text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        FOREIGN KEY (recipe_id) REFERENCES RECIPE_TABLE(id) ON DELETE CASCADE
    )
""")

# Inserting data
mycursor.execute("INSERT INTO RECIPE_TABLE(name, category) VALUES('BURGER', 'JUNK_FOOD')")
db.commit()  # Commit the transaction

# Fetch and print data
mycursor.execute("SELECT * FROM RECIPE_TABLE")
for row in mycursor.fetchall():
    print(row)

db.close()  # Close connection

# mycursor.execute(
#     "CREATE DATABASE recipe_database"
# )
# name
# category
# no_Of_Likes
# comments

