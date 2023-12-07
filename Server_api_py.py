import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/Sistema_B/actualizar_cliente', methods=['POST'])
def actualizar_cliente():
    try:
        #nuevo_data = request.json  # Obtiene los datos JSON del cuerpo de la solicitud
        #data.update(nuevo_data)  # Actualiza los datos existentes con los nuevos datos
        id = request.form.get('ide')
        nuevo_nombre = request.form.get('nombre')
        nuevo_apellido1 = request.form.get('apellido1')
        nuevo_apellido2 = request.form.get('apellido2')
        nueva_direccion = request.form.get('direccion')
        nuevo_telefono = request.form.get('telefono')
        nuevas_observaciones = request.form.get('observaciones')


        with open('Sistema_B/clientes.json', 'r') as f:
            data = json.load(f)
        clientes = data.get('clientes', [])
        
        cliente_existente = next((cliente for cliente in clientes if cliente['identificacion'] == id), None)
        if cliente_existente:
            cliente_existente['nombre'] = nuevo_nombre
            cliente_existente['apellido1'] = nuevo_apellido1
            cliente_existente['apellido2'] = nuevo_apellido2
            cliente_existente['direccion'] = nueva_direccion
            cliente_existente['telefono'] = nuevo_telefono
            cliente_existente['observaciones'] = nuevas_observaciones

            with open('Sistema_B/clientes.json', 'w') as f:
                json.dump(data, f)
        else:
            print("No existe el cliente")

        with open('Sistema_B/clientes.json', 'w') as f:
            json.dump(data, f)  # Guarda el archivo clientes.json
            

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def obtener_datos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return{"error": str(e)}, 500
    

# Rutas para Sistema_A
@app.route('/Sistema_A/<archivo>', methods=['POST'])
def sistema_a(archivo):
    ruta = f"Sistema_A/{archivo}.json"
    return obtener_datos(ruta)


########################################################################################################################
#                    SEGUNDO SERVIDOR CARPETA COMPARTIDA                                                 
#######################################################################################################################




# Rutas para Sistema_B
@app.route('/Sistema_B/<archivo>', methods=['POST'])
def sistema_b(archivo):
    ruta = f"Sistema_B/{archivo}.json"
    return obtener_datos(ruta)






if __name__ == '__main__':
    app.run()
