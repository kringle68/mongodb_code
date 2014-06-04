import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db=connection.photos
images = db.images
albums = db.albums

def find_and_delete():

    try:
        cursor = images.find({}, {'_id':1})
    except:
        print "Unexpected error:", sys.exc_info()[0]

    found = 0
    nfound = 0
    for doc in cursor:
        docid = doc['_id']
        albcursor = albums.find({ 'images' : docid }).count()
        if albcursor == 0:
            images.remove( { '_id' : docid } )
            nfound += 1
            print "NOT FOUND:, ", docid
        else:
            found += 1

    print "No. found = ", found
    print "No. not found = ", nfound

find_and_delete()

