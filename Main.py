import sqlite3


def connect_database():
    conn = sqlite3.connect('budget.db')
    return conn


def create_table():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS budget (
                        id INTEGER PRIMARY KEY,
                        item TEXT,
                        amount REAL
                    )''')
    conn.commit()
    conn.close()

# agregar un nuevo artículo al presupuesto
def add_item(item, amount):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO budget (item, amount) VALUES (?, ?)", (item, amount))
    conn.commit()
    conn.close()

#  buscar un artículo 
def search_item(item):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budget WHERE item=?", (item,))
    result = cursor.fetchall()
    conn.close()
    return result

# editar articulo
def edit_item(item, new_amount):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("UPDATE budget SET amount=? WHERE item=?", (new_amount, item))
    conn.commit()
    conn.close()

# eliminar un artículo
def delete_item(item):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budget WHERE item=?", (item,))
    conn.commit()
    conn.close()

# principal
def main():
    create_table()

    while True:
        print("\n1. Agregar artículo")
        print("2. Buscar artículo")
        print("3. Editar artículo")
        print("4. Eliminar artículo")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            item = input("Nombre del artículo: ")
            amount = float(input("Cantidad: "))
            add_item(item, amount)
            print("Artículo agregado al presupuesto.")

        elif choice == '2':
            item = input("Nombre del artículo a buscar: ")
            result = search_item(item)
            if result:
                print("Artículo encontrado:", result)
            else:
                print("Artículo no encontrado.")

        elif choice == '3':
            item = input("Nombre del artículo a editar: ")
            new_amount = float(input("Nueva cantidad: "))
            edit_item(item, new_amount)
            print("Artículo editado correctamente.")

        elif choice == '4':
            item = input("Nombre del artículo a eliminar: ")
            delete_item(item)
            print("Artículo eliminado correctamente.")

        elif choice == '5':
            print("nos vemos!")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
