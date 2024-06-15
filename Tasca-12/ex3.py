import pygame
import random

# Función principal del juego del dinosaurio
def pex3():
    pygame.init()  # Inicializa Pygame

    # Configuración de la pantalla
    SCREEN_WIDTH = 871
    SCREEN_HEIGHT = 489
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    pygame.display.set_caption("Dinosaur Game")  #

    # Cargar imágenes
    ground = pygame.image.load("ground.png").convert()  
    DinoS = pygame.image.load("DinoStart.png")  
    cactus_img = pygame.image.load("Cactus1.png")  

    # Configuración del dinosaurio
    dino_rect = DinoS.get_rect()  # Obtiene el rectángulo del dinosaurio
    dino_rect.topleft = (10, SCREEN_HEIGHT - dino_rect.height - 50)  
    jumping = False  
    jump_velocity = 5
    gravity = 1

    # Configuración de los cactus
    cactus_list = []  # Lista para almacenar los cactus en pantalla
    cactus_timer = 0  # Temporizador para controlar la generación de nuevos cactus
    cactus_interval = 60   # Intervalo de tiempo en frames para generar nuevos cactus

    clock = pygame.time.Clock()  
    done = False  # Variable para controlar el fin del juego

    # Bucle principal del juego
    while not done:
        for event in pygame.event.get():  # Maneja los eventos de Pygame
            if event.type == pygame.QUIT:
                done = True  # Sale del bucle si se cierra la ventana

        # Manejo del salto del dinosaurio
        keys = pygame.key.get_pressed()  # Obtiene el estado de todas las teclas
        if keys[pygame.K_SPACE] and not jumping:  # Si se presiona espacio y no está saltando
            jumping = True
            jump_velocity = 20  

        if jumping: 
            dino_rect.y -= jump_velocity  # Actualiza la posición vertical del dinosaurio
            jump_velocity -= gravity  # Aplica la gravedad al salto
            if dino_rect.y >= SCREEN_HEIGHT - dino_rect.height - 50:  # Si toca el suelo
                dino_rect.y = SCREEN_HEIGHT - dino_rect.height - 50
                jumping = False  # Termina el salto

        # Generar nuevos cactus
        cactus_timer += 1
        if cactus_timer >= cactus_interval:
            cactus_timer = 0
            new_cactus_rect = cactus_img.get_rect()  # Rectángulo del nuevo cactus
            new_cactus_rect.topleft = (SCREEN_WIDTH, SCREEN_HEIGHT - new_cactus_rect.height - 50)

            # Generar velocidad aleatoria para el cactus
            cactus_speed = random.randint(10, 15)  # Velocidades entre 10 y 15 
            cactus_list.append((new_cactus_rect, cactus_speed))  # Agrega el nuevo cactus a la lista

        # Mover los cactus y verificar colisiones
        for cactus_rect, cactus_speed in cactus_list:
            cactus_rect.x -= cactus_speed  # Mueve el cactus hacia la izquierda

            # Detección de colisiones
            if dino_rect.colliderect(cactus_rect):
                print("Game over, se ha acabat el joc")
                done = True  # Termina el juego si hay colisión

        # Eliminar los cactus que han salido de la pantalla
        cactus_list = [(cactus_rect, cactus_speed) for cactus_rect, cactus_speed in cactus_list if cactus_rect.x + cactus_rect.width > 0]

        # Dibujar todo en la pantalla
        screen.blit(ground, (0, 0))  # Dibuja el suelo
        screen.blit(DinoS, dino_rect)  # Dibuja el dinosaurio
        for cactus_rect, _ in cactus_list:
            screen.blit(cactus_img, cactus_rect)  # Dibuja los cactus

        pygame.display.flip()  # Actualiza la pantalla
        clock.tick(30)  

    pygame.quit()  # Cierra Pygame 

# Esta función se llama desde el programa principal para iniciar el juego
if __name__ == "__main__":
    pex3()