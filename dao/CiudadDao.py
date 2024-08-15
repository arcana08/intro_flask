# data acces object
from conexion.Conexion import Conexion

class CiudadDao:
    def getCiudades(self):
        ciudadSQL="""
        select * 
        from ciudades
        """
        conexion = Conexion()
        con= conexion.getConexion()
        try:
            pass
        except:
            pass
        finally:
            pass
        