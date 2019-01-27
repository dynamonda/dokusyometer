#!/usr/bin/python

import unittest
from dokusyometer import dokusyoapi as dapi

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_datas_from_id(self):
        datas = dapi.user_datas_from_id(199863)
        self.assertEqual(datas['name'], 'dynamonda')

        datas = dapi.user_datas_from_id(452601)
        self.assertEqual(datas['name'], 'さっとる◎')
        
        with self.assertRaises(TypeError):
            dapi.user_datas_from_id("string")

        datas = dapi.user_datas_from_id(9999999999)
        self.assertEqual(datas['name'], 'NotFound')

if __name__ == '__main__':
    unittest.main()