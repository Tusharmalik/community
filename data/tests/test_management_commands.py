from django.core.management import call_command
from django.test import TestCase

from data.models import Contributor


class ImportContributorDataTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        call_command('import_contributors_data')

    def test_command_import_contributors_data(self):
        contributors = Contributor.objects.all()
        self.assertIn('jayvdb',
                      [contributor.login for contributor in contributors])
