class Book:
    def __init__(self, title, isbn):
        if not title:
            raise RuntimeError("Title cannot be empty")
        if not self._is_valid_isbn(isbn):
            raise RuntimeError("Invalid ISBN")
        
        self.__title = title
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    def _is_valid_isbn(self, isbn):
        normalized = isbn.replace('-', '').replace(' ', '')
        if len(normalized) != 13 or not normalized.isdigit():
            return False
    
        digits = [int(d) for d in normalized]
        total = 0
        for idx, digit in enumerate(digits):
            if idx % 2 == 0:
                total += digit
            else:
                total += digit * 3
        return total % 10 == 0