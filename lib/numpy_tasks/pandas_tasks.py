import pandas as pd
import numpy as np
import tools

# Задание 1

authors = pd.DataFrame(
    {
        "author_id": [1, 2, 3],
        "author_name": [
            'Тургенев',
            'Чехов',
            'Островский'
        ]
    }
)

book = pd.DataFrame(
    {
        "author_id": [1, 1, 1, 2, 2, 3, 3],
        "book_title": [
            'Отцы и дети',
            'Рудин',
            'Дворянское гнездо',
            'Толстый и тонкий',
            'Дама с собачкой',
            'Гроза',
            'Таланты и поклонники'
        ],
        "price": [450, 300, 350, 500, 450, 370, 290]
    }
)


print('Task 1')
print(authors)
tools.print_separator()
print(book)
tools.print_separator()

# Задание 2

authors_price = pd.merge(
    authors,
    book,
    on="author_id"
)

print('Task 2')
print(authors_price)
tools.print_separator()

# Задание 3

top_5 = authors_price.sort_values('price', ascending=False).head(5)

print('Task 3')
print(top_5)
tools.print_separator()

# Задание 4

authors_stat = authors_price.groupby('author_name').agg(
    min_price=('price', 'min'),
    max_price=('price', 'max'),
    mean_price=('price', 'mean')
)

print('Task 4')
print(authors_stat)
tools.print_separator()

# Задание 5**

print('Task 5')

cover = pd.Series(
    [
        'твердая',
        'мягкая',
        'мягкая',
        'твердая',
        'твердая',
        'мягкая',
        'мягкая'
    ]
)

authors_price['cover'] = cover
print(authors_price)
tools.print_separator()

book_info = pd.pivot_table(
    authors_price,
    values=['price'],
    index=['author_name'],
    columns=['cover'],
    aggfunc=np.sum,
    fill_value=0
)

print(book_info)
tools.print_separator()
