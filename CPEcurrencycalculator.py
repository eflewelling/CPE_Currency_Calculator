import requests
from packaging import version

def get_latest_versions(cpe):
    url = f"https://services.nvd.nist.gov/rest/json/cpes/1.0?cpeMatchString={cpe}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'result' in data and 'cpes' in data['result']:
            return [cpe_item['cpe23Uri'] for cpe_item in data['result']['cpes']]
    return []

def compare_versions(cpe, latest_versions):
    cpe_version = cpe.split(':')[5]
    for version_uri in latest_versions:
        latest_version = version_uri.split(':')[5]
        if version.parse(cpe_version) < version.parse(latest_version):
            return f"{cpe} is outdated. Latest version is {latest_version}."
    return f"{cpe} is up to date."

def main():
    cpe = input("Enter the CPE to check: ")
    latest_versions = get_latest_versions(cpe)
    if latest_versions:
        result = compare_versions(cpe, latest_versions)
        print(result)
    else:
        print("No latest versions found for the given CPE.")

if __name__ == "__main__":
    main()