import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
# Ruta para recibir datos
@app.route('Sistema_A/gastos', methods=['POST'])
def clientes():
    try:
        with open('Sistema_A/gastos.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505
@app.route('Sistema_A/recerva_habitac', methods=['POST'])
def clientes():
    try:
        with open('Sistema_A/gastos.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505

@app.route('Sistema_A/tipo_servicio', methods=['POST'])
def clientes():
    try:
        with open('Sistema_A/servicios.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505
@app.route('Sistema_A/tipo_servicio', methods=['POST'])
def clientes():
    try:
        with open('Sistema_A/tipo_servicio.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505

########################################################################################################################
#                    SEGUNDO SERVIDOR CARPETA COMPARTIDA                                                 
#######################################################################################################################
@app.route('Sistema_B/actualizar_cliente', methods=['POST'])
def actualizar_cliente():
    try:
        nuevo_data = request.json  # Obtiene los datos JSON del cuerpo de la solicitud
        data.update(nuevo_data)  # Actualiza los datos existentes con los nuevos datos

        with open('Sistema_B/clientes.json', 'w') as f:
            json.dump(data, f)  # Guarda el archivo clientes.json
            

        return jsonify({"mensaje": "Datos actualizados correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('Sistema_B/clientes', methods=['POST'])
def clientes():
    try:
        with open('Sistema_B/clientes.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505
@app.route('Sistema_B/habitaciones', methods=['POST'])
def clientes():
    try:
        with open('Sistema_B/habitacions.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505

@app.route('Sistema_B/paises', methods=['POST'])
def clientes():
    try:
        with open('Sistema_B/paises.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505
@app.route('Sistema_B/precio_habitacion', methods=['POST'])
def clientes():
    try:
        with open('Sistema_B/precio_habitacion.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505
@app.route('Sistema_B/temporada', methods=['POST'])
def clientes():
    try:
        with open('Sistema_B/temporada.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}, 505
    




if __name__ == '__main__':
    app.run()
