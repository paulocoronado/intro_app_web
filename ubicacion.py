from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape

# Instancia de SQLAlchemy
db = SQLAlchemy()

# Modelo para la tabla 'ubicacion'
class Ubicacion(db.Model):
    __tablename__ = 'ubicacion'

    # Columna 'id': clave primaria con incremento automático
    id = db.Column(db.Integer, primary_key=True)

    # Columna 'localizacion': tipo geométrico Point (SRID 4326 para coordenadas geográficas)
    localizacion = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)

    # Columna 'nombre': texto de máximo 100 caracteres, obligatorio
    nombre = db.Column(db.String(100), nullable=False)

    # Columna 'estado': número entero, opcional
    estado = db.Column(db.Integer)

    # Columna 'direccion': texto de máximo 150 caracteres, opcional
    direccion = db.Column(db.String(150))

    # Columna 'celular': texto de máximo 13 caracteres, opcional
    celular = db.Column(db.String(13))

    def __repr__(self):
        return f'<Ubicacion {self.id} - {self.nombre}>'

    def to_dict(self):
        """
        Convierte la instancia en un diccionario, incluyendo el punto como lat/lon.
        """
        point = to_shape(self.localizacion)
        return {
            'id': self.id,
            'nombre': self.nombre,
            'latitud': point.y,
            'longitud': point.x,
            'estado': self.estado,
            'direccion': self.direccion,
            'celular': self.celular
        }
