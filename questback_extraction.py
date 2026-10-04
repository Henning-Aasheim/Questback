import requests
from bs4 import BeautifulSoup

login_url = 'https://web2.questback.com/Authenticate.aspx'
main_url = 'https://web2.questback.com/Quests/Quests.aspx?PPK=onkwoi1dvg#/' # Change this

payload = {
    'username': 'post@sprakradet.no',
    'AuthPassword': 'Retskriving1'
}


with requests.Session() as session:
    session.post(login_url, data=payload)
    response = session.get(main_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())

