# models/predio.py

from sqlalchemy import Integer, String
from geoalchemy2 import Geometry
from db import Db  # o directamente `from db import db` si usas la versión simplificada

class Predio(Db.db.Model):  # si usas `from db import db` directo, usa: db.Model
    __tablename__ = 'predio'
    __table_args__ = {'schema': 'public'}  # opcional si el esquema es 'public'

    id = Db.db.Column(Integer, primary_key=True)
    nombre = Db.db.Column(String(100), nullable=False)
    localizacion = Db.db.Column(Geometry(geometry_type='POINT', srid=4326))  # usa SRID correcto
    estado = Db.db.Column(Integer)
    celular = Db.db.Column(String(13))
    direccion = Db.db.Column(String(150))

    def __init__(self, nombre, localizacion=None, estado=None, celular=None, direccion=None):
        self.nombre = nombre
        self.localizacion = localizacion
        self.estado = estado
        self.celular = celular
        self.direccion = direccion
