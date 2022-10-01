import requests

response=requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
all_projects = response.json()

for project in all_projects:
    print(f" Project Name: {project['name']} Project URL: {project['web_url']}")

