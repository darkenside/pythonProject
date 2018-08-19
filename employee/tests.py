import unittest
from .models import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.teste1 = Employee.objects.create(name="teste_1", email="teste_1@teste.com", department='TI')
        self.teste2 = Employee.objects.create(name="teste_2", email="teste_2@teste.com", department='Arquitetura')

    def testDadosBase(self):
        self.assertEquals(self.teste1.name, 'teste_1')
        self.assertEquals(self.teste2.department, 'Arquitetura')






