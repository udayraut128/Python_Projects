import os
import random
import string
import instaloader


def random_folder_name():
    chars = string.ascii_lowercase + string.digits
    random_name = "".join(random.choices(chars, k=8))
    return f"IG_{random_name}"


def download_instagram_post(url):
    # Current folder
    current_folder = os.getcwd()

    # Create random folder
    folder_name = random_folder_name()
    download_folder = os.path.join(current_folder, folder_name)

    os.makedirs(download_folder, exist_ok=True)

    # Instagram loader
    loader = instaloader.Instaloader(
        dirname_pattern=download_folder,
        filename_pattern="{shortcode}_{mediaid}",
        download_comments=False,
        save_metadata=False,
        compress_json=False,
    )

    try:
        # Get shortcode from URL
        shortcode = url.rstrip("/").split("/")[-1]

        print(f"\nDownloading: {url}")
        print(f"Folder: {download_folder}")

        post = instaloader.Post.from_shortcode(
            loader.context,
            shortcode
        )

        # Download post
        loader.download_post(
            post,
            target=""
        )

        print("\nDownload completed!")
        print(f"Saved to: {download_folder}")

    except Exception as e:
        print(f"\nError: {e}")


while True:
    url = input("\nEnter Instagram post URL (or q to quit): ").strip()

    if url.lower() == "q":
        break

    if not url:
        print("Please enter a URL.")
        continue

    download_instagram_post(url)
