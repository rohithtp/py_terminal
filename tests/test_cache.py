import os
import shutil
import tempfile
import unittest

import ai.cache as cache
import ai.config as config


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self._original_cache_dir = config.CACHE_DIR
        self._original_enable_cache = cache.ENABLE_CACHE
        self._original_ttl = cache.CACHE_TTL_SECONDS
        config.CACHE_DIR = self.tempdir
        cache.ENABLE_CACHE = True
        cache.CACHE_TTL_SECONDS = 3600

    def tearDown(self):
        config.CACHE_DIR = self._original_cache_dir
        cache.ENABLE_CACHE = self._original_enable_cache
        cache.CACHE_TTL_SECONDS = self._original_ttl
        shutil.rmtree(self.tempdir, ignore_errors=True)

    def test_set_and_get_cached_response(self):
        namespace = "preflight"
        command = "rm -rf /tmp/test"
        context = "ctx"
        payload = {"plain_english_summary": "Dangerous removal."}

        cache.set_cached_response(namespace, command, context, payload)
        cached = cache.get_cached_response(namespace, command, context)

        self.assertIsNotNone(cached)
        self.assertEqual(cached["plain_english_summary"], payload["plain_english_summary"])

    def test_expired_cache_returns_none(self):
        namespace = "preflight"
        command = "rm -rf /tmp/test"
        context = "ctx"
        payload = {"plain_english_summary": "Dangerous removal."}

        cache.set_cached_response(namespace, command, context, payload)
        cache.CACHE_TTL_SECONDS = -1

        expired = cache.get_cached_response(namespace, command, context)
        self.assertIsNone(expired)
