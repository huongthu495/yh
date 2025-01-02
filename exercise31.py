from urllib.parse import urlparse, parse_qs
import os


def parse_url(url):
    result = {}

    # Parse the URL
    parsed = urlparse(url)

    # Extract protocol
    result['protocol'] = parsed.scheme

    # Extract hostname
    result['hostname'] = parsed.hostname

    # Extract domain name
    if parsed.hostname:
        domain_parts = parsed.hostname.split('.')
        if len(domain_parts) > 2:
            result['domain_name'] = '.'.join(domain_parts[-2:])
        else:
            result['domain_name'] = parsed.hostname

    # Extract directory and filename
    path = parsed.path
    result['directory'], result['filename'] = os.path.split(path)

    # Extract query parameters
    result['query_parameters'] = parse_qs(parsed.query)

    return result


if __name__ == "__main__":
    # Prompt the user to input a URL
    url = input("Nhập URL: ").strip()
    components = parse_url(url)
    print("\nCác thành phần của URL:")
    for key, value in components.items():
        print(f"{key}: {value}")
