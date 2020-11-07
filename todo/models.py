from django.db import models

# Create your models here.
# モデルは本質的には、データベースのレイアウトと、それに付随するメタデータ
# https://docs.djangoproject.com/ja/2.2/ref/models/fields/#field-types
# https://tutorial.djangogirls.org/ja/deploy/
class Todo(models.Model):
    large_class   = models.CharField('LargeClass',  max_length=100, null=False, blank=False, default='general')
    middle_class  = models.CharField('MiddleClass', max_length=100, null=False, blank=False, default='general')
    small_class   = models.CharField('SmallClass',  max_length=100, null=False, blank=False, default='general')
    todo          = models.CharField('ToDo', max_length=100, null=False, blank=False)
    remarks       = models.TextField('Remarks', max_length=100, null=False, blank=True)
    deadline      = models.DateTimeField('予定完了日時', auto_now_add=False, auto_now=False, editable=True, blank=True)
    created_at    = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at    = models.DateTimeField('更新日時', auto_now=True)
    
    def __str__(self):
        return self.todo
