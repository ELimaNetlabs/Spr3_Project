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

        loadData(cur, conn)

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

def loadData(cur, conn):
    # Insertar datos en la tabla Civilizacion
    insert_query_civilizacion = """
        INSERT INTO Civilizacion (nombre, ciudad_capital, lider_actual, poder_monetario, inteligencia, ejercito, poblacion)
        VALUES 
        ('Azteca', 'Tenochtitlán', 'Montezuma II', 124500.00, 85, 12000, 1500000),
        ('Egipcia', 'Menfis', 'Cleopatra VII', 180000.50, 90, 8000, 2000000),
        ('Romana', 'Roma', 'Julio César', 300000.00, 95, 25000, 4000000),
        ('Vikinga', 'Kattegat', 'Ragnar Lothbrok', 75000.00, 70, 15000, 800000),
        ('China', 'Xian', 'Qin Shi Huang', 220000.00, 98, 18000, 5000000);
    """
    cur.execute(insert_query_civilizacion)

    # Insertar datos en la tabla Aliados
    insert_query_aliados = """
        INSERT INTO Aliados (civi_1_id, civi_2_id, nivel)
        VALUES 
        (1, 2, 7),
        (3, 5, 9),
        (2, 5, 6),
        (4, 1, 8),
        (3, 4, 5);
    """
    cur.execute(insert_query_aliados)

    # Insertar datos en la tabla Enemigos
    insert_query_enemigos = """
        INSERT INTO Enemigos (civi_1_id, civi_2_id, nivel)
        VALUES 
        (1, 3, 8),
        (2, 4, 7),
        (3, 1, 9),
        (4, 5, 6),
        (5, 2, 10);
    """
    cur.execute(insert_query_enemigos)

    # Insertar datos en la tabla Territorio
    insert_query_territorio = """
        INSERT INTO Territorio (nombre, ocupante_actual, ocupante_anterior)
        VALUES 
        ('Valle del Nilo', 2, NULL),
        ('Coliseo', 3, NULL),
        ('Mesoamérica', 1, 4),
        ('Vinlandia', 4, NULL),
        ('Muralla China', 5, NULL);
    """
    cur.execute(insert_query_territorio)

    # Insertar datos en la tabla Recursos
    insert_query_recursos = """
        INSERT INTO Recursos (civi_id, madera, metal, piedra, agua, comida)
        VALUES 
        (1, 5000, 7000, 8000, 10000, 9000),
        (2, 6000, 5000, 4000, 12000, 11000),
        (3, 8000, 15000, 12000, 13000, 15000),
        (4, 10000, 9000, 7000, 8000, 12000),
        (5, 12000, 14000, 16000, 20000, 18000);
    """
    cur.execute(insert_query_recursos)

    # Confirmar los cambios
    conn.commit()

    # Ver los datos insertados en la tabla Civilizacion
    cur.execute("SELECT * FROM Civilizacion;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
