import pyodbc
import cx_Oracle

class ConexionBD:
    conexion = None

    @staticmethod
    def abrir_conexion():
        connection = cx_Oracle.connect("DESKTOP-HB58NUH\SQLEXPRESS", "area", "1521")
        return connection

    @staticmethod
    def get_usuarios():
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.execute("BEGIN SP_GET_USUARIO; END;")
            data = cursor.fetchall()
            return data
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error fetching usuarios:", error.message)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_usuario(id):
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.execute("BEGIN SP_GET_USUARIOU(:id_usuario); END;", id_usuario=id)
            data = cursor.fetchall()
            return data[0] if data else None
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error fetching usuario:", error.message)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def post_usuario(obj_usuario):
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.execute("BEGIN SP_INS_USUARIO(:codigo, :id_usuario, :nombres, :apellidos, :mail, :fecha_nacimiento, :contrasena, :usuario_creacion); END;",
                           codigo=obj_usuario.codigo, id_usuario=obj_usuario.id_usuario, nombres=obj_usuario.nombres, apellidos=obj_usuario.apellidos,
                           mail=obj_usuario.mail, fecha_nacimiento=obj_usuario.fecha_nacimiento, contrasena=obj_usuario.contrasena, usuario_creacion=obj_usuario.usuario_creacion)
            connection.commit()
            print("Usuario posted successfully.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error posting usuario:", error.message)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def put_usuario(usuario_modificacion, obj_usuario):
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.callproc("SP_UPD_USUARIO", [obj_usuario.id_usuario, obj_usuario.codigo, obj_usuario.id_usuario, obj_usuario.nombres, obj_usuario.apellidos, obj_usuario.mail, obj_usuario.fecha_nacimiento, obj_usuario.contrasena, usuario_modificacion])
            connection.commit()
            print("Usuario updated successfully.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error updating usuario:", error.message)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_usuario(id_usuario, id_usuario_modificacion):
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.callproc("SP_DEL_USUARIO", [id_usuario, id_usuario_modificacion])
            connection.commit()
            print("Usuario deleted successfully.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error deleting usuario:", error.message)
        finally:
            cursor.close()
            connection.close()

    #Opciones
    @staticmethod
    def get_opciones():
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.execute("BEGIN SP_GET_OPCION; END;")
            data = cursor.fetchall()
            return data
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error fetching opciones:", error.message)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_opcion(id):
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.execute("BEGIN SP_GET_OPCION(:id_opcion); END;", id_opcion=id)
            data = cursor.fetchall()
            return data[0] if data else None
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error fetching opcion:", error.message)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def post_opcion(obj_opcion):
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.execute("BEGIN SP_INS_OPCIONES(:id_opcion, :verperfil, :editarperfil, :opcionmodificacion); END;",
                           id_opcion=obj_opcion.id_opcion, verperfil=obj_opcion.verperfil, editarperfil=obj_opcion.editarperfil, opcionmodificacion=obj_opcion.opcionmodificacion)
            connection.commit()
            print("Opcion posted.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error posting:", error.message)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def put_opcion(usuario_modificacion, obj_opcion):
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.callproc("SP_UPD_USUARIO", [obj_opcion.id_opcion, obj_opcion.verperfil, obj_opcion.editarperfil, obj_opcion.opcionmodificacion])
            connection.commit()
            print("Usuario updated successfully.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error updating usuario:", error.message)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_opcion(id_opcion, id_opcionmodificacion):
        connection = ConexionBD.abrir_conexion()
        cursor = connection.cursor()
        try:
            cursor.callproc("SP_DEL_USUARIO", [id_opcion, id_opcionmodificacion])
            connection.commit()
            print("Opcion deleted.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Error deleting opcion:", error.message)
        finally:
            cursor.close()
            connection.close()





if __name__ == '__main__':
    app.run()