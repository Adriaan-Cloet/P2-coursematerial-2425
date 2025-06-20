class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, dx, dy):
        """
        Returns a new Position object that has been moved horizontally by dx
        and vertically by dy.
        """
        return Position(self.x + dx, self.y + dy)

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Position):
            raise NotImplemented()
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    

class ChessPiece:
    def __init__(self, position, color):

        if not self.is_valid_position(position):
            raise ValueError("Invalid position.")
        if not self.is_valid_color(color):
            raise ValueError("Invalid color.")

        self.__position = position
        self.__color = color


    @property
    def position(self):
        return self.__position
    
    @property
    def color(self):
        return self.__color
    
    @staticmethod
    def is_valid_color(color):
        return color in ["black", "white"]
    
    @staticmethod
    def is_valid_position(position):
        return 0 <= position.x < 8 and 0 <= position.y < 8

    def move(self, new_position):
        if not self.is_legal_move(new_position):
            raise ValueError("Illegal move.")
        self.__position = new_position

    def is_legal_move(self, new_position):
        raise NotImplementedError("Subclasses must implement this method.")


class Pawn(ChessPiece):
    def is_legal_move(self, new_position):
        if not self.is_valid_position(new_position):
            return False
        direction = 1 if self.color == "white" else -1
        return self.position.move(0, direction) == new_position
    


class King(ChessPiece):
    def is_legal_move(self, new_position):
        if new_position == self.position:
            return False
        if not self.is_valid_position(new_position):
            return False
        if abs(new_position.x - self.position.x) > 1:
            return False
        if abs(new_position.y - self.position.y) > 1:
            return False
        return True