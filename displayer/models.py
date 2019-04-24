from django.db import models

# Create your models here.

class Algorithm_template(models.Model):
    
    categorys = (
        ("classifier","分类"),
        ("regression","回归"),
        #("决策树"),
        #("贝叶斯"),
        #("核"),
        ("cluster","聚类"),
        ("others","其他"),
    )

    patterns = (
        ("supervised","监督学习"),
        ("semi_supervised","半监督学习"),
        ("RF","强化学习"),
        ("unsupervised","无监督学习"),
        ("others","其他"),

    )

    name = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    pattern = models.CharField(max_length=32, choices=patterns, default="supervised")
    category = models.CharField(max_length=32, choices=categorys, default="classifier")
    template_file = models.FileField(upload_to="alg_tem_file")


    def __str__(self):
        return self.name # ,self.name_en,self.pattern,self.category

    class Meta:
        # ordering = ["-name"]
        ordering = ["-category"]
        verbose_name = "算法"
        verbose_name_plural = "算法"

    






