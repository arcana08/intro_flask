# data acces object
from flask import current_app as app
from conexion.Conexion import Conexion

class CiudadDao:
    def getCiudades(self):
        ciudadSQL="""
        select * 
        from ciudades
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ciudadSQL)
            lista_ciudades = cur.fetchall()
            lista_ordenada = []
            for item in lista_ciudades:
                lista_ordenada.append({
                    "id_ciudades": item[0],
                    "ciu_nombre": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()
            
    def getCiudadById(self, id):

        ciudadSQL = """
        SELECT id_ciudades, ciu_nombre
        FROM ciudades WHERE id_ciudades=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ciudadSQL, (id,))
            ciudadEncontrada = cur.fetchone()
            return {
                    "id_ciudades": ciudadEncontrada[0],
                    "ciu_nombre": ciudadEncontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()
            
    def guardarCiudad(self,ciudad):
        insertCiudadSQL = """
        INSERT INTO ciudades (ciu_nombre) VALUES(%s)
        """
        conexion= Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(insertCiudadSQL, (ciudad,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)

        finally:
            cur.close()
            con.close()

            
        return False
    def updateCiudad(self, id, descripcion):

        updateCiudadSQL = """
        UPDATE ciudades
        SET ciu_nombre=%s
        WHERE id_ciudades=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCiudadSQL, (descripcion, id,))
            con.commit()

            return True

        except con.Error as e:
            app.logger.info(e)

        finally:
            cur.close()
            con.close()

        return False
    
    def deleteCiudad(self, id):

        updateCiudadSQL = """
        DELETE FROM ciudades
        WHERE id_ciudades=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCiudadSQL, (id,))
            con.commit()

            return True

        except con.Error as e:
            app.logger.info(e)

        finally:
            cur.close()
            con.close()

        return False