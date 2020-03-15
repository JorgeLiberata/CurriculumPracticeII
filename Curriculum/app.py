from flask import Flask, render_template


app = Flask(__name__)

title = {'datos': 'Datos Personales', 'formacion':'Formacion Profesional', 
     'experiencia': 'Experiencia Profesional', 'habilidades':'Habilidades'}
    
     

@app.route('/')
def DatosPersonales():
    datos = [
        {'cedula':'223-0083422-2', 'nombres':'Jorge Luis', 'apellidos' : 'Liberata Garcia', 'edad':'30', 
        'direccion': 'Res. Buenaventuranza, Edif. 8 Apt. 104', 'ciudad':'Santo Domingo Norte', 
        'pais':'Republica Dominicana'}
    ]    
    return render_template('datos.html', datos = datos, title = title) 


@app.route('/formacion')
def Formacion():
    formacion = ['Basica: Escuela Fe y Alegria', 
                 'Bachiller: Tecnico Profesional en Informatica - INPHA', 
                 'Operador Manofactura Industrial', 
                 'Instalacion y Rep. de Lineas Telefonicas',
                 'Tecnologo en Desarrollo de Software - ITSC'
                ]
    return render_template('formacion.html',formacion = formacion, title = title) 

@app.route('/experiencia')
def Experiencia():
    experiencias = ['MercaSID: Operador Manufactura', 'Altice: Helpdesk', 'HST Soluciones: Desarrollador AS400']
      
    return render_template('experiencia.html', experiencias = experiencias, title = title) 

@app.route('/habilidades')
def habilidades():
    habilidades = ['Empacador', 
                   'Vendedor',
                    'Taxista'
           ]    
    return render_template('habilidades.html', habilidades = habilidades, title = title)
