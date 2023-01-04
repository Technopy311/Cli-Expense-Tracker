from datetime import datetime
from os import getcwd, path, listdir
import logging 


logging.basicConfig(format='%(levelname)s- %(asctime)s - %(message)s', level=logging.DEBUG)

path = f"{getcwd()}\\"

def create():
    pass


def read():
    pass


def update():
    pass


def delete():
    pass


def checkDb(path):
    files = listdir(path)

    for file in files:
        logging.debug("File: " + str(file))

        if ".etdb" in file:
            logging.warning("DB FOUND!: " + str(file))
            return True

    return False


def createDb():
    print("No se encontró alguna base de datos, creando una.")
    dbname = input("Escriba el nombre de la base de datos: ")
    dbdescription = input("Escriba una breve descripción: ")

    file = f"{path}{dbname}.etdb"
    
    with open(file, "x") as database:
        database.write(f"# nombre: {dbname} ")
        database.write(f"# descripción: {dbdescription} ")
        database.write(f"# fecha de creación: {datetime.now()} ")

    print(f"Base de datos creada exitosamente, guardada en: {file}")


def availabledbs():
    files = listdir(path)

    for file in files:
        if ".etdb" in file:
            print(f" + Database file: {file} ")



def main():
    print("\n#### Bienvenido al contador de Gastos ####")
    logging.debug("App Path: " + path)

    existing = checkDb(path)

    if existing:
        logging.debug("Found at least 1 db file.")
    else:
        logging.debug("Did not find any etdb file.")
        createDb()

    print("### Base de Datos disponibles ###\n")
    availabledbs()

    userdb = input("## Escriba el nombre de la base de datos a utilizar ##\nej: testing.edtb\nBASE DE DATOS: ")

    while True:
        pass
        


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n### Adiós! ###\n")