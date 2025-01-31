from django.core.management.base import BaseCommand
from modelsapp.models import Author, Post


class Command(BaseCommand):
    help = "Get Post by author ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    # def handle(self, *args, **options):
    #     pk = options.get('pk')
    #     author = Author.objects.filter(pk=pk).first()
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)
    #         intro = f'All posts of {author.name}\n'
    #         text = '\n'.join(post.content for post in posts)
    #         self.stdout.write(f'{intro}{text}')


    # def handle(self, *args, **options):
    #     pk = options.get('pk')
    #     posts = Post.objects.filter(author__pk=pk)
    #     intro = f'All posts\n'
    #     text = '\n'.join(post.content for post in posts)
    #     self.stdout.write(f'{intro}{text}')

    def handle(self, *args, **options):
        pk = options.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'First three words from text\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')