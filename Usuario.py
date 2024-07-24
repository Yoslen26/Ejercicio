class Usuario:
    def __init__(self, id_usuario, codigo, nombres, apellidos, mail, contrasena, estado, fecha_ultima_conexion,
                 usuario_creacion, fecha_creacion, usuario_modificacion, fecha_modificacion, fecha_nacimiento):
        self.id_usuario = id_usuario
        self.codigo = codigo
        self.nombres = nombres
        self.apellidos = apellidos
        self.mail = mail
        self.contrasena = contrasena
        self.estado = estado
        self.fecha_ultima_conexion = fecha_ultima_conexion
        self.usuario_creacion = usuario_creacion
        self.fecha_creacion = fecha_creacion
        self.usuario_modificacion = usuario_modificacion
        self.fecha_modificacion = fecha_modificacion
        self.fecha_nacimiento = fecha_nacimiento