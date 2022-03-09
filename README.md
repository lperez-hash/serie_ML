## Proceso de despliegue Local(PRUEBAS)

1. Desde la carpeta raiz del proyecto ejecute el comando

conda create --name ENV_PRB --file requirements.txt

2. Seleccione el ambiente creado

conda activate ENV_PRB

3. Levante el servidor (Por defecto en localhost:8000)

uvicorn main:app

## Documentación

Puede acceder a ella por medio de los endpoint:
* /docs
* /redoc

## App desplegada en GCP

URL     https://apiml1.uc.r.appspot.com/
