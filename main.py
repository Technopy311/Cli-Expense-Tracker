from datetime import datetime
from os import getcwd, path, listdir
# import logging 


# logging.basicConfig(format='%(levelname)s- %(asctime)s - %(message)s', level=# logging.DEBUG)

path = f"{getcwd()}\\"

def addexpense(database):
    # # logging.debug("Add expense function called")
    print("\n### Añadir un gasto ###")

    expense = input("Ingrese el nombre del gasto: ")
    amount = input("Ingrese la cantidad gastada (sin puntos o comas): ")
    description = input("Escriba una pequeña descripción: ")

    with open (f"{path}{database}", 'a') as db:
        # logging.debug(f"Opened DB: {database}")
        db.write(f"\n{expense};{amount};{description}")
        # # logging.debug(f"Wrote in the DB: {expense};{amount};{description}")


def showexpense(database):
    # # logging.debug("Show expenses function called")
    print("\n### Mostrar los Gastos ###\n")
    print("#  ID    Nombre    Cantidad    Descripción\n")
    sum = 0

    with open (f"{path}{database}", "r") as db:
        for index, line in enumerate(db):
            if index == 0:
                header = line.split("#")
                # # logging.debug(f"Structure: {line.split('#')}")
                #print(f"## {header[0]} ## {header[1]} ## {header[2]} ##")
            elif line == "" or line =="\n":
                print("  No hay gastos registrados")
            else:
                parsed = line.split(";")
                # # logging.debug(f"parsed line: {parsed}")
                print(f"  {index}  {parsed[0]}  {parsed[1]}  {parsed[2]}")
                sum += int(parsed[1])

        print(f"\nTotal de Gastos: {sum}\n\n")


def deleteexpense(database):
    pass
    # logging.debug("Delete expense function called")


def checkDb(path):
    files = listdir(path)

    for file in files:
        # logging.debug("File: " + str(file))

        if ".etdb" in file:
            # logging.warning("DB FOUND!: " + str(file))
            return True

    return False


def createDb():
    print("No se encontró alguna base de datos, creando una.")
    dbname = input("Escriba el nombre de la base de datos: ")
    dbdescription = input("Escriba una breve descripción: ")

    file = f"{path}{dbname}.etdb"
    
    with open(file, "x") as database:
        database.write(f"Nombre: {dbname} ")
        database.write(f"#Descripción: {dbdescription} ")
        database.write(f"#fecha de creación: {datetime.now()} ")

    print(f"Base de datos creada exitosamente, guardada en: {file}\n\n")


def availabledbs():
    files = listdir(path)

    for file in files:
        if ".etdb" in file:
            print(f" + Database file: {file} ")



def main():
    print("\n#### Bienvenido al contador de Gastos ####\n\n")

    # logging.debug("App Path: " + path)

    existing = checkDb(path)

    if existing:
        pass
        # logging.debug("Found at least 1 db file.")
    else:
        # logging.debug("Did not find any etdb file.")
        createDb()

    print("### Base de Datos disponibles ###\n")
    availabledbs()

    userdb = input("\n### Escriba el nombre de la base de datos a utilizar ###\nEj: testing.etdb\n\nBASE DE DATOS: ")
    print("\n ### Menu de Usuario ### \n")
    while True:
        option = input("Opciones:\n + Añadir Gasto (1).    + Ver los gastos (2).\n + Eliminar Gasto(3). \n\nIngrese Nro de opción: ")

        if int(option) == 1:
            addexpense(userdb)
        elif int(option) == 2:
            showexpense(userdb)
        elif int(option) == 3:
            deleteexpense(userdb)
        else:
            # logging.debug(f"Option not recognized: {option}")
            pass



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n### Adiós! ###\n")