class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def intro(self):
        print(f'제목은 {self.title}이고 저자는 {self.author}입니다.')

harry = Book('해리포터', '롤링')
print(harry.author)

harry.intro()
