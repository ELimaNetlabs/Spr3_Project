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
            inteligencia INT CHECK (inteligencia BETWEEN 1 AND 10),
            ejercito INT CHECK (ejercito BETWEEN 1 AND 10),
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

        

        cur.close()
        conn.close()
        loadData()

    except Exception as e:
        print(f"Error: {e}")

def loadData():
    
    conn = psycopg2.connect(
        dbname="civilizationsimulator",  
        user="emiliano",  
        password="Emiliano123",  
        host="localhost",  
        port="5432"
    )

    cur = conn.cursor()

    insert_query_civilizacion = """
        INSERT INTO Civilizacion (nombre, ciudad_capital, lider_actual, poder_monetario, inteligencia, ejercito, poblacion)
        VALUES 
        ('Azterna', 'Luminaris', 'Solaria Eclipse', 250000.00, 8, 4, 1200000),
        ('Nyboria', 'Umbraterra', 'Kael Umbra', 175000.50, 7, 3, 950000),
        ('Velmoria', 'Zenthara', 'Artemis Nova', 300000.00, 9, 5, 2200000),
        ('Aqualis', 'Hydronix', 'Poseidros Marinus', 190000.00, 6, 4, 1800000),
        ('Pyrosis', 'Flamidor', 'Ignatia Blaze', 200000.00, 5, 6, 1700000),
        ('Aerion', 'Skylantis', 'Zephyr Tempus', 225000.00, 6, 4, 1600000),
        ('Terranova', 'Gaiapolis', 'Terra Verde', 210000.00, 8, 3, 1900000),
        ('Celestica', 'Astropolis', 'Luna Starfall', 320000.00, 9, 2, 1500000),
        ('Frostgard', 'Cryonis', 'Aurora Frostbane', 180000.00, 6, 5, 1400000),
        ('Mystara', 'Enigma', 'Arcana Shade', 240000.00, 10, 3, 1000000);
    """
    cur.execute(insert_query_civilizacion)

    insert_query_aliados = """
        INSERT INTO Aliados (civi_1_id, civi_2_id, nivel)
        VALUES 
        (1, 2, 8),
        (3, 4, 6),
        (5, 6, 7),
        (7, 8, 9),
        (2, 3, 5),
        (4, 5, 8),
        (1, 9, 6),
        (6, 10, 4),
        (8, 10, 7),
        (3, 7, 5);
    """
    cur.execute(insert_query_aliados)

    insert_query_enemigos = """
        INSERT INTO Enemigos (civi_1_id, civi_2_id, nivel)
        VALUES 
        (1, 3, 9),
        (2, 5, 7),
        (4, 6, 8),
        (7, 9, 5),
        (8, 10, 6),
        (3, 5, 9),
        (2, 6, 7),
        (1, 8, 8),
        (4, 10, 6),
        (9, 5, 5);
    """
    cur.execute(insert_query_enemigos)

    insert_query_territorio = """
        INSERT INTO Territorio (nombre, ocupante_actual, ocupante_anterior)
        VALUES 
        ('Bosque de Luminaris', 1, 2),
        ('Montañas de Umbraterra', 2, 3),
        ('Llanuras de Zenthara', 3, 4),
        ('Islas de Hydronix', 4, 5),
        ('Desiertos de Flamidor', 5, 6),
        ('Cumbres de Skylantis', 6, 7),
        ('Valles de Gaiapolis', 7, 8),
        ('Asteroides de Astropolis', 8, 9),
        ('Glaciares de Cryonis', 9, 10),
        ('Ruinas de Enigma', 10, 1);
    """
    cur.execute(insert_query_territorio)

    insert_query_recursos = """
        INSERT INTO Recursos (civi_id, madera, metal, piedra, agua, comida)
        VALUES 
        (1, 500, 300, 200, 1000, 800),
        (2, 600, 400, 300, 1200, 900),
        (3, 700, 500, 400, 1400, 1000),
        (4, 800, 600, 500, 1600, 1100),
        (5, 900, 700, 600, 1800, 1200),
        (6, 1000, 800, 700, 2000, 1300),
        (7, 1100, 900, 800, 2200, 1400),
        (8, 1200, 1000, 900, 2400, 1500),
        (9, 1300, 1100, 1000, 2600, 1600),
        (10, 1400, 1200, 1100, 2800, 1700);
    """
    cur.execute(insert_query_recursos)



    conn.commit()
    cur.close()
    conn.close()
   

def updateTableCivilization(cId, op, data):
    conn = psycopg2.connect(
        dbname="civilizationsimulator",  
        user="emiliano",  
        password="Emiliano123",  
        host="localhost",  
        port="5432"
    )

    cur = conn.cursor()

    if op == 1:  
        query = "UPDATE Civilizacion SET nombre = %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 2:  
        query = "UPDATE Civilizacion SET ciudad_capital = %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 3:  
        query = "UPDATE Civilizacion SET lider_actual = %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 4:  
        query = "UPDATE Civilizacion SET poder_monetario = poder_monetario + %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 5:  
        query = "UPDATE Civilizacion SET inteligencia = %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 6:  
        query = "UPDATE Civilizacion SET ejercito = ejercito + %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 7:  
        query = "UPDATE Civilizacion SET poblacion = poblacion + %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 8:  
        query = "UPDATE Civilizacion SET ejercito = ejercito - %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 9:  
        query = "UPDATE Civilizacion SET poder_monetario = poder_monetario - %s WHERE id = %s"
        cur.execute(query, (data, cId))
    elif op == 10:  
        query = "UPDATE Civilizacion SET poblacion = poblacion - %s WHERE id = %s"
        cur.execute(query, (data, cId))
    else:
        print("Error: Operación no válida.")

    conn.commit()
    cur.close()
    conn.close()

def updateTableAliados(cId1, cId2, op, data):
    conn = psycopg2.connect(
        dbname="civilizationsimulator",  
        user="emiliano",  
        password="Emiliano123",  
        host="localhost",  
        port="5432"
    )

    cur = conn.cursor()

    if op == 1:  
        query = "UPDATE Aliados SET nivel = %s WHERE civi_1_id = %s and civi_2_id = %s"
        cur.execute(query, (data, cId1, cId2))
    elif op == 2:  
        query = "DELETE FROM Aliados WHERE civi_1_id = %s and civi_2_id = %s"
        cur.execute(query, (cId1, cId2))
    elif op == 3:  
        query = "INSERT INTO Aliados (civi_1_id, civi_2_id, nivel) VALUES (%s, %s, %s)"
        cur.execute(query, (cId1, cId2, data))

    else:
        print("Error: Operación no válida.")

    conn.commit()
    cur.close()
    conn.close()

def updateTableEnemigos(cId1, cId2, op, data):
    conn = psycopg2.connect(
        dbname="civilizationsimulator",  
        user="emiliano",  
        password="Emiliano123",  
        host="localhost",  
        port="5432"
    )

    cur = conn.cursor()

    if op == 1:  
        query = "UPDATE Enemigos SET nivel = %s WHERE civi_1_id = %s and civi_2_id = %s"
        cur.execute(query, (data, cId1, cId2))
    elif op == 2:  
        query = "DELETE FROM Enemigos WHERE civi_1_id = %s and civi_2_id = %s"
        cur.execute(query, (cId1, cId2))
    else:
        print("Error: Operación no válida.")

    conn.commit()
    cur.close()
    conn.close()
