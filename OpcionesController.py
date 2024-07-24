from flask import Flask, request, jsonify

from Ejercicio.ConexionBD import ConexionBD

app = Flask(__name__)

class usuariosController:
    # GetOpciones
    @app.route('/api/opciones', methods=['GET'])
    def get_opciones():
        return jsonify(ConexionBD.GetOpciones())

    # GetUsuario
    @app.route('/api/opciones/<int:id>', methods=['GET'])
    def get_opcion(id):
        return jsonify(ConexionBD.GetOpcion(id))

    # Post
    @app.route('/api/opciones', methods=['POST'])
    def post_opcion():
        data = request.get_json()
        ConexionBD.PostUsuario(data)
        return 'Opcion added', 201

    # Put
    @app.route('/api/opciones/<int:opcionmodificacion>', methods=['PUT'])
    def put_opcion(opcionmodificacion):
        data = request.get_json()
        ConexionBD.PutUsuario(opcionmodificacion, data)
        return 'Opcion updated', 200

    # Delete
    @app.route('/api/opciones/<int:>', methods=['DELETE'])
    def delete_opcion(id_opcion, opcionmodificacion):
        ConexionBD.DeleteUsuario(id_opcion, opcionmodificacion)
        return 'Opcion deleted', 200

if __name__ == '__main__':
    app.run()