

class Library:

    def __init__(self):
        self.books = []
        self.sign_up_preocess = None
        self.max_ship_num = None
        self.num_books = None

    def remove_book(self, id):
        del self.books[]

    def load_library(self, scores, info_line, book_line):

        self.num_books = info_line[0]
        self.sign_up_preocess = info_line[1]
        self.max_ship_num = info_line[2]

        for id in book_line:
            self.books.append([id, scores[id]])

