import serial, time, json, requests

# Esta función enviará el JSON al servidor web local
def enviar_json_al_servidor(json_data):
    url = "http://localhost:5000/Sistema_B/actualizar_cliente"  # Reemplaza con la URL de tu servidor
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, data=json_data, headers=headers)
        response.raise_for_status()  # Verifica si hay errores en la respuesta HTTP

        print("Datos enviados exitosamente al servidor.")
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar datos al servidor: {e}")


def asignar_nombre(llave):
    # Aquí puedes implementar la lógica para asignar un nombre a la llave
    # y almacenar esta información en algún lugar, como un diccionario o una base de datos.
    print(f"Asignando nombre a la llave {llave} ")
    nuevo_nombre = input(f"Asignar un nombre a la llave {llave_rfid}: ")
    nuevo_Apellido1 = input(f"Asignar un Apellido 1 : ")
    nuevo_Apellido2 = input(f"Asignar un Apellido 2: ")
    direccion = input(f"Direccion: ")
    telefono = input(f"telefono: ")
    observacion = input(f"observaciones ejemplo nuevo cluente o cliente habitual: ")
    # llaves_con_nombre[llave_rfid] = nuevo_nombre
    nuevo_cliente = {
        "identificacion": llave,
        "pais": "México",
        "nombre": nuevo_nombre,
        "apellido1": nuevo_Apellido1,
        "apellido2": nuevo_Apellido2,
        "direccion": direccion,
        "telefono": telefono,
        "observaciones": observacion
    }
    
    clientes.append(nuevo_cliente)
    with open('Sistema_B/clientes.json', 'w') as f:
        json.dump(data, f)
    print(f"Nombre asignado a la llave {llave_rfid}: {nuevo_nombre}")
def asignar_nuevo_nombre(llave):

        print(f"Cliente existente encontrado:")
        print(f"Identificación: {cliente_existente['identificacion']}")
        print(f"Nombre actual: {cliente_existente['nombre']}")
        print(f"Apellido 1 actual: {cliente_existente['apellido1']}")
        print(f"Apellido 2 actual: {cliente_existente['apellido2']}")
        print(f"Dirección actual: {cliente_existente['direccion']}")
        print(f"Teléfono actual: {cliente_existente['telefono']}")
        print(f"Observaciones actuales: {cliente_existente['observaciones']}")

        # Preguntar al usuario si desea editar los datos
        editar = input("¿Deseas editar los datos de este cliente? (si/no): ").lower()

        if editar == 'si':
            # Editar los campos deseados
            nuevo_nombre = input(f"Asignar un nuevo nombre a la llave {llave}: ")
            nuevo_apellido1 = input(f"Asignar un nuevo Apellido 1: ")
            nuevo_apellido2 = input(f"Asignar un nuevo Apellido 2: ")
            nueva_direccion = input(f"Asignar una nueva dirección: ")
            nuevo_telefono = input(f"Asignar un nuevo teléfono: ")
            nuevas_observaciones = input(f"Asignar nuevas observaciones: ")

            # Modificar los campos en el cliente existente
            cliente_existente['nombre'] = nuevo_nombre
            cliente_existente['apellido1'] = nuevo_apellido1
            cliente_existente['apellido2'] = nuevo_apellido2
            cliente_existente['direccion'] = nueva_direccion
            cliente_existente['telefono'] = nuevo_telefono
            cliente_existente['observaciones'] = nuevas_observaciones

            # Actualizar el archivo JSON después de la edición
            with open('Sistema_B/clientes.json', 'w') as f:
                json.dump(data, f)

            print(f"Datos del cliente actualizados correctamente.")
        else:
            print("Datos del cliente no editados.")

def cambiar_nombre(llave):
    
    # Aquí puedes implementar la lógica para cambiar el nombre asignado a la llave.
    print(f"La llave {llave} ya tiene un nombre {cliente_existente['nombre']}. ¿Deseas cambiarlo?")

    respuesta = input("Ingresa el nuevo nombre (o 'no' para mantener el actual): ")
    
    if respuesta.lower() != 'no':
        # Aquí puedes actualizar el nombre en la base de datos o en tu lógica de almacenamiento.
        asignar_nuevo_nombre(llave)
        print(f"Nombre de la llave {llave} actualizado a: {cliente_existente['nombre']}")
    else:
        print("Nombre de la llave no cambiado.")

# Configura el puerto serial
puerto_serial = serial.Serial('COM4', 9600)  # Reemplaza 'COMX' con el puerto correcto
datos = puerto_serial.readline()

# read JSON file
with open('Sistema_B/clientes.json', 'r') as f:
    data = json.load(f)

while True:
    if puerto_serial.in_waiting > 0:
        # Lee la llave RFID desde el puerto serial
        llave_rfid = puerto_serial.read(8).hex().upper()
        print(f"Llave RFID detectada: {llave_rfid}")

        # Verifica si la llave ya tiene un nombre asignado
        # y realiza las acciones correspondientes
        clientes = data.get('clientes', [])
        cliente_existente = next((cliente for cliente in clientes if cliente['identificacion'] == llave_rfid), None)

        if cliente_existente:
            cambiar_nombre(llave_rfid)
        else:
            asignar_nombre(llave_rfid)
            

         # Esperar a que se acerque otra llave antes de continuar
        print("Esperando a que se acerque otra llave...")
        while puerto_serial.in_waiting == 0:
            pass  # Esperar hasta que llegue otra señal desde el puerto serial

        # Limpiar el buffer del puerto serial antes de procesar la próxima llave
        puerto_serial.read(puerto_serial.in_waiting)