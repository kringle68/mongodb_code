
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db=connection.students
grades = db.grades


def find_and_delete():

    print "find, reporting for duty"

    query = {'type':'homework'}

    try:
        cursor = grades.find(query)
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    student_id = -1
    for doc in cursor:
        if student_id != doc['student_id']:
            student_id = doc['student_id']
            grades.remove(doc)


find_and_delete()

