import requests
from bs4 import BeautifulSoup


def get_count_available_repositories():
    language_list = ['pascal', 'python', 'ruby', 'c#']
    available_repositories_list = []

    for language_element in language_list:

        url = 'https://github.com/search?type=Repositories&q=language:@'

        url = url.replace("@", language_element)
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')
        headings_element = soup.find_all('h3')

        for id, title_element in enumerate(headings_element, start=1):
            part_element = title_element.find('span', class_='v-align-middle')

            if part_element is not None:
                part_element = part_element.text.strip().split(" ")[1]

                available_repositories_list.append([language_element.capitalize(), part_element])
                break

    return available_repositories_list


print(get_count_available_repositories())
