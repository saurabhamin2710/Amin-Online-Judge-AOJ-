from statistics import mode
from django.db import models
from django.forms import CharField, PasswordInput


class users(models.Model):                               # Users Model
    username = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=50, min_length=8)
    contry = models.CharField(max_length=50)
    score = models.IntegerField()
    status = models.CharField(max_length=50)


class problems(models.Model):                          # Problems Model
    prob_description = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    score = models.IntegerField()
    difiiculty = models.CharField(max_length=50)
    testcase_ip = models.CharField(max_length=50)
    testcase_op = models.CharField(max_length=50)


class submissions(models.Model):                       # Submissions Model
    usercode = models.CharField(max_length=50)
    useroutput = models.CharField(max_length=50)
    submissiontime = models.IntegerField()
    verdict = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    problem_id = models.ForeignKey(problems,  on_delete=models.CASCADE)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)


class testcases(models.Model):                          # Testcases Model
    problem_id = models.ForeignKey(problems, on_delete=models.CASCADE)
    testcase_ip = models.CharField(max_length=50)
    testcase_op = models.CharField(max_length=50)
