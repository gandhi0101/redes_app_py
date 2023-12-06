import serial, time

def asignar_nombre(llave):
    # Aquí puedes implementar la lógica para asignar un nombre a la llave
    # y almacenar esta información en algún lugar, como un diccionario o una base de datos.
    print(f"Asignando nombre a la llave {llave}...")
    nuevo_nombre = input(f"Asignar un nombre a la llave {llave_rfid}: ")
    llaves_con_nombre[llave_rfid] = nuevo_nombre
    print(f"Nombre asignado a la llave {llave_rfid}: {nuevo_nombre}")

def cambiar_nombre(llave):
    # Aquí puedes implementar la lógica para cambiar el nombre asignado a la llave.
    print(f"La llave {llave} ya tiene un nombre {llaves_con_nombre[llave_rfid]}. ¿Deseas cambiarlo?")

    respuesta = input("Ingresa el nuevo nombre (o 'no' para mantener el actual): ")
    
    if respuesta.lower() != 'no':
        # Aquí puedes actualizar el nombre en la base de datos o en tu lógica de almacenamiento.
        llaves_con_nombre[llave_rfid] = respuesta
        print(f"Nombre de la llave {llave} actualizado a: {llaves_con_nombre[llave_rfid]}")
    else:
        print("Nombre de la llave no cambiado.")

# Configura el puerto serial
puerto_serial = serial.Serial('COM4', 9600)  # Reemplaza 'COMX' con el puerto correcto
datos = puerto_serial.readline()
llaves_con_nombre = {}

while True:
    if puerto_serial.in_waiting > 0:
        # Lee la llave RFID desde el puerto serial
        llave_rfid = puerto_serial.read(8).hex().upper()
        print(f"Llave RFID detectada: {llave_rfid}")

        # Verifica si la llave ya tiene un nombre asignado
        # y realiza las acciones correspondientes
        if llave_rfid in llaves_con_nombre:
            cambiar_nombre(llave_rfid)
        else:
            asignar_nombre(llave_rfid)

         # Esperar a que se acerque otra llave antes de continuar
        print("Esperando a que se acerque otra llave...")
        while puerto_serial.in_waiting == 0:
            pass  # Esperar hasta que llegue otra señal desde el puerto serial

        # Limpiar el buffer del puerto serial antes de procesar la próxima llave
        puerto_serial.read(puerto_serial.in_waiting)