# Challenge Mercadolibre 


Api con Flask-Redis con imagen de de docker 

Basado en alpine que es más pequeña


Requisitos 

```
Docker
docker-compose
```

Se pueden instalar desde:
```
[Docker](https://docs.docker.com/install/)

[Docker-Compose](https://docs.docker.com/compose/install/)
```

Para probar la API es necesario descargar el contenido de la repo y navegar a la ruta para lanzarla ejecutando:

```
docker-compose up
```
para crear la imagen que contiene la aplicación.




La API va a correr en localhost puerto 5000 (http://localhost:5000/api/queue/*)

Los endpoints implementados son:


```
Endpoint: /api/queue/pop
Metodo: POST
Función: Saca el ultimo job de la cola de tareas
Prueba: curl -XPOST http://127.0.0.1:5000/api/queue/pop
```
```
Endpoint: /api/queue/count
Metodo: GET
Función: Devuelve la lista de jobs actuales en cola
Prueba: curl -XGET http://127.0.0.1:5000/api/queue/count
```
```
Endpoint: /api/queue/push
Metodo: POST
Función: pushea el cuerpo en JSON de la solicitud a la cola de Redis.
Prueba: curl -XPOST http://127.0.0.1:5000/api/queue/push
```



NOTA: La respuesta del metodo push sufre el siguiente cambio:

```
{
  ‘status’: ‘ok’,
}

Se cambia a: 

{
  ‘status’: ‘Created’,
}

Ya que esta respuesta http es mas adecuada para el metodo pues este "crea" una tarea y esto representa mejor el status code 201. 
```


