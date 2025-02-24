from bookapidao import getAllBooks

books = getAllBooks()

total = 0
count = 0
for book in books:
    #print(book)
    total += book["price"]
    count += 1

print ("Average of ", count, "books is ", total/count )

'''
# or if you want to be fancier
total = sum(book["price"] for book in books)
count = len(books)

print ("Average of ", count, "books is ", total/count )
'''