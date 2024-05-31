#!/usr/bin/env python3
''' Test Client Module '''
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


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

    def test_public_repos_url(self):
        ''' testing public_repos_url '''
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }
        with patch.object(
            GithubOrgClient, 'org', new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = mock_payload
            client = GithubOrgClient("test-org")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/test-org/repos"
            )
