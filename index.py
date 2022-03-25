#!/Users/deanyoon/opt/anaconda3/bin/python3
print("Content-Type: text/html")    # HTML is following
print()     

import cgi, os,view,html_sanitizer

sanitizer = html_sanitizer.Sanitizer()

 




form = cgi.FieldStorage()
if 'id' in  form:
    title = page_id = form["id"].value
    description = open('data/'+page_id,'r').read()
    title= sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)


    update_link = '<a href="update.py?id={}">update</a>'.format(page_id)
    delete_action = '''
    <form action="process_delete.py" method="post">
        <input type="hidden" name="page_id" value="{}">
        <input type="submit" value="delete">
    </form>
    '''.format(page_id)

else:
    title=page_id='Welcome'
    description = 'Hello WEB'
    update_link = ''
    delete_action = ''
# print(page_id)  
print('''<!doctype html>

<html>

<head>
  <title>My Frist Web</title>
  <meta charset="utf-8">
</head>

<body>

  <h1><a href="index.py">index</a></h1>
<ol>
    {listStr}
  
</ol>
<a href='create.py'>create</a>
{update_link}
{delete_action}
<h2>{title}</h2>
  <p>{desc}</p>


</body>
</html>
'''.format(title=title, desc=description, listStr = view.get_list(),
update_link=update_link,delete_action=delete_action))