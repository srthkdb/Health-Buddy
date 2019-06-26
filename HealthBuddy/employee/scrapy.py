from bs4 import BeautifulSoup
import re
import requests
import psycopg2

conn = psycopg2.connect(host="localhost",database="myproject", user="myuser", password="mypassword")
c = conn.cursor()

s = requests.Session()
s.get("https://oa.cc.iitk.ac.in/Oa/Jsp/Main_Frameset.jsp")
s.get("https://oa.cc.iitk.ac.in/Oa/Jsp/Main_Intro.jsp?frm='SRCH'")
s.get("https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITK_Srch.jsp?typ=stff")

headers = {
    "Referer": "https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITK_Srch.jsp?typ=stff"
}

headers1 = {
    "Referer": "https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchStffRoll_emp.jsp"
}

payload = {
    'k4': 'oa',
    'numtxt': '',
    'recpos': 0,
    'str': '',
    'selstudrol': '',
    'selstuddep': '',
    'selstudnam': '',
    'stud': 'pfno',
    'txpfno': '',
    'Dept_Stff': '',
    'sort': ['', ''],
    'selstffnam': '',
    'selstffmail': ''
}

payload1 = {
    'recpos': 0,
    'txpfno': '',
    'typ': ['stff'] * 12,
    'numtxt': '',
    'sbm': ['Y'] * 12
}

TOTAL = 8517

def process_response_soup(soup, c):
    for link in soup.select('.TableText a'):
        roll = link.get_text().strip()
        payload1['numtxt'] = roll
        r1 = s.post("https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchRes_new.jsp", headers=headers1, data=payload1)
        soup1 = BeautifulSoup(r1.text, 'html.parser')

        name = ''
        desig = ''
        dept = ''
        office = ''
        tel = ''
        email = ''
        blood_group = ''
        resid = ''

        for para in soup1.select('.TableContent p'):
            body = para.get_text().strip()
            field = body.split(':')
            key = field[0].strip()
            value = field[1].strip()
            if key == 'Name':
                name = value.lower().title()
            elif key == 'Designation':
                desig = value
            elif key == 'Department':
                dept = value.lower().title()
            elif key == 'Office Location':
                office = value
            elif key == 'E-Mail':
                email = value
            elif key == 'Blood Group':
                blood_group = value
            elif key == 'Residence':
                resid = value
            elif key == 'Tel':
                resid = tel
            
        body = soup1.prettify()
        sql = 'INSERT INTO employee_employee(roll, name, desig, dept, office, tel, email, blood_group, resid) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);'

        c.execute(sql, (roll, name, desig, dept, office, tel, email, blood_group, resid))


r = s.post("https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchStffRoll_emp.jsp", headers=headers, data=payload)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.select('.DivContent'):
    substituted = re.sub(r'\s+', ' ', link.text)
    pattern = re.compile(r'\s*You are viewing 1 to 12 records out of (\d+) records\s*')
    match = pattern.match(substituted)
    TOTAL = int(match.group(1))
    print("Total: {}".format(TOTAL))
process_response_soup(soup, c)
print("Processed 12")
for i in range(12, TOTAL+1, 12):
    payload['recpos'] = i
    r = s.post("https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchStffRoll_emp.jsp", headers=headers, data=payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    process_response_soup(soup, c)
    print("Processed {}".format(i + 12))
    conn.commit()
conn.close()
