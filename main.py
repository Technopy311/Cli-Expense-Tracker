from datetime import datetime
from os import getcwd, path, listdir
import logging 


logging.basicConfig(format='%(levelname)s- %(asctime)s - %(message)s', level=logging.DEBUG)

currentpath = f"{getcwd()}\\"
print(currentpath)

def addexpense(database):
    # logging.debug("Add expense function called")
    print("\n### Añadir un gasto ###")

    expense = input("Ingrese el nombre del gasto: ")
    amount = input("Ingrese la cantidad gastada (sin puntos o comas): ")
    description = input("Escriba una pequeña descripción: ")

    try:
        amount = int(amount)

    except ValueError:
        print("La cantidad del gasto debe ser un número!")
        return

    with open ((currentpath + database), 'a') as db:
        # logging.debug(f"Opened DB: {database}")

        db.write(f"\n{expense};{amount};{description}")
        # logging.debug(f"Wrote in the DB: {expense};{amount};{description}")


def showexpense(database):
    # # logging.debug("Show expenses function called")
    print("\n### Mostrando los Gastos ###\n")
    print("#  ID    Nombre    Cantidad    Descripción\n")
    sum = 0

    # logging.debug("Database currentpath: " + currentpath + database)

    with open ((currentpath + database), "r") as db:
        for index, line in enumerate(db):
            if index == 0:
                header = line.split("#")
                # logging.debug(f"Structure: {line.split('#')}")

            elif line == "" or line =="\n":
                pass
            else:
                parsed = line.split(";")
                # logging.debug(f"parsed line: {parsed}")
                print(f"  {index}  {parsed[0]}  {parsed[1]}  {parsed[2]}")
                sum += int(parsed[1])

        print(f"\nTotal de Gastos: {sum}\n\n")


def deleteexpense(database):

    # logging.debug("Delete expense function called")
    print("## Eliminar gasto ##")
    showexpense(database)
    id = input("Ingrese el ID del gasto a eliminar")

    try:
        id = int(id)
    except ValueError:
        print("Valor de ID no válido")
        return

    saving = ""


    with open ((currentpath + database), "r") as readdb:
        
        for index, line in enumerate(readdb):
            logging.debug(f"Current Index: {index}")
            logging.debug(f"Line Content: {line}")
            
            
            if line == "" or line =="\n":
                logging.debug("Line = nothing or \\n")
            elif index == id:
                logging.debug("Line = id")
            else:
                logging.debug("Line else")
                saving = f"{saving}{line}"
                logging.debug(f"Saving Content: {saving}")

        logging.debug("For loop finished")

    with open ((currentpath + database), "w") as writedb:
        logging.debug("File opened to write")
        writedb.write(saving)
        logging.debug(f"File wrote: {saving}")
    
    logging.debug("Ended function")




def checkDb(currentpath):
    files = listdir(currentpath)

    for file in files:
        # logging.debug("File: " + str(file))

        if ".etdb" in file:
            # logging.warning("DB FOUND!: " + str(file))
            return True

    return False


def createDb():
    dbname = input("Escriba el nombre de la base de datos: ")
    dbdescription = input("Escriba una breve descripción: ")

    file = f"{currentpath}{dbname}.etdb"
    
    with open(file, "x") as database:
        database.write(f"Nombre: {dbname} ")
        database.write(f"#Descripción: {dbdescription} ")
        database.write(f"#fecha de creación: {datetime.now()} ")

    print(f"Base de datos creada exitosamente, guardada en: {file}\n\n")


def availabledbs():
    files = listdir(currentpath)

    for file in files:
        if ".etdb" in file:
            print(f" + Database file: {file} ")



def main():
    print("\n#### Bienvenido al contador de Gastos ####\n\n")

    # logging.debug("App Path: " + currentpath)

    existing = checkDb(currentpath)


    if not existing:
        print("### No se encontró ninguna base de datos, creando una ###")
        createDb()
        # logging.debug("Did not find any etdb file.")

    else:
        pass
        # logging.debug("Found at least 1 db file.")


    print("### Base de Datos disponibles ###\n")

    availabledbs()


    newdb = input("\n Desea crear una nueva base de datos? Si(1) No(2): ")

    if newdb == "1":
        # logging.debug(f"Creating New DB, option: {newdb}")
        createDb()
    elif newdb == "2":
        # logging.debug(f"Creating New DB, option: {newdb}")
        pass
    else:
        # logging.debug(f"Option not recognized: {newdb}")
        print("Opción no reconocida, ejecutando menu...\n\n")


    userdb = input("\n### Escriba el nombre de la base de datos a utilizar ###\nEj: testing.etdb\n\nBASE DE DATOS: ")

    if path.isfile(f"{currentpath}{userdb}"):
        pass
    else:
        print("### El nombre de la base de datos, no es válido.")
        return



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