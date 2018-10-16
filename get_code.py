import bs4 as bs
import urllib.request

name = 'atelier.txt'
with open(name) as fp:
    soup = bs.BeautifulSoup(fp, 'lxml')

title = soup.find('h1').text.split(':')[0].lower().replace(' ', '')

formated_text = ''
prev_header = ''
for pre_tag in soup.find_all('pre'):
    header = None
    pre_parent = pre_tag
    while not header:
        header = pre_parent.find_previous_sibling('h3')
        if not header:
            header = pre_parent.find_previous_sibling('h2')
            if not header:
                header = pre_parent.find_previous_sibling('h1')
        pre_parent = pre_parent.parent
    
    header = header.text
    formated_text += '{}{}\n{}\n'.format('# {}\n\n'.format(header) if header != prev_header else '', pre_tag.text,'-'*15)
    prev_header = header


file = open("formated_text/android-{}.txt".format(title),"w")

file.write(formated_text)

file.close()


