from __future__ import unicode_literals
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import AllBooks , recentlyOpened , userFav , userUploads
from django.shortcuts import redirect , render
import random
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
import string
# Create your views here.

# bookName = models.CharField(max_length=250)
# authorName = models.CharField(max_length=250)
# synopsis = models.CharField(max_length=10000)
# genre = models.CharField(max_length=250)
# authorName = models.CharField(max_length=250)
# ratings = models.CharField(max_length=10)
# trendingNow = models.BooleanField(default=False)
# date = models.CharField(max_length=20)
# thumbnailImage = models.FileField()
# bookCoverImage = models.FileField()
# review1 = models.CharField(max_length=400, default="")
# review2 = models.CharField(max_length=400, default="")
# review3 = models.CharField(max_length=400, default="")
# bookPages = models.CharField(max_length=10, default="")
# secondName = models.CharField(max_length=100, default="")
# bookPDF = models.FileField()


def upload(request):
    form = request.POST
    print("here")
    # bookPDF = request.FILES['bookpdf']
    print ("Error")
    print (request.FILES)
    bookpdf = request.FILES['bookpdf']
    thumbnailImage = request.FILES['thumbnail']
    # print (thumbnailImage.name)
    bookCoverImage = request.FILES['thumbnail']
    fs = FileSystemStorage()
    fs.save(thumbnailImage.name, thumbnailImage)
    fs.save(bookpdf.name, bookpdf)
    album = {
        "bookName":form['bookname'],
        "authorName":form['author'],
        "synopsis": form['synopsis'],
        "genre":form['genre'],
        "thumbnailImage": request.FILES['thumbnail'].name,
        "bookCoverImage": request.FILES['thumbnail'].name,
        "bookPDF": request.FILES['bookpdf'].name,
        "ratings": 4.1,
        "trendingNow": True,
        "date":form['date'],
        }
    print (form)
    print (album)
    book = AllBooks()
    book.bookName = album['bookName']
    book.authorName = album['authorName']
    book.synopsis = album['synopsis']
    book.genre = album['genre']
    book.thumbnailImage = album['thumbnailImage']
    book.bookCoverImage = album['bookCoverImage']
    book.bookPDF = album['bookPDF']
    book.ratings = album['ratings']
    book.trendingNow = album['trendingNow']
    book.date = album['date']
    book.save()
    uploads = userUploads()
    uploads.bookName = album['bookName']
    uploads.userName  = request.user
    uploads.save()


    response = redirect('/Books/')
    return response
    # if form.is_valid():
    #     album = form.save(commit=False)
    #     album.user = request.user
    #     album.album_logo = request.FILES['album_logo']
    #     file_type = album.album_logo.url.split('.')[-1]
    #     file_type = file_type.lower()
    #     if file_type not in IMAGE_FILE_TYPES:
    #         context = {
    #             'album': album,
    #             'form': form,
    #             'error_message': 'Image file must be PNG, JPG, or JPEG',
    #         }
    #         return render(request, 'music/create_album.html', context)
    #     album.save()
    #     return render(request, 'music/detail.html', {'album': album})
    # context = {
    #     "form": form,
    # }
    # return render(request, 'music/create_album.html', context)


def Psychology(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    book = AllBooks.objects.filter(genre="Psychology")
    for i in book:
        print (i)
    context = {
    "Books": book,
    "type": "Psychology",
    }
    return render(request,'Books/all.html',context)


def useruploads(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request, 'Books/error.html')
    uploads = []
    recent = userUploads.objects.filter(userName__exact=request.user.username)
    # print (recent)
    for book in recent:
        print("hellllllllll")
        k = AllBooks.objects.get(bookName__startswith=book.bookName)
        uploads.append(k)
    uploads.reverse()



    print("hello wolrds",uploads)
    context = {
        "Books": uploads,
        "type": "User Uploads",
    }
    return render(request, 'Books/all.html', context)

def Spiritual(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    book = AllBooks.objects.filter(genre="Spiritual")
    for i in book:
        print (i)
    context = {
    "Books": book,
    "type": "Spiritual",
    }
    return render(request,'Books/all.html',context)

def Fiction(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    book = AllBooks.objects.filter(genre="Fiction")
    for i in book:
        print(i)
    context = {
    "Books": book,
    "type": "Fiction",
    }
    return render(request,'Books/all.html',context)



def Mystery(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    book = AllBooks.objects.filter(genre="Mystery")
    for i in book:
        print (i)
    context = {
    "Books": book,
    "type": "Mystery",
    }
    return render(request,'Books/all.html',context)
def horror(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    book = AllBooks.objects.filter(genre="Horror")
    for i in book:
        print (i)
    context = {
    "Books": book,
    "type": "Horror",
    }
    return render(request,'Books/all.html',context)

def Romantic(request):
    if request.user.is_authenticated:
        print( 'Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    book = AllBooks.objects.filter(genre="Romantic")
    for i in book:
        print( i)
    context = {
    "Books": book,
    "type": "Romantic",
    }
    return render(request,'Books/all.html',context)

def Thriller(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    book = AllBooks.objects.filter(genre="Thriller")
    for i in book:
        print (i)
    context = {
    "Books": book,
    "type": "Thriller",
    }
    return render(request,'Books/all.html',context)

def search(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    # book = AllBooks.objects.get(bookName=filter_by)
    # if AllBooks.DoesNotExist:
    #     print "no"
    #     return render(request,'Books/open.html')
    # print "yes"
    # return render(request,'Books/open.html')
    print ("yoyoyooyoyooy")
    book = AllBooks.objects.all()
    query = request.GET.get("q")
    print (query)
    if query:
        book = book.filter(
            Q(bookName=query)
            ).distinct()
        if book:
            print (book)
        # print book.bookName
            for i in book:
                print (i.id)
                synopsis = i.bookName
                ratings = i.ratings
                books = book
            length = len(synopsis)

        # print (Book)
            context = {
                "selectedBook": books,
                "lessDesp": "",
                "moreDesp": "",
                "ratings": float(ratings),
                "isLiked": True,
            }
            print ("Almost rendered")
            return render(request,'Books/details.html', context)
        else:
            return redirect('home')
    else:
        return redirect('home')





def editorchoice(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    books = AllBooks.objects.all()
    z = 0
    k = 20
    editor = []
    randlist = []
    for i in books:
        z += 1
    while k>=0:
        rand = random.randint(0,z-1)
        if rand in randlist:
            continue
        else:
            randlist.append(rand)
            k -= 1
            editor.append(books[rand])
    context = {
        "Books": editor,
        "type": "Editor's Choice",
    }
    return render(request, 'Books/all.html', context)


def highrated(request):
    if request.user.is_authenticated:
        print( 'Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    highestRate = AllBooks.objects.order_by("ratings").reverse()
    z=0
    highestRated = []
    for i in highestRate:
        highestRated.append(i)
        z += 1
        if z == 20:
            break
    context = {
        "Books": highestRated,
        "type": "High Rated",
    }
    return render(request, 'Books/all.html',context)

def trending(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    trendingBooks = AllBooks.objects.filter(trendingNow=True)
    context = {
        "Books":trendingBooks,
        "type":"Trending Now"
    }
    return render(request, 'Books/all.html',context)


def addfavourite(request , book_id):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    Liked = True
    selectedBook = AllBooks.objects.get(id=book_id)
    add=userFav()
    check = userFav.objects.filter(userName=request.user.username).filter(bookName__startswith=selectedBook.bookName)
    i = 0
    for c in check:
        i += 1
    if i == 0:
        add.bookName = selectedBook.bookName
        add.userName = request.user.username
        add.save()
        Liked = True
    else:
        check.delete()
        Liked = False
    selectedBook = AllBooks.objects.filter(id=book_id)
    print ("The Execution is here")
    for book in selectedBook:
        synopsis = book.synopsis
        ratings = book.ratings
    length = len(synopsis)
    #lessDesp = synopsis[0:length / 2]
    #moreDesp = synopsis[length / 2:length - 1]
    # print (Book)
    context = {
        "selectedBook": selectedBook,
        "lessDesp": "",
        "moreDesp": "",
        "ratings": float(ratings),
        "isLiked" : True,
        "Liked" : Liked,
    }
    return render(request, 'Books/details.html' , context)


def favourites(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    z=0
    favourites = []
    fav = userFav.objects.filter(userName=request.user.username)
    for i in fav:
        z += 1
        k=AllBooks.objects.get(bookName__startswith=i.bookName)
        favourites.append(k)
    context = {
        "type":"Your Favourites",
        "numberOfColumns": (z/4),
        "totalBooks": z,
        "Books": favourites,
        "tp":range(4),
        "extra": z-z/4,
    }
    return render(request , 'Books/all.html', context)

def readBook(request , book_id):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    print (request.user.username)
    selectedBook = AllBooks.objects.get(id=book_id)
    add = recentlyOpened()
    print (selectedBook)
    check = recentlyOpened.objects.filter(userName=request.user.username).filter(bookName__startswith=selectedBook.bookName)
    i = 0
    # for z in selectedBook:
    #     book = z
    for c in check:
        i += 1
    if i == 0:
        add.bookName = selectedBook.bookName
        add.userName = request.user.username
        add.save()
    context = {
        "book":selectedBook,
    }
    return render(request, 'Books/final.html',context)

def displayBook(request , book_id):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')
    selectedBook = AllBooks.objects.filter(id=book_id)
    selectBook = AllBooks.objects.get(id=book_id)
    liked = userFav.objects.filter(userName=request.user.username).filter(bookName__startswith=selectBook.bookName)
    l = 0
    for a in liked:
        l +=1
    if l == 1:
        Liked = True
    else:
        Liked = False
    print ("The Execution is here")
    for book in selectedBook:
        #synopsis = book.synopsis()
        ratings = book.ratings
    #length = len(synopsis)
    lessDesp = "Hello"
    moreDesp = "OK Cool"
    # print (Book)
    context = {
        "selectedBook": selectedBook,
        "lessDesp":lessDesp,
        "moreDesp":moreDesp,
        "ratings": float(ratings),
        "Liked":Liked
    }
    return render(request, 'Books/details.html', context)


def home(request):
    if request.user.is_authenticated:
        print ('Yes')
        # for user in User.username:
        print (request.user.username)
    else:
        return render(request,'Books/error.html')

    z = 0
    recents = []
    print (recentlyOpened.objects.all())
    recent = recentlyOpened.objects.filter(userName__exact=request.user.username)
    print (recent)
    for book in recent:
        k = AllBooks.objects.get(bookName__startswith=book.bookName)
        recents.append(k)
    recents.reverse()
    toBeDisplayed = []
    editorsPicked =[]
    randList = []
    print ("hello world",recents)

    k = 0
    trendingBooks = AllBooks.objects.filter(trendingNow__exact=True)
    allBooks = AllBooks.objects.all()
    for i in allBooks:
        k += 1
    for i in trendingBooks:
        z += 1
    for i in range(0,3):
        rand = random.randint(0,z-1)
        if rand in randList:
            rand = random.randint(0, z - 1)
        toBeDisplayed.append(trendingBooks[rand])
        randList.append(rand)
    # print (toBeDisplayed)
    highestRated = AllBooks.objects.order_by("ratings").reverse()
    # print (highestRated)
    randList = []
    # print ("Hellllooooooooo")
    for i in range(0,3):
        rand = random.randint(0,k-1)
        if rand in randList:
            rand = random.randint(0, k - 1)
        editorsPicked.append(allBooks[rand])
        randList.append(rand)
    # print (editorsPicked)
    context = {
        "toBeDisplayed": toBeDisplayed,
        "allBooks": allBooks,
        "highestRated": highestRated,
        "editorsPicked": editorsPicked,
        "recents": recents,

    }
    # print (context)
    return render(request, 'Books/home.html', context)

