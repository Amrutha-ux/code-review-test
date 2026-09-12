import requests


def get_repository_files(owner, repo):
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(repo_url)

    if response.status_code != 200:
        print("Could not find repository")
        return []

    repo_data = response.json()

    branch = repo_data["default_branch"]

    tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"

    response = requests.get(tree_url)

    if response.status_code != 200:
        print("Could not get repository files")
        return []

    data = response.json()

    files = []

    for item in data.get("tree", []):
        if item["type"] == "blob":
            files.append(item["path"])

    return files


def get_file_content(owner, repo, path):
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(repo_url)

    if response.status_code != 200:
        return None

    repo_data = response.json()

    branch = repo_data["default_branch"]

    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.text

    return None