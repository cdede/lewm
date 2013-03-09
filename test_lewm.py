#!/usr/bin/python
import os
from kppy import KPDB
try:
    from lib_lewm.main import main1
except ImportError:
    os.sys.path.append(os.curdir)
    from lib_lewm.main import CmdKeepass
    from lib_lewm.common import   opendb

import unittest
class AppTest(unittest.TestCase):

      def setUp(self):
          #db,sleep1=opendb('config','a')
          db,sleep1=opendb('config1','a')
          self.cmd = CmdKeepass(db)

      def tearDown(self):
          pass

      def test_ls(self):
          self.cmd.do_ls('')
          self.assertTrue(self.cmd._loc_ls==['Internet_a_c', 'Internet_e'])
          self.cmd.do_ls('-l')
          self.assertTrue (self.cmd._loc_ls==['Internet_a_c c', 'Internet_e e'])


      def test_cat(self):
          self.cmd.do_cat('Internet_a_c')

      def test_export(self):
          if self.cmd.isdb:
              self.cmd.do_export('vqydwa')

if __name__ == '__main__':
    unittest.main()
