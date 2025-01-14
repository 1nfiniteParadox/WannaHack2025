import socket
from sudoku import Sudoku
from time import sleep

def solve(board):
    try:
        solver = Sudoku(3, 3, board=board)
        result = solver.solve()
        return result.board if result else None
    except Exception as e:
        print(f"Error solving Sudoku: {e}")
        return None

def handle_connection(server_host, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.connect((server_host, server_port))
            print(f"Connected to {server_host}:{server_port}")

            while True:
                message = connection.recv(1024).decode('utf-8')
                score = message.split("Current Score: ")[1].split()[0]

                print(f"Received message from server:")
                print(message)
                print(score)

                if ">>" in message:
                    puzzle_data = message.split(">>", 1)[1].strip()  
                    puzzle = parse_board(puzzle_data)

                    print("Solving the received puzzle:")
                    print(puzzle)

                    solved_puzzle = solve(puzzle)
                    if solved_puzzle:
                        print("Puzzle solved!")
                        print(solved_puzzle)
                        send_solution(connection, solved_puzzle)
                    else:
                        print("No solution found for this puzzle.")
                else:
                    print("No puzzle data found in the server message.")

                iteration = 1
                while iteration <= 999:  
                    response = connection.recv(1024).decode('utf-8')
                    print(f"Server response: {response}")
                    score = response.split("Current Score: ")[1].split()[0]

                    if ">>" in response:
                        puzzle_response = response.split(">>", 1)[1].strip()  
                        puzzle = parse_board(puzzle_response)

                        print("Solving the received puzzle:")
                        print(puzzle)

                        solved_puzzle = solve(puzzle)
                        if solved_puzzle:
                            print("Puzzle solved!")
                            send_solution(connection, solved_puzzle)
                        else:
                            print("No solution found for this puzzle.")
                    else:
                        print("No puzzle data found in the server message.")

                    print(score)
                    if 'failure' in response.lower():  
                        print("Puzzle solving failed. Exiting.")
                        break  

                    iteration += 1

                final_response = connection.recv(1024).decode('utf-8')
                print(f"Server response: {final_response}")

    except Exception as e:
        print(f"Error here: {e}")

def parse_board(data):
    rows = data.strip().split('\n')
    board = []
    for row in rows:
        try:
            board.append([0 if val == '_' else int(val) for val in row.split()])
        except ValueError as ve:
            print(f"Invalid row data: {row}, skipping this row.")
    return board

def send_solution(connection, solved_board):
    solved_string = '\n'.join([' '.join(map(str, row)) for row in solved_board])
    connection.sendall(solved_string.encode('utf-8'))
    print("Sent solved Sudoku to server.")

SERVER_HOST = "wannahack.iitbhucybersec.in"
SERVER_PORT = 61457

handle_connection(SERVER_HOST, SERVER_PORT)
