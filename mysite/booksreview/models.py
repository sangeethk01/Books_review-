from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    auther = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField()  # Rating from 1-5
    
    def __str__(self):
        return f"{self.reviewer_name}'s review of {self.book}"