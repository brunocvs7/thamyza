from thamyza import app

from flask import request, render_template

@app.route("/")

def index():
	return render_template('Index.html')

@app.route("/analisador_virtual")

def analisador():
	import h2o
	h2o.init()
	Vazao = request.args['Vazao']
	Turbidez_Agua_Bruta_x = request.args['Turbidez_Agua_Bruta']
	Dosagem_Coagulante = request.args['Dosagem_Coagulante']
	Vazao = float(Vazao)
	Turbidez_Agua_Bruta_x = float(Turbidez_Agua_Bruta_x)
	Dosagem_Coagulante = float(Dosagem_Coagulante)
	path ='./thamyza/controllers/analisador'
	modelo = h2o.load_model(path)
	teste =h2o.H2OFrame({"Vazao": Vazao, "Turbidez_Agua_Bruta_x": Turbidez_Agua_Bruta_x,"Dosagem_Coagulante": Dosagem_Coagulante})
	Turbidez_Agua_Tratada_x = modelo.predict(teste) 
	Turbidez_Agua_Tratada_x = Turbidez_Agua_Tratada_x.as_data_frame().to_json()
	

	return (Turbidez_Agua_Tratada_x)

@app.route("/dosador_virtual")

def dosador():
	import h2o
	h2o.init()
	Vazao = request.args['Vazao']
	Turbidez_Agua_Bruta_x = request.args['Turbidez_Agua_Bruta']
	Turbidez_Agua_Tratada_x = request.args['Turbidez_Agua_Tratada']
	Vazao = float(Vazao)
	Turbidez_Agua_Bruta_x = float(Turbidez_Agua_Bruta_x)
	Turbidez_Agua_Tratada_x = float(Turbidez_Agua_Tratada_x)
	path ='./thamyza/controllers/dosador'
	modelo = h2o.load_model(path)
	teste =h2o.H2OFrame({"Vazao": Vazao, "Turbidez_Agua_Bruta_x": Turbidez_Agua_Bruta_x,"Turbidez_Agua_Tratada_x":Turbidez_Agua_Tratada_x })
	Dosagem_Coagulante = modelo.predict(teste) 
	Dosagem_Coagulante= Dosagem_Coagulante.as_data_frame().to_json()

	return (Dosagem_Coagulante)