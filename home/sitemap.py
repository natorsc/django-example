# -*- coding: utf-8 -*-
"""."""

from django.contrib import sitemaps
from django.urls import reverse


class HomeSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home:index']

    def location(self, item):
        return reverse(item)


home_sitemap = (__package__.rsplit('.', 1)[-1], HomeSitemap())
