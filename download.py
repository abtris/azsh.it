import re
import markdownify
from mastodon import Mastodon
import requests

# Mastodon instance and username
INSTANCE_URL = "https://mastodon.social"
USERNAME = "@azureshit"


# Function to fetch user's ID
def get_user_id(instance_url, username):
    search_url = f"{instance_url}/api/v2/search"
    params = {"q": username, "type": "accounts"}
    response = requests.get(search_url, params=params)
    response.raise_for_status()

    data = response.json()
    if data["accounts"]:
        return data["accounts"][0]["id"]
    return None


# Function to fetch posts by user ID
def fetch_posts(instance_url, user_id, limit=100):
    api_url = f"{instance_url}/api/v1/accounts/{user_id}/statuses"
    params = {"limit": limit, "exclude_replies": True, "exclude_reblogs": True}
    all_posts = []

    while api_url:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        posts = response.json()
        all_posts.extend(posts)

        if "next" in response.links:
            api_url = response.links["next"]["url"]
        else:
            break

    return all_posts


# Function to clean and convert posts to markdown
def convert_posts_to_markdown(posts):
    md_content = "# Mastodon Posts\n\n"

    for post in posts:
        content = markdownify.markdownify(post["content"], heading_style="ATX")
        created_at = post["created_at"]
        url = post["url"]
        md_content += f"## {created_at}\n\n{content}\n\n[View post]({url})\n\n---\n\n"

    return md_content


# Main script execution
if __name__ == "__main__":
    user_id = get_user_id(INSTANCE_URL, USERNAME)
    if not user_id:
        print("User not found.")
    else:
        print(f"Fetching posts for user ID: {user_id}")
        posts = fetch_posts(INSTANCE_URL, user_id)
        markdown_output = convert_posts_to_markdown(posts)

        with open("mastodon_posts.md", "w", encoding="utf-8") as file:
            file.write(markdown_output)

        print("Markdown file saved: mastodon_posts.md")
