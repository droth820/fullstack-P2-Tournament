#
# Database access functions for the web forum.
# 

#import time
import psycopg2
import bleach



## Get posts from database.
def GetAllPosts():
  ##Get all the posts from the database, sorted with the newest first.
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("SELECT time, content FROM posts ORDER BY time DESC")
  posts = ({'content': str(row[1]), 'time': str(row[0])}
          for row in c.fetchall())

  DB.close()
  return posts

## Add a post to the database.
def AddPost(content):
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  clean_content = bleach.clean(content)
  c.execute("INSERT INTO posts (content) VALUES (%s)",
    (clean_content,))
  DB.commit()
  DB.close()

#use in python console to remove spam.
'''$ psql forum  
update posts set content = 'safe' where content like '%spam%';

#Delete all from posts
delete from posts where content = 'cheese'; 
'''