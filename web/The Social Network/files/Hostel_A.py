import requests
from bs4 import BeautifulSoup
import json

base_url = 'http://wannahack.iitbhucybersec.in:51001/hostel/A?page='

# Loop through all 50 pages
for page_number in range(1, 51):
    # Construct the URL for each page
    url = f"{base_url}{page_number}"
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text
    
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.select('tbody tr')
    
    # Extract and append student data for the current page
    with open('HostelA.txt', 'a') as file:
        for row in rows:
            name = row.select_one('.user-name').text
            email = row.select_one('.user-email').text
            room = int(row.select_one('td:last-child').text)
            student = {
                "hostel": "Hostel A",
                "name": name,
                "email": email,
                "room": room
            }
            json_output = json.dumps(student)
            file.write(json_output + ',\n')

print("Data has been appended to HostelA.txt")
