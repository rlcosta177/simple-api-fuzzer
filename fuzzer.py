import requests
import sys

try:
    for word in sys.stdin:
        word = word.strip() # remove newlines and extra spaces from the wordlist.txt

        try:
            res = requests.get(url=f"https://example.com/{word}")
            print(res) # print response status (e.g. <Response [200]> or <Response [404]>)
            data = res.json() # parse response to json
            print(data)

        # catch all request-related errors
        except requests.exceptions.RequestException:
            print(f"{{'{word}': Not Found'}}")
            continue

        # handle json decoding errors
        except ValueError:
            print(f"failed to decode json for {word}")
            continue

# handle user interruption (e.g. CTRL+C)
except KeyboardInterrupt:
    print("\nProcess interrupted by user.")