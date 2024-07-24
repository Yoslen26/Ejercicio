from flask import Flask, request, jsonify

from Ejercicio.ConexionBD import ConexionBD

app = Flask(__name__)

class usuariosController:
    # GetUsuarios
    @app.route('/api/usuarios', methods=['GET'])
    def get_usuarios():
        return jsonify(ConexionBD.GetUsuarios())

    # GetUsuario
    @app.route('/api/usuarios/<int:id>', methods=['GET'])
    def get_usuario(id):
        return jsonify(ConexionBD.GetUsuario(id))

    # Post
    @app.route('/api/usuarios', methods=['POST'])
    def post_usuario():
        data = request.get_json()
        ConexionBD.PostUsuario(data)
        return 'Usuario added', 201

    # Put
    @app.route('/api/usuarios/<int:Usuariomodificacion>', methods=['PUT'])
    def put_usuario(Usuariomodificacion):
        data = request.get_json()
        ConexionBD.PutUsuario(Usuariomodificacion, data)
        return 'Usuario updated', 200

    # Delete
    @app.route('/api/usuarios/<int:idUsuario>/<int:idUsuariomodificacion>', methods=['DELETE'])
    def delete_usuario(idUsuario, idUsuariomodificacion):
        ConexionBD.DeleteUsuario(idUsuario, idUsuariomodificacion)
        return 'Usuario deleted', 200

if __name__ == '__main__':
    app.run()