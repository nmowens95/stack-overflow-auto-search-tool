import requests
import time
import webbrowser

def search_stackoverflow(error_type, error_message, max_tabs=1):
    # Stack exchange API base url
    api_url = "https://api.stackexchange.com/"


    try:
        # Make an API request using the relevant parameters
        response = requests.get(f"{api_url}"+f"/2.3/search?order=desc&tagged=python&sort=activity&site=stackoverflow&q={error_message}".format(error_type))
        response.raise_for_status() # returns HTTPError object if an error occurs during the process

        # Parses data
        data = response.json()

        # Get th list of relevant threads
        relevant_threads = data["items"]

        # Determine how many tabs to open
        num_tabs_to_open = min(max_tabs, len(relevant_threads))

        # Open relevan threads
        for i in range(num_tabs_to_open):
            thread = relevant_threads[i]
            thread_link = thread["link"]

        # Open the thread in a we browser tab
        webbrowser.open_new_tab(thread_link)
        print("Opened:", thread_link)

        # Used for a delay to stay within rate
        time.sleep(2)  

    # General exception handling         
    except requests.exceptions.RequestException as err: 
        print("Error:", err)


if __name__ == "__main__":
    pass