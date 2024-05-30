#!/usr/bin/env python3
''' Test Client Module '''
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    ''' testing for HithubOrgClient '''
    @parameterized.expand([
        ("google",), ("abc",)
    ])
    def test_org(self, org_names):
        ''' testing for GithubOrgClient.org '''
        with patch('client.get_json') as mock_get:
            newOrg = GithubOrgClient(org_names)
            newOrg.org()
            mock_get.assert_called_once()
