import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#----------------------------------------------------------
#LAS INSTRUCCIONES PIDIERON UNA TABLA USER... AQUI LA TENEMOS.
# Tabla User
class User(Base):
    __tablename__ = 'user'

    id             = Column(Integer, primary_key=True)
    nombreUsuario  = Column(String(80), unique=True, nullable=False)
    correo         = Column(String(120), unique=True, nullable=False)
    claveAcceso    = Column(String(128), nullable=False)
    favoritos      = relationship('Favoritos', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

#------------------------------------------------------------


# Tabla Character
class Character(Base):
    __tablename__ = 'character'

    id              = Column(Integer, primary_key=True)
    nombrePersonaje = Column(String(80), nullable=False)
    description     = Column(Text, nullable=True)
    sexo            = Column(String(1), nullable=True)
    cumple          = Column(String(20), nullable=True)
    favoritos       = relationship('Favoritos', backref='character', lazy=True)

    def __repr__(self):
        return f'<Character {self.name}>'
#----------------------------------------------------------

# Tabla Planet
class Planet(Base):
    __tablename__ = 'planet'
    id        = Column(Integer, primary_key=True)
    nombre    = Column(String(80), nullable=False)
    clima     = Column(String(50), nullable=True)
    terreno   = Column(String(50), nullable=True)
    poblacion = Column(String(50), nullable=True)
    favoritos = relationship('Favoritos', backref='planet', lazy=True)

    def __repr__(self):
        return f'<Planet {self.name}>'
#----------------------------------------------------------

# Tabla Favorites
# LAS INDICACIONES PEDIAN QUE SE PUEDIERAN GUARDAR LOS FAVORITOS DE LOS BLOG USERS CON LOS PLANETAS Y PERSONAJES,AQUI ESTA...
class Favoritos(Base):
    __tablename__ = 'favoritos'
    id           = Column(Integer, primary_key=True)
    user_id      = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id    = Column(Integer, ForeignKey('planet.id'), nullable=True)

    def __repr__(self):
        return f'<Favorite User: {self.user_id}, Character: {self.character_id}, Planet: {self.planet_id}>'


#-----------------------------------------------------------
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
