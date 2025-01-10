def make_path(http, link, *paths):
    # Join the paths together and ensure proper URL format
    path = "/".join(path.strip("/") for path in paths)
    return f"{http}://{link}/{path}"

print(make_path("https", "drive.facebook.com", "profile", "u", "0", "Rohan"))