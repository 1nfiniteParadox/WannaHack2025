import requests
from bs4 import BeautifulSoup

# Base URL with a placeholder for the page number
base_url = 'http://wannahack.iitbhucybersec.in:51001/hostel/D?page={}'

# Loop through the pages from 1 to 50
for page_num in range(1, 51):  # Pages 1 to 50
    # Generate the URL for the current page
    url = base_url.format(page_num)
    
    # Send a GET request to fetch the HTML content of the page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.text
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table with class "user-table"
        table = soup.find('table', class_='user-table')

        # Check if the table exists
        if table:
            # Open the file in append mode to add data from each page
            with open('HostelD.txt', 'a') as file:
                # Iterate over each row in the table (skip the header row)
                for row in table.find_all('tr')[1:]:  # Skip header row
                    columns = row.find_all('td')
                    
                    if len(columns) > 0:  # Ensure there's data in the row
                        student = {
                            "hostel": "Hostel D",  # You can modify this if needed
                            "name": columns[1].text.strip(),
                            "email": columns[2].text.strip(),
                            "room": int(columns[3].text.strip())
                        }
                        # Write each student's data in the required format
                        file.write(f"{{\n")
                        file.write(f'    "hostel": "{student["hostel"]}",\n')
                        file.write(f'    "name": "{student["name"]}",\n')
                        file.write(f'    "email": "{student["email"]}",\n')
                        file.write(f'    "room": {student["room"]}\n')
                        file.write(f"}},\n")  # Add a comma after each entry

        else:
            print(f"No table found on page {page_num}.")
    else:
        print(f"Failed to retrieve page {page_num}. Status code: {response.status_code}")

print("Data has been successfully saved to 'HostelD.txt'.")
