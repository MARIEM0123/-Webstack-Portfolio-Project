from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    """ organizing courses into different categories """
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    """ class course includes fields for the title, description, category, duration, 
        cover image, detailed content, and an introductory file."""
    title = models.CharField(max_length=200, blank=False, null=False, unique=True)
    description = RichTextUploadingField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='media')
    detail = RichTextUploadingField(blank=True, null=True)
    intro = models.FileField(upload_to='media', blank=True)


class Reference(models.Model):
    """ enhance the learning experience by providing students with additional resource """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='media')
    description = models.CharField(max_length=300, blank=True, null=True)


class Module(models.Model):
    """ class module """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)


class Content(models.Model):
    """ content of the course """
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=True)
    file = models.FileField(upload_to='media', blank=False)


ROLE_CHOICES = {
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Staff', 'Staff'),
}


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='media', blank=True, null=True)


class TakenCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextUploadingField(blank=True, null=True)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=True, null=True)
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = RichTextUploadingField()
