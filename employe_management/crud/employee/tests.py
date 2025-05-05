from django.test import TestCase, Client
from django.urls import reverse
from .models import employee

class EmployeeTestCase(TestCase):

    def setUp(self):
        # Create test client
        self.client = Client()

        # Sample employee
        self.employee = employee.objects.create(
            employee_id="E001",
            employee_name="John Doe",
            employee_email="john@example.com",
            employee_contact="9876543210"
        )

    def test_employee_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.employee.employee_name)

    def test_create_employee(self):
        data = {
            'employee_id': 'E002',
            'employee_name': 'Jane Smith',
            'employee_email': 'jane@example.com',
            'employee_contact': '1234567890'
        }
        response = self.client.post(reverse('create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertEqual(employee.objects.count(), 2)

    def test_update_employee(self):
        update_url = reverse('update', args=[self.employee.id])
        data = {
            'employee_id': self.employee.employee_id,
            'employee_name': 'Updated Name',
            'employee_email': self.employee.employee_email,
            'employee_contact': self.employee.employee_contact,
        }
        response = self.client.post(update_url, data)
        self.assertEqual(response.status_code, 302)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.employee_name, 'Updated Name')

    def test_delete_employee(self):
        delete_url = reverse('delete', args=[self.employee.id])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(employee.objects.filter(id=self.employee.id).exists())
