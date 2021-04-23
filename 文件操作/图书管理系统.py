'''
文件操作：
    open函数的读写操作

'''


def register():
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    check_password = input('确认密码')
    if password == check_password:
        with open('./user.txt','a') as file:
            file.write('{} {}\n'.format(username, password))
        print('注册成功')
    else:
        print('密码不一致')


def login():
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    # check = username + ' ' + password
    # print(check)
    stream = open('./user.txt', 'r')
    lines = stream.readlines()
    for line in lines:
        uname = line.split()[0]
        pwd = line.split()[1]
        if uname == username and password == pwd:
            print('登录成功')
    else:
        print('登录失败')
        # print(uname, pwd)
    stream.close()

    # for line in lines:
    #     # print(line, end='')
    #     if check == line:
    #         print('登录成功')
    # else:
    #     print('登录失败')

def show_book():
    book_db_path = './book.txt'
    with open(book_db_path, 'r', encoding='utf-8') as f:
        books = f.readlines()
    for book in books:
        print(book,end='')


if __name__ == '__main__':
    # register()
    # login()
    show_book()