from django.contrib import admin
from .models import Profile, Ticket, Comment

# Register your models here.
class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 0

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    search_fields = ['user__username', 'role']
    inlines = [TicketInline]


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_by', 'status', 'created_on', 'updated_on']
    list_filter = [ 'status', 'created_on', 'updated_on']
    search_fields = ['subject', 'user__username', 'description']
    raw_id_field= ['user', 'profile']
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'user', 'content', 'created_on']
    list_filter = ['created_on'] 
    search_fields = ['ticket_subject', 'user__username', 'content']





