from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return "hola desde backend"
           
@app.route('/contacto')
def contacto():
    return "<h3>Introduciendo html desde el servidor</h3>"          

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')

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

if __name__=='__main__':
    app.run(debug=True)