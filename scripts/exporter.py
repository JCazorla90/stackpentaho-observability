from prometheus_client import start_http_server, Gauge
import time
import random

# Definimos las métricas
filas_procesadas = Gauge('filas_procesadas', 'Número de filas procesadas')
estado_job = Gauge('estado_job', 'Estado del job (0=OK, 1=ERROR)')

def ejecutar_job():
    filas = random.randint(100, 1000)
    status = random.choice([0, 0, 0, 1])  # Mayor probabilidad de OK

    filas_procesadas.set(filas)
    estado_job.set(status)

if __name__ == '__main__':
    start_http_server(9100)
    print("Exporter escuchando en http://localhost:9100/metrics")
    while True:
        ejecutar_job()
        time.sleep(10)
