class Library:

   def __init__(self, books):
       self.books = books

   def show_avail_books(self):
       print('Our Library Can Offer You The Following Books:')
       print('================================================')
       for book, borrower in self.books.items():
           if borrower == 'Free':
               print(book)

   def lend_book(self, requested_book, name):
       if self.books[requested_book] == 'Free':
           print(
               f'{requested_book} has been marked'
               f' as \'Borrowed\' by: {name}')
           self.books[requested_book] = name
           return True
       else:
           print(
               f'Sorry, the {requested_book} is currently'
               f' on loan to: {self.books[requested_book]}')
           return False

   def return_book(self, returned_book):
       self.books[returned_book] = 'Free'
       print(f'Thanks for returning {returned_book}')
