#!/Users/deanyoon/opt/anaconda3/bin/python3

import cgi,os

form = cgi.FieldStorage()
page_id = form['page_id'].value


title = form["title"].value
description = form["description"].value

opened_file = open('data/'+ page_id, 'w')
opened_file.write(description)
opened_file.close()
os.rename( 'data/'+page_id,'data/'+title)


# Redirection
print("Location: index.py?id="+title)   
print()  


