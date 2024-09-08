from flask import Flask, render_template, request, redirect, url_for, flash
from dao.CiudadDao import CiudadDao

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/inicio')
def inicio():
    return "hola desde backend"
           
@app.route('/contacto')
def contacto():
    return "<h3>Introduciendo html desde el servidor</h3>"          

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')

@app.route('/ciudades')
def ciudades():
    return render_template('ciudades.html')

@app.route('/ciudades-index')
def ciudades_index():
    ciudadDao = CiudadDao()
    lista_ciudades = ciudadDao.getCiudades()
    return render_template('ciudades-index.html', lista_ciudades=lista_ciudades)

@app.route('/guardar-cliente',methods=['POST'])
def guardarCliente():
    print(request.form)
    nombrecliente = request.form.get('nombre')
    mailcliente = request.form.get('email')
    telefonocliente = request.form.get('telefono')
    direccioncliente = request.form.get('direccion')
    return f"""<h3>Cliente Registrado:</h3>
            <p><strong>Nombre:</strong> {nombrecliente}</p>
            <p><strong>Email:</strong> {mailcliente}</p>
            <p><strong>Teléfono:</strong> {telefonocliente}</p>
            <p><strong>Dirección:</strong> {direccioncliente}</p>"""
            
@app.route('/guardar-ciudad',methods=['POST'])
def guardarCiudad():
    
    ciudad = request.form.get('txt_ciudad').strip()
    if ciudad == None or len(ciudad) < 1:
        flash('Debe escribir nombre de la ciudad', 'warning')

        return redirect(url_for('ciudades'))
    Ciudaddao = CiudadDao()
    Ciudaddao.guardarCiudad(ciudad.upper())
    
    flash('guardado exitoso','success')
    
    return redirect(url_for('ciudades'))
    
@app.route('/ciudades-editar/<id>')
def ciudadesEditar(id):
    ciudaddao = CiudadDao()
    return render_template('ciudades-editar.html', ciudad=ciudaddao.getCiudadById(id))

@app.route('/actualizar-ciudad', methods=['POST'])
def actualizarCiudad():
    id = request.form.get('txtIdCiudad')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('ciudadesEditar', id=id))

    # actualizar
    ciudaddao = CiudadDao()
    ciudaddao.updateCiudad(id, descripcion.upper())

    return redirect(url_for('ciudades_index'))

@app.route('/ciudades-eliminar/<id>')
def ciudadesEliminar(id):
    ciudaddao = CiudadDao()
    ciudaddao.deleteCiudad(id)
    return redirect(url_for('ciudades_index'))

if __name__=='__main__':
    app.run(debug=True)