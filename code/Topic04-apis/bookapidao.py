# This is a module that provides a set of functions to interact with
# the demonstration book API hosted at PythonAnyhwere
# Author Andrew Beatty

import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"


def getAllBooks():
    response = requests.get(url)
    return response.json()

#Test it
#if __name__ == "__main__":       
#    print(getAllBooks())


def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

#Test it
#if __name__ == "__main__":       
#    print(getBookById(1027))            #Note this comes back s a dictionary object not as json. Json has double quotes
                                        #{'author': 'test', 'id': 1027, 'price': 123, 'title': 'test title'}


def createBook(book):               # two ways to create book
    
    response = requests.post(url, json=book)
    #headers ={ "Content-type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)
    
    return response.json()


def createBook(book):
    book = {
        'author':"sharon",
        'title':"test title",
        "price": 123
    }
    response = requests.post(url, json=book)
    return response.json()

#Test it
#if __name__ == "__main__":    
#    book={
#        'author':"sharon",
#        'title':"test title",
#        "price": 123    
#    }  
# print (createBook(book))            # result: {'author': 'sharon', 'id': 1604, 'price': 123, 'title': 'test title'}                                


def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()
    pass

#Test it
#if __name__ == "__main__":    
#    bookdiff={
#        "price": 1000000   
#    }   
#print (updateBook(1604, bookdiff))             # result : {'author': 'sharon', 'id': 1604, 'price': 1000000, 'title': 'test title'}                        
    


def deleteBook(id):                             # same as getbook by id
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


#if __name__ == "__main__":    
#    book= {
#        'author':"sharon",
#        'title':"test title",
#        "price": 1000000
#    }          

#    #print(getAllBooks())
#    #print(getBookById(22))
#    print (deleteBook(1604))
#    print (deleteBook(1605))



# TEST FROM LECTURE
if __name__ == "__main__":              
    book= {
        'author':"test",
        'title':"test title",
        "price": 123
    }
    bookdiff= {
        "price": 1234444
    }
    #print(getAllBooks())
    #print(getBookById(22))
    print (deleteBook(1604))        # 1604 1605 are the id of the book created in the createBook function by me
    print (deleteBook(1605))
    #print (createBook(book))
    #print (updateBook(22, bookdiff))
