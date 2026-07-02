from django.test import Client, TestCase



class TestTaskView(TestCase):

    def test_task_list(self):
        client = Client()
        response = client.get("/tasks/")
        self.assertEqual(response.status_code,200)

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('foo'.islower())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()