from django.contrib import sitemaps
from django.urls import reverse

class StaticViewsSitemap(sitemaps.Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):

        return [
            'egfdatabase:index',
            'egfdatabase:about',
            'egfdatabase:evaluation',
            'egfdatabase:services',
            'egfdatabase:contact',
        ]

    def location(self, item):
        return reverse(item)
