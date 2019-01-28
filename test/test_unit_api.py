#!/usr/bin/python

import unittest
from dokusyometer import dokusyoapi as dapi

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_datas_from_id_name(self):
        datas = dapi.user_datas_from_id(199863)
        self.assertEqual(datas['name'], 'dynamonda')

        datas = dapi.user_datas_from_id(452601)
        self.assertEqual(datas['name'], 'さっとる◎')

        with self.assertRaises(TypeError):
            dapi.user_datas_from_id("string")

        datas = dapi.user_datas_from_id(9999999999)
        self.assertEqual(datas['name'], 'NotFound')

    def test_read_books_from_user_id(self):
        datas = dapi.read_books_from_user_id(199863)
        self.assertEqual(len(datas), 409)

        datas = dapi.read_books_from_user_id(567419)
        self.assertEqual(len(datas), 159)

        with self.assertRaises(TypeError):
            dapi.read_books_from_user_id("string")

if __name__ == '__main__':
    unittest.main()