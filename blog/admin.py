from django.contrib import admin
from .models import Author, Entry, Blog

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ("name", "email")



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

def display_entry_authors(obj):
    return ",".join([author.name for author in obj.authors.all()])

display_entry_authors.short_description = 'Authors'


def add_one_batch_on_n_comments(modeladmin, request, queryset):
    for entry in queryset:
        entry.n_comments += 1
        entry.save()

add_one_batch_on_n_comments.short_description = "批量将n_comments加一"

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    exclude = ["n_comments", "n_pingbacks", "rating"]
    list_display = ["headline", "body_text", "pub_date", display_entry_authors, "n_comments"]
    search_fields = ("headline", "body_text")
    date_hierarchy = "pub_date"
    actions = [add_one_batch_on_n_comments]

