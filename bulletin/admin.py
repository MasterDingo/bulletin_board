from django.contrib import admin

from .models import City, Bulletin

# Register your models here.

@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    readonly_fields = ("author",)

    def is_author_or_superuser(self, user, obj):
        if obj is None:
            return False
        return user.is_authenticated and \
                (user.is_superuser or user == obj.author)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return self.is_author_or_superuser(request.user, obj)

    def has_delete_permission(self, request, obj=None):
        return self.is_author_or_superuser(request.user, obj)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    class Meta:
        model = Bulletin


admin.site.register(City)
