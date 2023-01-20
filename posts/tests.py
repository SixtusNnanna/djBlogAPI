from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class TestPost(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="sixtus", email="sixtusq@gmaol.com", password="secret"
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="The tale of Ikenga",
            body="ikenga signifys the spirit of masculinity that motivates man exploits",
        )

    def test_models(self):
        self.assertEqual(self.post.author.username, "sixtus")
        self.assertEqual(self.post.title, "The tale of Ikenga")
        self.assertEqual(
            self.post.body,
            "ikenga signifys the spirit of masculinity that motivates man exploits",
        )
        self.assertEqual(str(self.post), "The tale of Ikenga")
