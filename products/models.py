from django.db import models


from django.utils.translation import ugettext_lazy as _

# ugettext_lazy 
# برای مدل ها
# ugettext
# برای ویو ها

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_("parent"),blank=True,null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar') , blank=True , upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)

    # جدول ها به این صورت در دیتابیس ایجاد شود
    class Meta:
        db_table = 'catogories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Product(models.Model):
    pass

class File(models.Model):
    pass