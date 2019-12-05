import unittest
from distutils.tests import support

from mock import patch


class CFGovDjangoSetup(support.TempdirManager, unittest.TestCase):

    def setUp(self):
        super(CFGovDjangoSetup, self).setUp()

        metadata = {'frontend_build_script': 'myscript.sh'}
        pkg_info, self.dist = self.create_dist(**metadata)

    @patch('cfgov_setup.check_call')
    def test_build_frontend(self, mock_check_call):
        # Run build_frontend
        self.dist.run_command('build_frontend')
        mock_check_call.assert_called_once_with(['sh', 'myscript.sh'])

    @patch('cfgov_setup.check_call')
    def test_wrap_command(self, mock_check_call):
        # Run build_ext
        self.dist.run_command('build_ext')
        mock_check_call.assert_called_once_with(['sh', 'myscript.sh'])
