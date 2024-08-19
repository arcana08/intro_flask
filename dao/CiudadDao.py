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
        cur = con.cursor
        try:
            cur.execute(ciudadSQL)
            lista_ciudades = cur.fetchall()
            return lista_ciudades
        except con.Error as e :
            print(e)
        finally:
            cur.close()
            con.close()
            
    def guardarCiudad(self,ciudad,pais):
        insertCiudadSQL = """
        insert into ciudades (ciu_nombre,id_paises) values(%s,%s)
        """
        conexion= Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(insertCiudadSQL, (ciudad,pais))
            con.commit()
            return True
        except con.Error as e :
            print(e)
            
        finally:
            cur.close()
            con.close()
            
        return False