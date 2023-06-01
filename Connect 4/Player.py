from socket import *
import numpy as np
import pygame
import sys
import math
import threading


BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7
host = '127.0.0.1'
port = 8000
game_over = False
turn = False
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

def waiting_for_connection():
    global conn, addr
    conn, addr = sock.accept()
    print('client is connected')
    create_thread(receive_data)

def receive_data():
    global turn
    while True:
        data = conn.recv(1024).decode()
        data = data.split('-')
        row = int(data[0])
        col = int(data[1])
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            game_over = True
        if board[row][col] == 0:
            board[row][col] = 2


create_thread(waiting_for_connection)


# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 640
HEIGHT = 480
GRID_SIZE = 80
ROWS = 6
COLUMNS = 7
FPS = 30
    
# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

# Connect to the server
server_address = ('localhost', 8888)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


def draw_board(board):
    window.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLUMNS):
            pygame.draw.rect(window, BLUE, (col * GRID_SIZE, row * GRID_SIZE + GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.circle(window, BLACK,
                               (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE + GRID_SIZE // 2), 40)

    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == 1:
                pygame.draw.circle(window, RED,
                                   (col * GRID_SIZE + GRID_SIZE // 2, HEIGHT - (row * GRID_SIZE + GRID_SIZE // 2)), 40)
            elif board[row][col] == 2:
                pygame.draw.circle(window, YELLOW,
                                   (col * GRID_SIZE + GRID_SIZE // 2, HEIGHT - (row * GRID_SIZE + GRID_SIZE // 2)), 40)
    pygame.display.update()


def send_move(col):
    client_socket.send(pickle.dumps(col))


def receive_data():
    data = client_socket.recv(1024)
    return pickle.loads(data)


def game_loop():
    board = [[0] * COLUMNS for _ in range(ROWS)]
    turn = 1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x = event.pos[0]
                col = pos_x // GRID_SIZE
                if board[0][col] == 0:
                    send_move(col)

        board = receive_data()
        draw_board(board)

        if check_win(board, 1):
            print("Player 1 wins!")
            running = False
        elif check_win(board, 2):
            print("Player 2 wins!")
            running = False

        pygame.display.update()
        pygame.time.Clock().tick(FPS)


def check_win(board, player):
    # Check horizontally
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and \
                    board[row][col + 3] == player:
                return True

    # Check vertically
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and \
                    board[row + 3][col] == player:
                return True

    # Check diagonally (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and \
                    board[row + 3][col + 3] == player:
                return True

    # Check diagonally (top-right to bottom-left)
    for row in range(ROWS - 3):
        for col in range(3, COLUMNS):
            if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == player and \
                    board[row + 3][col - 3] == player:
                return True

    return False


game_loop()
