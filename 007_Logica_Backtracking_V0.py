#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 7/59 Backtracking

import matplotlib.pyplot as plt

# Función para verificar si una reina puede ser colocada en la posición actual
def is_safe(board, row, col):
    # Verificar si hay una reina en la misma columna
    for i in range(row):
        if board[i] == col:
            return False

    #Verificamos las diagonales superiores izquierda
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    #Verificamos las diagonales superiores derecha
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False

    return True

# Función recursiva para resolver el problema de las N reinas usando backtracking
def solve_n_queens(board, row):
    n = len(board)
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1):
                return True
            board[row] = -1

    return False

# Función para dibujar el tablero con las reinas colocadas
def draw_board(board):
    n = len(board)
    chessboard = [[(i + j) % 2 for i in range(n)] for j in range(n)]
    for i in range(n):
        chessboard[i][board[i]] = 2  # Marcar la posición de la reina en el tablero

    plt.matshow(chessboard, cmap="binary")
    plt.xticks([])
    plt.yticks([])
    plt.show()

# Función principal
def main():
    n = 8  # Tamaño del tablero (en este caso, un tablero de 8x8)
    board = [-1] * n  # Inicializar el tablero con -1 (sin reinas colocadas)

    if solve_n_queens(board, 0):
        print("Solución encontrada:")
        print(board)
        draw_board(board)
    else:
        print("No se encontró solución.")

if __name__ == "__main__":
    main()
