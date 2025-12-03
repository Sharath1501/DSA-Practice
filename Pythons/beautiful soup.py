from bs4 import BeautifulSoup

html_content = """
<ul>
<li>Name
<ul>
<li>grade:E</li>
<li>grade:E</li>
<li>grade:E</li>
</ul>
</li>
</ul>
"""

soup = BeautifulSoup(html_content,'html.parser')
li_tags = soup.find_all('li')
for li in li_tags:
    print(li.get_text(strip=True))
lrntag = len(li_tags)
print(lrntag)
