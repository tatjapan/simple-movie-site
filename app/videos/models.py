from django.db import models


class Video(models.Model):
    """動画"""

    title = models.CharField('動画タイトル', max_length=99)
    description = models.TextField('説明（空欄可）', blank=True)
    thumbnail = models.ImageField(
        'サムネイル（空欄可）', 
        upload_to='thumbnails/', 
        null=True, 
        blank=True
    ) # /media/thumnails/filename
    upload = models.FileField('ファイル', upload_to='uploads/%Y/%m/%d') # /media/uploades/2019/3/30/filename
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at =models.DateTimeField('更新日', auto_now=True) # 更新するたびにその日時が格納される

    def __str__(self):
        return self.title
