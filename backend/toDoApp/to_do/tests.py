from django.test import TestCase
from .models import Task

# Create your tests here.


class ApiViewsStatusCodeTest(TestCase):
    def setUp(self):
        self.createdTask = Task.objects.create(title="Created task",
                                               isDone=False)

    def test_if_status_code_of_list_view_is_correct(self):
        response = self.client.get('http://127.0.0.1:8000/api/tasks/')
        return self.assertEquals(response.status_code, 200)

    def test_if_status_code_of_detail_view_is_correct(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/tasks/' + str(self.createdTask.pk) + '/')
        return self.assertEquals(response.status_code, 200)


class TaskModelTest(TestCase):
    def setUp(self):
        self.createdTask = Task.objects.create(title="Created task",
                                               isDone=False)

    def test_if_task_model_contains_title_field(self):
        self.title = self.createdTask.title
        self.assertEquals(self.title, "Created task")

    def test_if_task_model_contains_isDone_field(self):
        self.isDone = self.createdTask.isDone
        self.assertEquals(self.isDone, False)
