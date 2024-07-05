from django import forms
from .models import Course, Reference, Module, Content, UserDetail, TakenCourse,
        Instructor, Enrollment, Review, Assignment, Quiz

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'category', 'duration', 'cover', 'intro', 'detail', 'description']

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'

class TakenCourseForm(forms.ModelForm):
    class Meta:
        model = TakenCourse
        fields = '__all__'

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['course', 'user', 'rating', 'comment']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'course', 'questions']
