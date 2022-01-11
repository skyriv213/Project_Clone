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

def run():

    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)

        elif menu ==2:
            print_contact((contact_list))

        elif menu == 4:
            break

if __name__ == "__main__":
    run()