import requests

def make_api_request(query):
    listing = []
    url = "https://v2f-api.shop/search/"
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://google-v2f.com",
        "Referer": "https://google-v2f.com/"
    }

    data = {
        "query": query
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        response_data = response.json()

        for result in response_data:
            url = result[0]
            name = result[1][1]
            time = result[1][0]

            listing.append(f"URL: {url}\nName: {name}\nTime: {time}\n{'-' * 30}")

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return 'ERROR'
    
    return '\n'.join(listing)

def main():
    user_query = input("Enter your query: ")

    req = make_api_request(user_query)
    print(req)

    with open('data.txt', 'w+', encoding='utf-8') as f:
        f.write(req)

if __name__ == "__main__":
    main()
