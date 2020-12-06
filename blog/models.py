from django.db import models

CATEGORIES = (
    ('Academics','Academics'),
    ('Business','Business'),
    ('Design','Design'),
    ('Development','Development'),
    ('Health & Fitness','Health & Fitness'),
    ('IT & Software','IT & Software'),
    ('language','language'),
    ('Lifestyle','Lifestyle'),
    ('Marketing','Marketing'),
    ('Music','Music'),
    ('Officer Productivity','Officer Productivity'),
    ('Personal Development','Personal Development'),
    ('Photography','Photography'),
)

class Blog(models.Model):
    course_name = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=True, blank=True)
    categories = models.CharField(max_length=50, choices=CATEGORIES, null=False, blank=False)
    description = models.TextField(max_length=1500, null=True, blank=True)
    link = models.URLField(max_length=400, null=False, blank=False)
    tags = models.CharField(max_length=255, null=False, blank=False)
    picture = models.ImageField(upload_to='blog/', null=False, blank=False)
    views = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def incrementViewCount(self):
        self.views += 1
        self.save()


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    text = models.TextField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name