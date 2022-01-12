class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")

    # Contact 클래스의 인스턴스를 생성후 반환, 생성된 인스턴스는 반환이 되면서 contact_list에 저장이 된다
    contact = Contact(name, phone_number, e_mail, addr)
    return contact


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


'''
enumerate 함수

반복문을 사용할 때 리스트의 순서값, 즉 인덱스의 정보가 필요한 경우가 존재한다.
enumerate 함수는 리스트의 원소에 순서값을 부여해주는 함수이다. 
입력으로 ㅂ다은 데이터와 인덱스 값을 포함하는 enumerate 객체를 리턴해준다.
enumerate 함수는 for문과 자주 사용이 된다.
'''
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name ==name:
            del contact_list[i]

def store_contact(contact_list):
    f = open("contact_db.txt","wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break

if __name__ == "__main__":
    run()