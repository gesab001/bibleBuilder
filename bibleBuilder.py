#!/usr/bin/python3
import os
import sqlite3
import time


def addVerse(book, chapter, verse, word):
        conn = sqlite3.connect('/home/giovanni/Dropbox/kjvtxt/kjv.db')
        conn.execute("INSERT INTO BIBLE3 (BOOK, CHAPTER, VERSE, WORD) VALUES(?, ?, ?, ?)", (book, chapter, verse, word));
        conn.commit()
        print (book + " " + str(chapter) + ":" + str(verse) + " verse added successfully");
        conn.close()    

def getABook(name):
    filepath = "./bible/" + name
    aBook = open(filepath, "r")
    lines = aBook.read()
    lines = lines.replace('\n', ' ')
    getVerses(lines)

def getVerses(lines):
   #split the book into verses
   verses = lines.split("{")
   
   #get the book title
   bookTitle = verses[0]
   bookTitle.strip()

   for x in range(1,len(verses),1):
      #get the chapter number
      aVerse = verses[x]
      chapterBeginningIndex = 0
      chapterEndingIndex = aVerse.index(":")
      chapter = aVerse[chapterBeginningIndex:chapterEndingIndex] 
      chapter.strip()
      chapter = int(chapter)

      #get the verse number
      verseBeginningIndex = aVerse.index(":")+1
      verseEndingIndex = aVerse.index("}")
      verse = aVerse[verseBeginningIndex:verseEndingIndex]
      verse.strip()
      verse = int(verse)

      #get the word of God
      wordBeginningIndex = aVerse.index("}")+1
      word = aVerse[wordBeginningIndex::]
      word.strip()
      addVerse(bookTitle, chapter, verse, word)
      #print(bookTitle + " " + str(chapter) + " " + str(verse) + " " + word + " " + "added")



#get a list of files
fileNames = os.listdir("./bible")
fileNames.sort()
for file in fileNames:
    getABook(file)


#read a book
filepath = "./bible/" + fileNames[0]
aBook = open(filepath, "r")
lines = aBook.read()
lines = lines.replace('\n', ' ')

#split the book into verses
verses = lines.split("{")

#get the book title
bookTitle = verses[0]
bookTitle.strip()

for x in range(1,len(verses),1):
   #get the chapter number
   aVerse = verses[x]
   chapterBeginningIndex = 0
   chapterEndingIndex = aVerse.index(":")
   chapter = aVerse[chapterBeginningIndex:chapterEndingIndex] 
   chapter.strip()
   chapter = int(chapter)

   #get the verse number
   verseBeginningIndex = aVerse.index(":")+1
   verseEndingIndex = aVerse.index("}")
   verse = aVerse[verseBeginningIndex:verseEndingIndex]
   verse.strip()
   verse = int(verse)

   #get the word of God
   wordBeginningIndex = aVerse.index("}")+1
   word = aVerse[wordBeginningIndex::]
   word.strip()
   #addVerse(bookTitle, chapter, verse, word)
   #print(bookTitle + " " + str(chapter) + " " + str(verse) + " " + word + " " + "added")



def retrieve():
        print ("thanks = t")
        print ("requests = r ")
        type = ""
        options = ["thanks", "requests"]
        choice = input("option: ")
        if choice == "t":
           type = options[0]
        if choice == "r":
           type = options[1]
        conn = connect()
        cursor = conn.execute("SELECT ID, DATE, WHAT FROM PRAYERS WHERE TYPE=(?)", (type,))
        for row in cursor:
                print ("ID = " , row[0], "DATE = ", row[1], "WHAT = ", row[2], "\n")
        print ("Operation done successfully");
        conn.close()


def delete(number):    
        conn = connect()
        cursor = conn.execute("DELETE FROM PRAYERS WHERE ID=(?)", (number,));
        conn.commit()
        conn.close()
        retrieve()

def createMultiple():
    filepath = input("type filepath: ")
    prayers = [line.strip() for line in open(filepath, 'r')]
    print (len(prayers))
    print ("thanks = t")
    print ("requests = r ")
    type = ""
    choice = input("option: ")
    if choice == "t":
       type = "thanks"
    if choice == "r":
       type = "requests"
    for aprayer in prayers:
        confirm = input("confirm : ")
        conn = connect()
        conn.execute("INSERT INTO PRAYERS (WHAT, TYPE) VALUES(?, ?)", (aprayer, type,));
        conn.commit()
        print ("prayer added successfully");
        conn.close()  


