from django.core.management.base import BaseCommand

from news.models import Post
from news.serializers import PostSerializer

class Command(BaseCommand):
    help = 'Reset posts upvotes to 0.'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        update_data: dict = {"upvotes_amount": 0}

        for post in posts:
            serializer = PostSerializer(post, data=update_data, partial=True)
            if serializer.is_valid():
                serializer.save()
        
        self.stdout.write("Upvoted posts")
