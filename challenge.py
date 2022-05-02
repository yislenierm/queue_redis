
#Dependencias 
from flask import Flask, request, jsonify
import redis
import json
from rq import Queue
import time


# Conección a la APP
miapp = Flask(__name__)
cache_redis = redis.Redis(host='redis', port=6379) ## Conectar a redis
cola = Queue(connection=cache_redis)               ## Crear la cola

# Metodo: POST
# Path: /api/queue/pop
# Respuesta: 200 en caso de éxito y en caso de error un status code correspondiente al tipo de error
# Body Respuesta:

# {
#   ‘status’: ‘ok’,
#   ‘message’: <msg>
# }
 
@miapp.route('/api/queue/pop', methods=["POST"])   ##ruta metodo pop
def pop():
	try:
		cola_len=len(cola)          
		IDscola = cola.job_ids
		fin_cola = IDscola[len(cola)-1]
		tarea = cola.fetch_job(fin_cola)
		jobString = tarea.description   
		tarea.delete()
		return {'status':'ok'},200
	except:
		return {'status':'Error'},410   ## Gone no existen items para eliminar



# Metodo: GET
# Path: /api/queue/count
# Respuesta: 200 en caso de éxito y en caso de error un status code correspondiente al tipo de error
# Body Respuesta:

# {
#   ‘status’: ‘ok’,
#   ‘count’: <count>,
# }

@miapp.route("/api/queue/count", methods=["GET"])    ##ruta metodo count
def count():
	return {'count':len(cola),'status':'ok'},200    ## devuelve las tareas en cola


## Simulando el tiempo de ejecución de tarea
def tarea_simulada (sim):
	espera = 5
	time.sleep(espera)
	return sim



# Metodo: POST
# Path: /api/queue/push
# Body: <msg> . Respuesta: 201 en caso de éxito y en caso de error un status code correspondiente al tipo de error . Body Respuesta:

# {
#   ‘status’: ‘ok’,
# }

@miapp.route("/api/queue/push", methods=["POST"])   ##ruta metodo push
def push():
	try:	
		retornoreq = request.get_json()              ## Manda el request 
		cola.enqueue(tarea_simulada,retornoreq)      ## Pasa la tarea al worker
		return {'status':'Created'}, 201			 ## 201 Creado Devuelve el estado
	except:
		return {'status':'Error'},501               ## 501 No implementado 



if __name__ == "__main__":
    miapp.run()

## agregar el health check ## 