from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from .models import Post

# Create your tests here.

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'Basma96',
            email = 'basmanizar@outlook.com',
            password = 'password'
        )

        self.post = Post.objects.create(
            title = 'oranges',
            body = 'Vitmain C',
            author = self.user
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_details_view(self):
        response = self.client.get(reverse('post_detail', args = '1'))
        self.assertEqual(response.status_code, 200)

    def test_post_create_view(self):
        post = self.client.post('blog/new', {'author':"Basma96", 'title': "Files in Python", 'body':"When you access a file on an operating system, a file path is required."})
        response = self.client.get(reverse('post_detail', args = '1'))
        self.assertEqual(response.status_code, 200)

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args = '1'), {
            'title': 'python',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'python')

    def test_post_delete_view(self):
        response = self.client.get(reverse_lazy('post_delete', args='1'))
        self.assertRedirects(response, reverse_lazy('postes'), status_code=200)
