import http.server
import socketserver
import time
from threading import Thread

# Función para iniciar un servidor web en un puerto específico durante una duración determinada
def start_server(port=5000, duration=5*60):
    # Configurar el manejador de las solicitudes HTTP usando SimpleHTTPRequestHandler
    handler = http.server.SimpleHTTPRequestHandler

    # Crear el objeto del servidor TCP
    httpd = socketserver.TCPServer(("", port), handler)

    print(f"Servidor web funcionando en el puerto {port}")

    try:
        # Iniciar el servidor  separado para permitir la espera
        server_thread = Thread(target=httpd.serve_forever)
        server_thread.start()

        # Esperar durante el tiempo especificado
        time.sleep(duration)
    except KeyboardInterrupt:
        pass
    finally:
        # Detener el servidor después de que haya pasado el tiempo de duración
        httpd.shutdown()
        server_thread.join()
        print(f"Servidor web detenido después de {duration} segundos")

# Función pex6 que se puede utilizar para iniciar el servidor web con parámetros específicos
def pex6():
    start_server(port=5000, duration=5*60)  # Llama a start_server con puerto 5000 y duración de 5 minutos

# Punto de entrada principal del programa
if __name__ == "__main__":
    start_server()  # Llama a start_server con los valores predeterminados
