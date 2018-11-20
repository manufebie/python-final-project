from .models import Article

def latest_articles(request):
    ''''
    This context processors allows me to use this function
    throughout the whole project. It will show the latest three
    blog post.
    '''
    articles_latest = Article.objects.all()[:3]

    return {'articles_latest': articles_latest}


def articles_count(request):
    count = Article.objects.count()
    return {'articles_count': count}
    