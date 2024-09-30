from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

# Define the characters to be used for generating short URLs
chars = ascii_lowercase + ascii_uppercase + digits

def gen(length: int) -> str:
    """Generate a random string of a given length using defined characters."""
    return ''.join(choice(chars) for _ in range(length))

def home(request):
    short_url = None

    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        
        if long_url:
            # Automatically append 'http://' if the user didn't provide it
            if not long_url.startswith(('http://', 'https://')):
                long_url = 'http://' + long_url

            # Check if the long URL already exists in the database
            existing_url = ShortURL.objects.filter(original_url=long_url).first()
            if existing_url:
                # If it exists, return the existing short URL
                short_url = request.build_absolute_uri('/') + existing_url.short_url
            else:
                while True:
                    short_url_code = gen(6)  # Generate a 6-char short URL
                    # Collision check: ensure no duplicate short URLs are generated
                    if not ShortURL.objects.filter(short_url=short_url_code).exists():
                        break

                # Save the new short URL in the database
                url_entry = ShortURL(original_url=long_url, short_url=short_url_code)
                url_entry.save()

                # Create the full shortened URL
                short_url = request.build_absolute_uri('/') + short_url_code

    return render(request, 'home.html', {'short_url': short_url})

def redirect_url(request, short_url):
    # Look up the original URL using the short URL code
    url_entry = get_object_or_404(ShortURL, short_url=short_url)

    # Redirect to the original URL
    return redirect(url_entry.original_url)
