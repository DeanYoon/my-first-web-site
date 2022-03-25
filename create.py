#!/Users/deanyoon/opt/anaconda3/bin/python3
print("Content-Type: text/html")    # HTML is following
print()     

import cgi, os,view
files = os.listdir('data')



form = cgi.FieldStorage()
if 'id' in  form:
    page_id = form["id"].value
    description = open('data/'+page_id,'r').read()



else:
    page_id='Welcome'
    description = 'Hello WEB'
# print(page_id)  
print('''<!doctype html>

<html>

<head>
  <title>아씨</title>
  <meta charset="utf-8">
</head>

<body>

  <h1><a href="index.py">index</a></h1>
<ol>
    {listStr}
  
</ol>

<a href="create.py">create</a>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>

</body>
</html>
'''.format(title=page_id, desc=description, listStr = view.get_list()))