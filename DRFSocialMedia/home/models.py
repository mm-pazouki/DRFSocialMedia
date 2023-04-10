from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user


class Post(models.Model):
    text = models.CharField(max_length=200)
    posted_by = CurrentUserField(related_name='posted_by')
    pub_date = models.DateTimeField('Publication Date', auto_now=True)
    in_reply_to_post = models.IntegerField(null=True)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_readable_date(self):
        return self.pub_date.strftime("%B %d, %Y")

    def get_user(self):
        user_dict = vars(self.posted_by)
        return {"id": user_dict["id"], "username": user_dict["username"]}

    def get_likes(self):
        return Post.objects.filter(id=self, liked_by=get_current_authenticated_user().pk)

    def get_comments(self):
        return Post.objects.filter(in_reply_to_post=self.pk)

    def __str__(self):
        return str(self)
