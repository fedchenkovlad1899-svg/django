from django.test import Client, TestCase


from account.models import User
from task_manager.models.comments import Comments
from task_manager.models.attachments import Attachments
from task_manager.models import Tasks
from task_manager.models.tasks import TaskStatus


from rest_framework import status
from rest_framework.test import APITestCase

from unittest.mock import patch
from unittest.mock import MagicMock


class TestTaskView(TestCase):
    def setUp(self):
        self.client = Client()
        test_user_email = "test@test.com"
        test_password = "1234"
        self.user = User.objects._create_user(
            email=test_user_email,
            password=test_password
        )
        self.client.force_login(self.user)

    def test_task_list(self):

        path = "/tasks/"
        test_task_name ="test task"
        test_default_status = TaskStatus.CREATED
        test_priority = 1

        Tasks.objects.create(
            name=test_task_name,
            priority=test_priority,
            assignee=self.user,
            status=test_default_status,
        )

        response = self.client.get(path=path)

        self.assertEqual(response.status_code,200)

        objects = response.context["object_list"]
        self.assertEqual(len(objects),1)

        self.assertEqual(objects[0].name , test_task_name)
        self.assertEqual(objects[0].priority, test_priority)
        self.assertEqual(objects[0].status, test_default_status)
        self.assertEqual(objects[0].assignee, self.user)

    def test_create_task(self):
        path = "/tasks/create"

        test_task_name ="test task"
        test_priority = 2
        test_description = "test description"
        test_status = TaskStatus.CREATED

        body = {
            "name": test_task_name,
            "priority": test_priority,
            "description": test_description,
            "status": test_status
        }

        response = self.client.post(
            path=path,
            data=body
        )
        print(response.status_code, 302)
        self.assertEqual(response.status_code,302)

        tasks = Tasks.objects.all()


        self.assertEqual(len(tasks),1)
        self.assertEqual(tasks[0].name,test_task_name)
        self.assertEqual(tasks[0].priority, test_priority)
        self.assertEqual(tasks[0].description, test_description)
        self.assertEqual(tasks[0].status, test_status)
#
# class TestCommentFormView(TestCase):
#     def setUp(self):
#         self.client = Client()
#         test_user_email = "test@test.com"
#         test_password = "1234"
#         self.user = User.objects._create_user(
#             email=test_user_email,
#             password=test_password
#         )
#         self.client.force_login(self.user)
#         self.tasks = Tasks.objects.create(name="test task")

    def test_create_comment_form(self):
        path = '/tasks/comment/create'

        test_comments = 'Test comments'
        test_user = self.user
        test_task_name ="test task"
        test_priority = 2
        test_description = "test description"
        test_status = TaskStatus.CREATED


        test_task = Tasks.objects.create(
            name=test_task_name,
            priority=test_priority,
            assignee=self.user,
            description=test_description,
            status=test_status,
        )
        body = {
            "message": test_comments,
            "user": test_user.id,
            "task": test_task.id,
        }
        response = self.client.post(
            path=path,
            data=body
        )
        print(response.status_code, 302)
        self.assertEqual(response.status_code, 302)

        comments = Comments.objects.all()
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0].message, test_comments)
        self.assertEqual(comments[0].user, test_user)
        self.assertEqual(comments[0].task.name, test_task_name)



    @patch('task_manager.views.user_test_validate')
    def test_mock_view(self,user_test_validate):

        user_test_validate = MagicMock(return_value=True)
        path = "/tasks/users/1"
        response = self.client.get(path=path)
        print(user_test_validate.return_value)


class TestTaskApiView(APITestCase):
    def setUp(self):
        self.client = Client()
        test_user_email = "test@test.com"
        test_password = "1234"
        self.user = User.objects._create_user(
            email=test_user_email,
            password=test_password
        )
        self.client.force_login(self.user)
        self.test_task_name ="test task"
        self.test_priority = 1

        Tasks.objects.create(
            name=self.test_task_name,
            priority=self.test_priority,
            assignee=self.user
        )

    def test_create_api_task(self):

        path = "/tasks/api/tasks/"

        response = self.client.get(path)

        task = response.json()["results"][0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(task["name"],self.test_task_name)
        self.assertEqual(task["priority"], self.test_priority)
        self.assertEqual(task["assignee"], self.user.id)

        # self.assertEqual(objects[0].name , test_task_name)
        # self.assertEqual(objects[0].priority, test_priority)
        # self.assertEqual(objects[0].status, test_default_status)
        # self.assertEqual(objects[0].assignee, self.user)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')

class TestUserView(TestCase):
    def test_user_list(self):

        path = "/tasks/users"
        test_id_user = 1
        test_name = "test1"
        test_email = "test1@test1.com"
        test_phone = '747457'

        User.objects.create(
            id=test_id_user,
            username=test_name,
            email=test_email,
            phone=test_phone,
        )

        response = self.client.get(path=path)

        self.assertEqual(response.status_code,200)

        objects = response.context["object_list"]
        self.assertEqual(len(objects),1)

        self.assertEqual(objects[0].id , test_id_user)
        self.assertEqual(objects[0].username, test_name)
        self.assertEqual(objects[0].email, test_email)
        self.assertEqual(objects[0].phone, test_phone)