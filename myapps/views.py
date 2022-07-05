from django.shortcuts import render ,HttpResponse

topics = [
    {'id':1 , 'title':'Routing' , 'body':'Routing is....'},
    {'id':2 , 'title':'View' , 'body':'View is....'},
    {'id':3 , 'title':'Model' , 'body':'Model is....'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
        <html>
            <body>
                <h1><a href="/">django</a></h1>
                <ol>
                    {ol}
                </ol>
                {articleTag}
            </body>
        </html>
    '''

def index(request):
    article = '''
        <h2>Welcome</h2>
        Hello djnago
    '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse("Create!")

def read(request,id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))