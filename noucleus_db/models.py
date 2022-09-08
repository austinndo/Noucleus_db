from django.db import models

# Create your models here.
forward_strand = "+"
reverse_strand = "-"

STRAND_CHOICES = (
    (forward_strand, "forward"),
    (reverse_strand, "reverse")
)

EDIT_CHOICES = (
    ("disruption", "disruption"),
    ("deletion", "deletion"),
    ("insertion", "insertion"),
    ("correction", "correction")
)


class Gene(models.Model):
    name = models.CharField(blank=False, max_length=100)
    species = models.CharField(blank=False, max_length=100)
    function = models.TextField()
    image_ref = models.TextField(null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(unique=True, blank=False, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password_digest = models.CharField(max_length=120)
    affiliation = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.username


class Guide(models.Model):
    gene = models.ForeignKey(
        Gene, on_delete=models.CASCADE, related_name='gene_guides')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_guides')
    sequence = models.TextField(max_length=28, blank=False)
    strand = models.CharField(choices=STRAND_CHOICES,
                              default="+", max_length=10)
    cas = models.CharField(max_length=20)
    edit_type = models.CharField(
        choices=EDIT_CHOICES, default="disruption", max_length=20)
    efficiency = models.FloatField()
    percent_gc = models.IntegerField()

    def __str__(self):
        return self.sequence
