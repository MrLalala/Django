# coding:utf-8
# @Date     :2017
# @Author   :Gan
# @Link     :None
# @Version  :0.0.1
from __future__ import unicode_literals
import random
# from New.wsgi import *
from models import Author, Article, Tag


author_name_list = ['Gan1', 'gan2', 'gAn3', 'gaN4']
article_name_list = ['Django', 'Python', 'HTML']


def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        author.qq = '.'.join(
            str(random.choice(range(10))) for _ in range(9)
        )
        author.addr = 'addr_{addr}'.format(addr=random.randrange(1, 3))
        author.email = '%s@gan.com' % (author.addr)
        author.save()


def create_article_and_tags():
    for article_name in article_name_list:
        tag_name = article_name.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)
        random_author = random.choice(Author.objects.all())

        for i in range(1, 21):
            title = '%s_%s' % (article_name, i)
            article, created = Article.objects.get_or_create(
                title=title, defaults={
                    'author': random_author,
                    'content': '%s正文' % title,
                    'score': random.randrange(70, 101)
                }
            )
            article.save()


def _main():
    create_authors()
    create_article_and_tags()
    print 'done'


if __name__ == '__main__':
    _main()
    print('Done')