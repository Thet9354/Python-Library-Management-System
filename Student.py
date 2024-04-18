class Student:
   def __init__(self, name, library):
       self.name = name
       self.books = []
       self.library = library

   def view_borrowed(self):
       if not self.books:
           print('You haven\'t borrowed any books')
       else:
           for book in self.books:
               print(book)

   def request_book(self):
       book = input(
           'Enter the name of the book you\'d like to borrow >> ')
       if self.library.lend_book(book, self.name):
           self.books.append(book)

   def return_book(self):
       book = input(
           'Enter the name of the book you\'d like to return >> ')
       if book in self.books:
           self.library.return_book(book)
       else:
           print('You haven\'t borrowed that book, try another...')


def create_lib():
   books = {
       'The Last Battle': 'Free',
       'The Hunger Games': 'Free',
       'Cracking the Coding Interview': 'Free'
   }
   library = Library(books)
   student_example = Student('Your Name', library)

   while True:
       print('''
           ==========LIBRARY MENU===========
           1. Display Available Books
           2. Borrow a Book
           3. Return a Book
           4. View Your Books
           5. Exit'''
             )

       choice = int(input('Enter Choice: '))
       if choice == 1:
           print()
           library.show_avail_books()
       elif choice == 2:
           print()
           student_example.request_book()
       elif choice == 3:
           print()
           student_example.return_book()
       elif choice == 4:
           print()
           student_example.view_borrowed()
       elif choice == 5:
           print('Goodbye')
           exit()


if __name__ == '__main__':
   create_lib()