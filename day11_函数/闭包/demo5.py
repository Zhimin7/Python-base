# 计数器

def generate_count():
    container = [0]

    def add_one():
        container[0] = container[0] + 1
        print('第{}次访问'.format(container[0]))

    return add_one


counter = generate_count()
counter()
counter()
counter()
