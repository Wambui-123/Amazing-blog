import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
  def setUp(self):
      self.user_Yvonne = User(username = "Yvonne",
                            password = "123456",
                            email = "yvonne@gmail.com")
      self.new_post = Post(post_title = "Sample Title",
                           post_content = "Hey there, hope you have an amazing day!",
                           user_id = self.user_Yvonne.id)
      self.new_comment = Comment(comment = "Great job",
                                 post_id = self.new_post.id,
                                 user_id = self.user_Yvonne.id)

  def test_instance(self):
      self.assertTrue(isinstance(self.user_Yvonne, User))
      self.assertTrue(isinstance(self.new_post, Post))
      self.assertTrue(isinstance(self.new_comment, Comment))