from django.test import TestCase
from django.urls import reverse

from .models import Employee


class EmployeeDetailViewTests(TestCase):
    def test_employee_details_are_displayed(self):
        employee = Employee.objects.create(
            first_name="Ada",
            last_name="Lovelace",
            email="ada@example.com",
            designation="Analyst",
            salary=1000,
            joining_date="2024-01-01",
            image="",
        )

        response = self.client.get(reverse("employee_detail", args=[employee.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ada Lovelace")
        self.assertContains(response, "ada@example.com")
        self.assertContains(response, "Analyst")
        self.assertNotContains(response, "<img")


class AddEmployeeViewTests(TestCase):
    def test_add_employee_page_is_displayed(self):
        response = self.client.get(reverse("add_employee"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Employee")
