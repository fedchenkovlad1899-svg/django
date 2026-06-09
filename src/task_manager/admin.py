from django.contrib import admin

from task_manager.models import Tasks,Tags,Projects,ProjectsDetails,Comments,Attachments
from django.contrib import messages

from django.utils.safestring import mark_safe

from task_manager.models.tasks import TaskStatus
from django.utils.html import format_html

# inline
class CommentInline(admin.TabularInline):
    model = Comments
    extra = 1

class TagsInline(admin.StackedInline):
    model = Tags.tasks.through
    extra = 1


class AttachmentsInline(admin.TabularInline):
    model = Attachments
    extra = 1






# @admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    #fields = ("description",("name","status"))
    fieldsets = [
        (
            None,
            {
                "fields": [("name", "status"),"description","priority","created_at","comments_count"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["assignee", "project"],
            },
        ),
    ]


    readonly_fields = ("created_at","comments_count")

    def comments_count(self, obj):
        return f"{obj.comments.count()} шт."

    comments_count.short_description = "Количество комментариев"


    exclude = ("is_reopened",)
    list_display = ("display_name","status","priority","priority_status","project","assignee",
                    "task_name_status","assignee_email")

    @admin.display(description="Задача и статус")
    def task_name_status(self, obj):
        return f"{obj.name} - {obj.status}"

    list_display_links = ("display_name",) # убрал "status" из-за 5 задания
    list_editable = ("status","priority",)
    list_filter = ("status","priority","project",("assignee", admin.RelatedOnlyFieldListFilter))
    search_fields = ("display_name",)
    list_per_page = 245
    ordering = ("-priority","name")
    inlines = (CommentInline,TagsInline,AttachmentsInline,)
    save_on_top = True
    actions = ("make_canceled","decrease_priority","make_completed","make_reopen","make_comment")

    @admin.display(description="Email исполнителя", ordering="assignee__email")
    def assignee_email(self, obj):
        return obj.assignee.email if obj.assignee else "-"

    def priority_status(self,obj):
        if obj.priority < 3:
            return "LOW"
        if obj.priority < 5:
            return "MEDIUM"
        return "HIGH"
    priority_status.string = ""
    priority_status.short_description = "Приоритет статуса"

    @admin.display(description="Наименование")
    def display_name(self, instance):
        return mark_safe(f"<h1>{instance.name}</h1>")

    @admin.action(description="Отметить задачи как отмененные")
    def make_canceled(self, request, queryset):
        queryset.update(status=TaskStatus.CANCELED)


    @admin.action(description="Снизить приоритетность на 1 пункт")
    def decrease_priority(self, request, queryset):
        lst_non_decrease_obj = []
        for obj in queryset:
            if obj.priority > 1:
                obj.priority -= 1
                obj.save()
            else:
                lst_non_decrease_obj.append(obj)
        if lst_non_decrease_obj:
            self.message_user(
                request,
                f"count not decrease priority obj {len(lst_non_decrease_obj)}. {[item.name for item in lst_non_decrease_obj]}",
                messages.ERROR,
            )

    @admin.action(description="Отметить задачи как завершённые")
    def make_completed(self, request, queryset):
        queryset.update(status="TaskStatus.COMPLETED")

    @admin.action(description="Сбросить флаг is_reopened")
    def make_reopen(self, request, queryset):
        queryset.update(is_reopen=False)

    @admin.action(description="Добавить комментарий к задаче “Processed by admin” ")
    def make_comment(self, request, queryset):
        for task in queryset:
            task.comments.get_or_create(message="Processed by admin", user=request.user)



class ProjectDetailInline(admin.StackedInline):
    model = ProjectsDetails
    extra = 0

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    # fields = ('name', 'description',)
    exclude = ('owner', )
    list_display = ('name', 'owner',)
    list_editable = ('owner',)
    inlines = (ProjectDetailInline, )
    actions = ('make_admin',)


class AttachmentsAdmin(admin.ModelAdmin):
    list_display = ("name","task","display_photo","photo","file","preview")
    @admin.display(description="Отображение картинки")
    def display_photo(self, instance):
        if instance.photo:
            return mark_safe(f'<img src={ instance.photo.url } width=50/>')

    @admin.display(description="Превью ")
    def preview(self,obj):
        if obj.file:
            return format_html('<a href="{}">Открыть файл</a>', obj.file.url)
        return "—"


admin.site.register(Tasks,TaskAdmin)
admin.site.register(Tags)
#admin.site.register(Projects)
admin.site.register(ProjectsDetails)
admin.site.register(Comments)
admin.site.register(Attachments,AttachmentsAdmin)

# Register your models here.
