# TODO Найдите количество книг, которое можно разместить на дискете
volume_mb = 1.44
pages_per_book = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4

volume_b = volume_mb*1024*1024
bytes_per_book = pages_per_book*lines_per_page*symbols_per_line*bytes_per_symbol
books = int(volume_b // bytes_per_book)
print("Количество книг, помещающихся на дискету:", books)
