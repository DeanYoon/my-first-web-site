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
  <title>아야</title>
  <meta charset="utf-8">
</head>

<body>

  <h1><a href="index.py">index</a></h1>
<ol>
    {listStr}
  
</ol>

<a href="create.py">create</a>
  <form action="process_update.py" method="post">
      <input type='hidden' name='page_id' value='{form_default_title}'>
      <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
      <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
      <p><input type="submit"></p>
  </form>

</body>
</html>
'''.format(title=page_id, desc=description, listStr = view.get_list(),form_default_title=page_id,
form_default_description=description))