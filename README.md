# quantum-Chess
started as a hack


src/
    ├── __init__.py
    ├── engine.py           # QuantumChessEngine class and UCI interface
    ├── board.py            # Board class and make_move method
    ├── pieces/             # Folder to store all piece classes
    │   ├── __init__.py
    │   ├── piece.py        # Base Piece class
    │   ├── pawn.py         # Pawn class
    |   +----King.py
    |.  +----Queen.py
    |.  +++++Bishop.py
    |.  +++++Rook.py
    │   └── knight.py       # Knight class
    |    \\implementation of pawn to upgrade
    ├── move.py             # Move class and move generation function
    ├── evaluation.py       # Quantum evaluation function
    ├── search.py           # Search function with quandrafying 
    └── utils/              # Utility classes and functions
        ├── __init__.py
        ├── quantum_gates.py # Quantum gates and operations
        └── quantum_utils.py # Other quantum utilities
        
