import json

# service account credentials
CREDENTIALS_FILE = "service-account.json"


def main():
    creds = json.load(open(CREDENTIALS_FILE))
    print("loaded", creds["client_email"])


if __name__ == "__main__":
    main()
