#!/Users/deanyoon/opt/anaconda3/bin/python3

import cgi,os

form = cgi.FieldStorage()
page_id = form["page_id"].value

os.remove('data/'+page_id)




# Redirection
print("Location: index.py")   
print()  


