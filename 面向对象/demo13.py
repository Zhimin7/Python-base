class Computer(object):
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在用电脑上网....')

    def __str__(self):
        return self.brand + '-------' + self.type + '------' + self.color


class Book(object):
    def __init__(self, book_name, author, number):
        self.book_name = book_name
        self.author = author
        self.number = number

    def __str__(self):
        return self.book_name + '----' + self.author + '----' + str(self.number)


class Student(object):
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.book_name == book.book_name:
                print('已经借过此书了。。')
                break
        else:
            # 将此书添加进books
            self.books.append(book)
            print('添加成功')

    def show_book(self):
        for book in self.books:
            print(book.book_name)



computer = Computer('苹果', 'max pro', 'gard')
book = Book('python 爬虫', '小鬼', 10)
student = Student('小东', computer, book)
print(student)
book1 = Book('python3 爬虫', '小鬼2', 20)
student.borrow_book(book1)
print('---------------')
# student.borrow_book(book=book1)
student.show_book()
