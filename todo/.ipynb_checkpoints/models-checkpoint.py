from django.db import models

# Create your models here.
# モデルは本質的には、データベースのレイアウトと、それに付随するメタデータ
class Todo(models.Model):
    large_class   = models.CharField('LargeClass', max_length=100, null=False, blank=False)
    middle_class  = models.CharField('MiddleClass', max_length=100, null=False, blank=False)
    small_class   = models.CharField('SmallClass', max_length=100, null=False, blank=False)
    todo          = models.CharField('ToDo', max_length=100, null=False, blank=False)
    remarks       = models.TextField('Remarks', max_length=100, null=False, blank=False)
    deadline      = models.DateTimeField('予定完了日時')
    created_at    = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at    = models.DateTimeField('更新日時', auto_now=True)
    
    def __str__(self):
        return self.todo
