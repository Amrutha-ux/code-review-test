from github import get_repository_files, get_file_content
from analyzer import analyze_code


def review_repository(owner, repo):

    files = get_repository_files(owner, repo)

    results = []

    for file in files:

        # Only analyze Python files
        if file.endswith(".py"):

            code = get_file_content(owner, repo, file)

            if code:
                issues = analyze_code(code)

                if issues:
                    results.append({
                        "file": file,
                        "issues": issues
                    })

    return results