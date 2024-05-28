#!/usr/bin/env python3
''' test_utils Module '''
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    ''' Unittesting for access_nested_map() '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' method to test that the method returns what it is supposed to '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' method test to test the exceptions '''
        self.assertRaises(TypeError)


class TestGetJson(unittest.TestCase):
    ''' Unittesting for get_json() '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, test_payload):
        ''' test that utils.get_json returns the expected result '''
        with patch('requests.get') as mock_get:  # patches requests.get method
            mock_response = mock_get.return_value  # sets patched requests.get.
            mock_response.json.return_value = test_payload  # sets json method
            result = get_json(url)
            assert result == test_payload


if __name__ == '__main__':
    unittest.main()
