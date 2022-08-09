

from django.db import models
# from .storage import OverwriteStorage
from PIL import Image
from .storage import OverwriteStorage


# Create your models here.
class Lang(models.Model):
    id=models.CharField(max_length=100,primary_key=True, db_index=True)
    lang=models.CharField(max_length=100,)
class MasterLabels(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata = models.CharField(max_length=200, null=True, db_index=True ,blank=True)
    label=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language", on_delete=models.SET_NULL, db_index=True)

    extrainfo = models.CharField(max_length=200, null=True)

class Statics(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )

class Course(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )

class Services(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )

class Events(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )

class Team(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )

class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    pic1 = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    pic2 = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    writer_name=models.CharField(max_length=200, null=True,blank=True,)
    
    heading=models.CharField(max_length=200, null=True,blank=True,)
    shortDescription=models.TextField(null=True,blank=True)


    description_para1=models.TextField(null=True,blank=True)
    description_para2=models.TextField(null=True,blank=True)
    description_quote=models.TextField(null=True,blank=True)
    tag1=models.TextField(null=True,blank=True,max_length=100)
    tag2=models.TextField(null=True,blank=True,max_length=100)
    tag3=models.TextField(null=True,blank=True,max_length=100)
    bullet_point_1=models.TextField(null=True,blank=True)
    bullet_point_2=models.TextField(null=True,blank=True)
    bullet_point_3=models.TextField(null=True,blank=True)
    bullet_point_4=models.TextField(null=True,blank=True)
    






    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )
class Videos(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    title=models.CharField(max_length=200, null=True,blank=True,)
    
    link=models.CharField( max_length=20000,null=True,blank=True,)
    shortDescription=models.TextField(null=True,blank=True)


    
    
class HomeBanner(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )

class ProjectCarousel(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )
class Clients(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )

class Testimonials(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    heading=models.CharField(max_length=200, null=True,blank=True,)

    description=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )
class HomeImages(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    name=models.CharField(max_length=200, null=True,blank=True, )

    size=models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(
        storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)

    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language27", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )
    

class Addressdata(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata = models.CharField(max_length=200, null=True, db_index=True ,blank=True)
    label=models.TextField(null=True,blank=True)
    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language", on_delete=models.SET_NULL, db_index=True)

    extrainfo = models.CharField(max_length=200, null=True)


class Navbar(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)

    name=models.CharField(max_length=200, null=True,blank=True,)
    urlitem=models.CharField(max_length=200, null=True,blank=True,)

    lang=models.ForeignKey(
        Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    attr1=models.CharField(max_length=200, null=True,blank=True,)
    attr2=models.CharField(max_length=200, null=True,blank=True, )
    attr3=models.CharField(max_length=200, null=True,blank=True, )
    attr4=models.CharField(max_length=200, null=True,blank=True, )