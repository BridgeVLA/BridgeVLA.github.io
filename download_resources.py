import os
import requests
from urllib.parse import urlparse


os.makedirs('static/css', exist_ok=True)
os.makedirs('static/js', exist_ok=True)
os.makedirs('static/fonts', exist_ok=True)


resources = [
    {
        'url': 'https://cdnjs.cloudflare.com/ajax/libs/overlayscrollbars/1.13.1/css/OverlayScrollbars.min.css',
        'path': 'static/css/OverlayScrollbars.min.css'
    },
    {
        'url': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
        'path': 'static/css/all.min.css'
    },
    {
        'url': 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
        'path': 'static/js/jquery.min.js'
    },
    {
        'url': 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/gsap.min.js',
        'path': 'static/js/gsap.min.js'
    },
    {
        'url': 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/ScrollTrigger.min.js',
        'path': 'static/js/ScrollTrigger.min.js'
    }
]

def download_file(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded: {path}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")


for resource in resources:
    download_file(resource['url'], resource['path'])

print("\nAll resources downloaded！") 