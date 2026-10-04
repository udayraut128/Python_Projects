import instaloader
from urllib.parse import urlparse
from pathlib import Path

# Documents folder
documents_path = Path.home() / "Documents"

# Main Instagram download folder
main_folder = documents_path / "Instagram_Downloads"
main_folder.mkdir(parents=True, exist_ok=True)

# Ask for Instagram URL
url = input("Enter Instagram post URL: ").strip()

# Extract shortcode
parts = urlparse(url).path.strip("/").split("/")

if "p" not in parts:
    print("Please enter a normal Instagram post URL.")
    exit()

index = parts.index("p")
shortcode = parts[index + 1]

# Create separate folder using shortcode
post_folder = main_folder / shortcode
post_folder.mkdir(parents=True, exist_ok=True)

# Instaloader
loader = instaloader.Instaloader(
    dirname_pattern=str(post_folder),
    filename_pattern="{date_utc:%Y-%m-%d}_{shortcode}"
)

try:
    post = instaloader.Post.from_shortcode(
        loader.context,
        shortcode
    )

    loader.download_post(
        post,
        target=""
    )

    print("\nDownload completed!")
    print(f"Saved to: {post_folder}")

except Exception as e:
    print("\nDownload failed!")
    print(e)