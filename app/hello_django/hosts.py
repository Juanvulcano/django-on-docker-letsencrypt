from django_hosts import patterns, host

host_patterns = patterns('',
                         host(r'', 'hello_django.urls', name=' '),
                         host(r'darling', 'hello_django.darling_urls', name='darling'),
                         )
