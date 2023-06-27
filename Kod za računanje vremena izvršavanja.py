import tkinter as tk
from tkinter import ttk
import time

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

def solve_n_queens_main(N):
    board = create_board(N)
    start_time = time.time()
    solve_n_queens(board, 0, N)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def generate_table_data():
    table_data = []
    for N in range(1, 9):
        execution_time = solve_n_queens_main(N)
        table_data.append((N, execution_time))
    return table_data

def display_table():
    table_data = generate_table_data()

    root = tk.Tk()
    root.title("Brzina izvršavanja algoritma")

    table = ttk.Treeview(root, columns=("N", "Vrijeme izvršavanja"), show="headings")
    table.heading("N", text="N")
    table.heading("Vrijeme izvršavanja", text="Vrijeme izvršavanja")

    for row in table_data:
        table.insert("", "end", values=row)

    table.pack()

    root.mainloop()

display_table()
