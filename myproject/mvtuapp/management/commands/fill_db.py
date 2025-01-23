from random import choices
from django.core.management.base import BaseCommand
from mvtuapp.models import Author, Post

LOREM = ("Далеко-далеко за словесными горами в стране, "
         "гласных и согласных живут рыбные тексты. Ты деревни lorem, "
         "сбить дал знаках встретил продолжил обеспечивает букв "
         "заманивший коварный приставка путь, правилами взгляд речью "
         "на берегу жизни грамматики даль осталось имени повстречался? "
         "Агентство он раз грамматики за ведущими необходимыми всемогущая "
         "над даже великий переписывается безорфографичный, мир свой "
         "обеспечивает коварный это последний власти все, домах языкового, "
         "вскоре маленькая своих. Он имени безопасную переписали страна "
         "ты толку до грустный от всех океана напоивший злых маленький "
         "составитель путь на берегу, запятой парадигматическая текст "
         "буквенных проектах журчит образ. Текст вскоре гор эта снова "
         "послушавшись силуэт продолжил наш если до путь оксмокс, "
         "всемогущая вдали парадигматическая!")

class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of authors')

    def handle(self, *args, **options):
        count = options.get('count')
        text = LOREM.split()
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@examp.com')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()