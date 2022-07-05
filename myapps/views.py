from django.shortcuts import render ,HttpResponse , redirect
from django.views.decorators.csrf import csrf_exempt

nextid = 4
topics = [
    {'id':1 , 'title':'Routing' , 'body':'Routing is....'},
    {'id':2 , 'title':'View' , 'body':'View is....'},
    {'id':3 , 'title':'Model' , 'body':'Model is....'}
]

def HTMLTemplate(articleTag ,id=None):
    global topics
    contextUI = ''
    if id!= None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
        '''

    ul = ''
    for topic in topics:
        ul += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
        <html>
            <body>
                <h1><a href="/">django</a></h1>
                <ul>
                    {ul}
                </ul>
                {articleTag}
                <ul>
                    <li><a href="/create/">create</a></li>
                    {contextUI}
                </ul>
            </body>
        </html>
    '''

def index(request):
    article = '''
        <h2>Welcome</h2>
        Hello djnago
    '''
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    if request.method == "GET":
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></P>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></P>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == "POST":
        global nextid
        global topics

        title = request.POST['title']
        body = request.POST['body']
        newTopic = {'id':nextid , 'title':title , 'body':body}
        topics.append(newTopic)
        url = '/read/'+ str(nextid)
        nextid = nextid + 1

        return redirect(url)
    

def read(request,id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def delete(request):
    global topics
    if request.method == "POST":
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        
    return redirect('/') 