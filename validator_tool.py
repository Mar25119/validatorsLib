import validators

def classify_input(text: str) -> str:
    """Êëàññèôèöèğóåò ñòğîêó êàê email, url, ip èëè unknown."""
    if validators.email(text):
        return "email"
    elif validators.url(text):
        return "url"
    elif validators.ip_address.ipv4(text) or validators.ip_address.ipv6(text):
        return "ip"
    else:
        return "unknown"

if name == "main":
    test_inputs = [
        "user@example.com",
        "https://example.com",
        "192.168.1.1",
        "2001:db8::1",
        "not-an-email",
        "ftp://invalid-url", # validators.url òğåáóåò http/https
        "hello world"
    ]

    print("Ğåçóëüòàòû êëàññèôèêàöèè:")
    for item in test_inputs:
        result = classify_input(item)
        print(f"'{item}' ? {result}")
