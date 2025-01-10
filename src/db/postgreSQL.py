import psycopg2

def run(dbName):
    try:
        
        conn = psycopg2.connect(
            dbname="init",  
            user="emiliano",  
            password="Emiliano123",  
            host="localhost",  
            port="5432"
        )

        # Habilitar autocommit para permitir la creación de la base de datos sin transacción
        conn.autocommit = True
  
        cur = conn.cursor()
    
        cur.execute(f"CREATE DATABASE {dbName};")

        cur.close()
        conn.close()

        print(f"Base de datos '{dbName}' creada con éxito.")

        createTables(dbName)

    except Exception as e:
        print(f"Error: {e}")

def createTables(dbName):
    try:
        conn = psycopg2.connect(
            dbname=dbName,  
            user="emiliano",  
            password="Emiliano123",  
            host="localhost",  
            port="5432"
        )

        
        cur = conn.cursor()

        create_tables_sql = """
        CREATE TABLE IF NOT EXISTS Civilizacion (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            ciudad_capital VARCHAR(100),
            lider_actual VARCHAR(100),
            poder_monetario DECIMAL(15, 2),
            inteligencia INT,
            ejercito INT,
            poblacion INT
        );

        CREATE TABLE IF NOT EXISTS Aliados (
            id SERIAL PRIMARY KEY,
            civi_1_id INT REFERENCES Civilizacion(id) ON DELETE CASCADE,
            civi_2_id INT REFERENCES Civilizacion(id) ON DELETE CASCADE,
            nivel INT CHECK (nivel BETWEEN 1 AND 10)
        );

        CREATE TABLE IF NOT EXISTS Enemigos (
            id SERIAL PRIMARY KEY,
            civi_1_id INT REFERENCES Civilizacion(id) ON DELETE CASCADE,
            civi_2_id INT REFERENCES Civilizacion(id) ON DELETE CASCADE,
            nivel INT CHECK (nivel BETWEEN 1 AND 10)
        );

        CREATE TABLE IF NOT EXISTS Territorio (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            ocupante_actual INT REFERENCES Civilizacion(id) ON DELETE CASCADE,
            ocupante_anterior INT REFERENCES Civilizacion(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS Recursos (
            id SERIAL PRIMARY KEY,
            civi_id INT REFERENCES Civilizacion(id) ON DELETE CASCADE,
            madera INT,
            metal INT,
            piedra INT,
            agua INT,
            comida INT
        );
        """

   
        cur.execute(create_tables_sql)

 
        conn.commit()

        loadContent(cur, conn)

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

def loadContent(cur, conn):
    civilizaciones = [
    ("Civilización A", "Ciudad A", "Líder A", 500000.00, 80, 50000, 2000000),
    ("Civilización B", "Ciudad B", "Líder B", 600000.00, 85, 60000, 2500000),
    ("Civilización C", "Ciudad C", "Líder C", 700000.00, 90, 70000, 3000000)
    ]

    insert_query_civilizacion = """
        INSERT INTO Civilizacion (nombre, ciudad_capital, lider_actual, poder_monetario, inteligencia, ejercito, poblacion)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    cur.executemany(insert_query_civilizacion, civilizaciones)

    conn.commit()

    cur.execute("SELECT * FROM Civilizacion;")

    rows = cur.fetchall()

    for row in rows:
        print(row)