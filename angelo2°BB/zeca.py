import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura = 800
altura = 600

# Define a cor do retângulo e do fundo
cor_retangulo = (0, 128, 255)  # Azul
cor_fundo = (0, 0, 0)         # Preto

# Cria a janela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Programa Simples em Pygame')

# Define a posição e tamanho do retângulo
retangulo_x = largura // 2
retangulo_y = altura // 2
retangulo_largura = 100
retangulo_altura = 50
velocidade = 5

# Loop principal do jogo
while True:
    # Processa os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        retangulo_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        retangulo_x += velocidade
    if teclas[pygame.K_UP]:
        retangulo_y -= velocidade
    if teclas[pygame.K_DOWN]:
        retangulo_y += velocidade

    # Atualiza a tela
    tela.fill(cor_fundo)
    pygame.draw.rect(tela, cor_retangulo, (retangulo_x, retangulo_y, retangulo_largura, retangulo_altura))
    pygame.display.flip()

    # Define a taxa de atualização do jogo
    pygame.time.Clock().tick(30)