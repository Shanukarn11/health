from django.contrib import admin
from sre_parse import State
from django.contrib import admin
from django.contrib import messages
import csv
from django.http import HttpResponse
from .models import MasterLabels,Addressdata,Navbar,Course,Lang, ProjectCarousel,Services,Events,Team,Blogs,HomeBanner,HomeImages,Statics,Clients,Testimonials,Videos
def export_as_csv(self, request, queryset):
    
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response
admin.site.add_action(export_as_csv)

@admin.register(Lang)
class LangAdmin(admin.ModelAdmin):
    list_display=('id','lang')
    search_fields=('id','lang',)

@admin.register(MasterLabels)
class MasterLabelsAdmin(admin.ModelAdmin):
    list_display=('id','keydata','label','lang','extrainfo')
    search_fields=('id','keydata','label','lang')
    
@admin.register(Addressdata)
class AddressdataAdmin(admin.ModelAdmin):
    list_display=('id','keydata','label','lang','extrainfo')
    search_fields=('id','keydata','label','lang')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')
    
@admin.register(Statics)
class StaticsAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','pic1','pic2','writer_name','shortDescription','heading','description_para1','description_para2','description_quote','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')
@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display=('id','keydata','title','link','shortDescription'
    )
    search_fields=('id','keydata','name')

@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')
@admin.register(ProjectCarousel)
class ProjectCarouselAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')
    
@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','heading','description','lang','attr1','attr2','attr3','attr4',
    )
    search_fields=('id','keydata','name')

@admin.register(HomeImages)
class HomeImagesAdmin(admin.ModelAdmin):
    list_display=('id','keydata','size','pic','name','lang',
    )
    search_fields=('id','keydata','name')



@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display=('id','keydata','name','urlitem','lang',
    )
    search_fields=('id','keydata','name')
    
