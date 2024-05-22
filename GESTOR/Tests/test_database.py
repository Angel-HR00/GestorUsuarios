import copy
import unittest
import database as db
import helpers

class TestDataBase(unittest.TestCase):
    
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('26A', 'Marta', 'Perez'),
            db.Cliente('65X', 'Ana', 'Martinez'),
            db.Cliente('70M', 'Pedro', 'Picapiedra')
        ]


    def test_buscar(self):
        cliente_existente = db.Clientes.buscar('26A')
        cliente_inexistente = db.Clientes.buscar('20P')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)
    
    
    def test_crear(self):
        nuevo_cliente = db.Clientes.crear('31X', 'Angel', 'Herrero')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '31X')
        self.assertEqual(nuevo_cliente.nombre, 'Angel')
        self.assertEqual(nuevo_cliente.apellido, 'Herrero')
    
    
    def test_modificar(self):
        mod_cliente = copy.copy (db.Clientes.buscar('65X'))
        cliente_moded = db.Clientes.modificar('65X', 'Ana', 'Martinez')
        self.assertEqual(mod_cliente.nombre, 'Ana')
        self.assertEqual(cliente_moded.nombre, 'Belen')
    
    
    def test_borrar(self):
        cliente_borrado = db.Clientes.borrar('70M')
        cliente_buscar = db.Clientes.buscar('70M')
        self.assertEqual(cliente_borrado, cliente_buscar)  
    
    def test_dni(self):
        self.assertTrue(helpers.validate_dni('00A', db.Clientes.lista))
        self.assertFalse(helpers.validate_dni('AA0', db.Clientes.lista))
        self.assertFalse(helpers.validate_dni('65X', db.Clientes.lista))
        self.assertFalse(helpers.validate_dni('00', db.Clientes.lista))
        self.assertFalse(helpers.validate_dni('0A', db.Clientes.lista))
        self.assertFalse(helpers.validate_dni('0', db.Clientes.lista))
        self.assertFalse(helpers.validate_dni('A', db.Clientes.lista))

if __name__ == '__main__':
    unittest.main()