import tkinter as tk

def is_safe(board, row, col, N):
    # Provjera da li su kraljice napadnute
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens(board, row, N):
    # Sve kraljice su postavljene
    if row == N:
        return True
    
    for col in range(N):
        # Provjera da li je pozicija sigurna
        if is_safe(board, row, col, N):
            board[row][col] = 1
            # Rekurzivno pozivanje funkcije za postavljanje sljedeće kraljice
            if solve_n_queens(board, row+1, N):
                return True
            # Vraćanje unazad ako se kraljica ne može postaviti
            board[row][col] = 0
    
    # Vraćanje False ako se ne može postaviti nijedna kraljica
    return False

def create_board(N):
    return [[0 for _ in range(N)] for _ in range(N)]

def display_solution(board):
    window = tk.Tk()
    window.title("Rješenje problema N kraljica")
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            color = "white" if (row+col) % 2 == 0 else "black"
            queen = "♕" if board[row][col] == 1 else ""
            
            label = tk.Label(window, text=queen, font=("Arial", 30), bg=color, fg="red")
            label.grid(row=row, column=col, padx=5, pady=5)
    
    window.mainloop()

def solve_n_queens_main():
    N = int(input("Unesite broj kraljica: "))
    board = create_board(N)
    if solve_n_queens(board, 0, N):
        display_solution(board)
    else:
        print("Nema rješenja")

solve_n_queens_main()
