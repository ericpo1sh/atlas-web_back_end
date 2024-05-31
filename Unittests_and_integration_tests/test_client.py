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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        ''' Testing that the list of repos is from the chosen payload. '''
        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl-3.0"}}
        ]
        mock_get_json.return_value = mock_repos_payload
        mock_repos_url = "https://api.github.com/orgs/test-org/repos"
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = mock_repos_url
            client = GithubOrgClient("test-org")
            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        ''' testing licenses '''
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
