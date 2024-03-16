import argparse

import requests


def get_followers_and_followings(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        response_data = response.json()
        followers = response_data.get("followers")
        following = response_data.get("following")
        return followers, following
    except Exception as e:
        print("Something went wrong ...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='GithubViewer')
    parser.add_argument('username')
    args = parser.parse_args()

    followers, following = get_followers_and_followings(args.username)
    print(f'''
    {args.username} has {followers} followers and {following} following
    ''')