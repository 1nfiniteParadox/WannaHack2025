import requests
from bs4 import BeautifulSoup
import json

base_url = 'http://wannahack.iitbhucybersec.in:51001/hostel/B?page='

# Loop through all 50 pages
for page_number in range(1, 51):
    # Construct the URL for each page
    url = f"{base_url}{page_number}"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text
    
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    cards = soup.select('.card')
    
    # Extract and append student data for the current page
    with open('HostelB.txt', 'a') as file:
        for card in cards:
            name = card.select_one('.data1').text
            email = card.select_one('.data2').text
            room = int(card.select_one('.room').text)
            student = {
                "hostel": "Hostel B",
                "name": name,
                "email": email,
                "room": room
            }
            json_output = json.dumps(student)
            file.write(json_output + ',\n')

print("Data has been appended to HostelB.txt")
