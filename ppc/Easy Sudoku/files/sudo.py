import socket
from sudoku import Sudoku

def solve_sudoku(board):
    try:
        sudoku = Sudoku(3, 3, board=board)
        solution = sudoku.solve()
        return solution.board if solution else None
    except Exception as e:
        print(f"Error solving Sudoku: {e}")
        return None

def handle_server(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f"Connected to {host}:{port}")

            solved_puzzles_count = 0  # Counter to track the number of solved puzzles

            while solved_puzzles_count < 10:  # Stop after 10 correct iterations
                data = s.recv(1024).decode('utf-8')
                print(f"Received message from server:")
                print(data)

                if ">>" in data:
                    puzzle_data = data.split(">>", 1)[1].strip()  
                    puzzle = parse_sudoku(puzzle_data)
                    print("Solving the received puzzle:")
                    print(puzzle)

                    solved_puzzle = solve_sudoku(puzzle)
                    if solved_puzzle:
                        print("Puzzle solved!")
                        print(solved_puzzle)
                        send_to_server(s, solved_puzzle)
                        solved_puzzles_count += 1  # Increment the solved puzzle count
                    else:
                        print("No solution found for this puzzle.")
                else:
                    print("No puzzle data found in the server message.")

                response = s.recv(1024).decode('utf-8')
                print(f"Server response: {response}")

                if ">>" in response:
                    puzzle_resp = response.split(">>", 1)[1].strip()
                    puzzle = parse_sudoku(puzzle_resp)
                    print("Solving the received puzzle:")
                    print(puzzle)

                    solved_puzzle = solve_sudoku(puzzle)
                    if solved_puzzle:
                        print("Puzzle solved!")
                        send_to_server(s, solved_puzzle)
                        solved_puzzles_count += 1  # Increment the solved puzzle count
                    else:
                        print("No solution found for this puzzle.")
                else:
                    print("No puzzle data found in the server message.")

                if 'failure' in response.lower():
                    print("Puzzle solving failed. Exiting.")
                    break

            print("Solved 10 puzzles. Exiting.")
            print(s.recv(1024).decode('utf-8'))

    except Exception as e:
        print(f"Error here: {e}")

def parse_sudoku(data):
    """Converts the received string to a 9x9 integer grid, treating underscores as 0."""
    rows = data.strip().split('\n')
    board = []
    for row in rows:
        try:
            board.append([0 if val == '_' else int(val) for val in row.split()])
        except ValueError:
            print(f"Invalid row data: {row}, skipping this row.")
    return board

def send_to_server(socket, solved_board):
    """Send the solved Sudoku board (only 9x9 numbers) to the server."""
    solved_string = '\n'.join([' '.join(map(str, row)) for row in solved_board])
    socket.sendall(solved_string.encode('utf-8'))
    print("Sent solved Sudoku to server.")

HOST = "wannahack.iitbhucybersec.in"  # Hostname for your server
PORT = 51748

handle_server(HOST, PORT)
