from django.test import Client, TestCase
from account.models import User
from task_manager.models.comments import Comments
from task_manager.models.attachments import Attachments
from task_manager.models import Tasks
from task_manager.models.tasks import TaskStatus
from task_manager.forms import TaskForm, CommentForm


class TestTaskForm(TestCase):
    def test_task_form_valid(self):
        test_task_name = "test task"
        test_priority = 2
        test_description = "test description"
        test_status = TaskStatus.CREATED

        body = {
            "name": test_task_name,
            "priority": test_priority,
            "description": test_description,
            "status": test_status
        }
        form = TaskForm(data=body)
        self.assertTrue(form.is_valid())

    def test_task_form_valid_high_priority_empty_description(self):
        test_task_name = "test task"
        test_priority = 4
        test_description = ""
        test_status = TaskStatus.CREATED

        body = {
            "name": test_task_name,
            "priority": test_priority,
            "description": test_description,
            "status": test_status
        }
        form = TaskForm(data=body)

        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)


    def test_task_form_max_priority(self):
        test_task_name = "test task"
        test_priority = 6
        test_description = "test description"
        test_status = TaskStatus.CREATED

        body = {
            "name": test_task_name,
            "priority": test_priority,
            "description": test_description,
            "status": test_status
        }
        form = TaskForm(data=body)

        self.assertFalse(form.is_valid())
        self.assertIn("priority", form.errors)

    def test_task_form_missing_fields(self):
        test_priority = 3
        test_description = "test description"
        test_status = TaskStatus.CREATED

        body = {
            "priority": test_priority,
            "description": test_description,
            "status": test_status
        }
        form = TaskForm(data=body)

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)




class TestCommentForm(TestCase):
    def setUp(self):
        self.client = Client()
        test_user_email = "test@test.com"
        test_password = "1234"
        self.user = User.objects._create_user(
            email=test_user_email,
            password=test_password
        )
        self.client.force_login(self.user)

        test_task_name = "test task"
        test_priority = 1
        test_description = "test description"
        test_default_status = TaskStatus.CREATED

        self.task = Tasks.objects.create(
            name=test_task_name,
            priority=test_priority,
            description=test_description,
            assignee=self.user,
            status=test_default_status,
        )

    def test_comment_form_valid(self):
        test_message = "test message"

        body = {
            "message": test_message,
            "user": self.user.id,
            "task": self.task.id
        }
        form = CommentForm(data=body)
        self.assertTrue(form.is_valid())

    def test_comment_form_empty_message(self):

        body = {
            "message": "",
            "user": self.user.id,
            "task": self.task.id
        }
        form = CommentForm(data=body)
        self.assertFalse(form.is_valid())
        self.assertIn("message", form.errors)




