import requests
import os


JENKINS_URL = "http://localhost:8080/job/jenkins-demo"
JAR_RELATIVE_PATH = "src/Main.jar"  # adjust to your actual JAR location
LOCAL_SAVE_PATH = "./downloaded.jar"  # where to save locally

# Your Jenkins username and API token (or password)
USERNAME ="shrutij22"
API_TOKEN = ""

def is_build_successful():
    api_url = f"{JENKINS_URL}/lastSuccessfulBuild/api/json"
    resp = requests.get(api_url, auth=(USERNAME, API_TOKEN))
    if resp.status_code != 200:
        print(f"Failed to get build info, status code {resp.status_code}")
        return False
    return True

def download_jar():
    jar_url = f"{JENKINS_URL}/lastSuccessfulBuild/artifact/{JAR_RELATIVE_PATH}"
    resp = requests.get(jar_url, auth=(USERNAME, API_TOKEN))
    if resp.status_code == 200:
        with open(LOCAL_SAVE_PATH, 'wb') as f:
            f.write(resp.content)
        print(f"JAR downloaded successfully to {LOCAL_SAVE_PATH}")
    else:
        print(f"Failed to download JAR, status code {resp.status_code}")

def main():
    if is_build_successful():
        print("Build successful! Downloading JAR...")
        download_jar()
    else:
        print("Build not successful yet. No download.")

if __name__ == "__main__":
    main()
