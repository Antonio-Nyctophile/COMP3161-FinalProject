import psycopg2 as psql

conn = psql.connect(
    database='lecturers_db',
    user='postgres',
    password='3072001',
    host='localhost',
    port='5432'
)

# Create a cursor
cur= conn.cursor()

# Read data from the CSV file and write it to a new SQL file
with open('Lecturers.csv', 'r') as csv_file, open('lecturers.sql', 'w') as sql_file:
    for line in csv_file.readlines()[1:]:
          values = line.strip().split(",")
          insert_query = "INSERT INTO Lecturers VALUES({}, '{}', '{}', '{}', '{}');\n".format(values[0], values[1], values[2], values[3], values[4])
          sql_file.write(insert_query)

print("A lecturer database SQL file was created with data")



# Close the database connection
conn.close()
cur.close()


