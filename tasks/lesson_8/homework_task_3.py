import re


class PhoneBook:
    def __init__(self):
        self.emergency_records = [Record('Fire_Station', '101'), Record('Police', '102'),
                                  Record('Ambulance', '103'), Record('Gas_Station', '104')]
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def delete_record(self, name):
        for record in self.records:
            if record.name == name:
                if record.phone in ['101', '102', '103']:
                    print("Cannot delete emergency service records.")
                else:
                    self.records.remove(record)
                    print(f"Record deleted: {name}")
                return
        print(f"Record with the name {name} not found.")

    def edit_record(self, name, new_phone):
        for record in self.records:
            if record.name == name:
                record.edit(new_phone)
                return
        print(f"Record with the name {name} not found.")

    def show_all(self):
        for record in self.records + self.emergency_records:
            print(record)

    @staticmethod
    def is_valid_phone(phone):
        pattern = r'^\d{3}-\d{3}-\d{2}-\d{2}$'
        return bool(re.match(pattern, phone))


class Interface:
    def __init__(self):
        self.phonebook = PhoneBook()

    def run(self):
        while True:
            print("\n--- Phone Book Interface ---")
            print("1. Add record")
            print("2. Delete record")
            print("3. Edit record")
            print("4. Show all")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone (format: XXX-XXX-XX_-XX): ")
                if name and phone and self.phonebook.is_valid_phone(phone):
                    record = Record(name, phone)
                    self.phonebook.add_record(record)
                else:
                    print("Invalid input. Name and valid phone number (format: XXX-XXX-XXXX) are required.")

            elif choice == "2":
                name = input("Enter name: ")
                self.phonebook.delete_record(name)

            elif choice == "3":
                name = input("Enter name: ")
                new_phone = input("Enter new phone (format: XXX-XXX-XXXX): ")
                if name and new_phone and self.phonebook.is_valid_phone(new_phone):
                    self.phonebook.edit_record(name, new_phone)
                else:
                    print("Invalid input. Name and valid new phone number (format: XXX-XXX-XXXX) are required.")

            elif choice == "4":
                self.phonebook.show_all()

            elif choice == "0":
                print("Exiting the interface...")
                break

            else:
                print("Invalid choice. Please try again.")


class Record:
    def __init__(self, name, phone, surname='', birth_date=''):
        self.__name = name
        self.__phone = phone
        self.__surname = surname
        self.__birth_date = birth_date

    def edit(self, new_phone):
        self.__phone = new_phone

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def surname(self):
        return self.__surname

    @property
    def birth_date(self):
        return self.__birth_date

    def __str__(self):
        return f"Name: {self.__name}, Phone: {self.__phone}"


def __main__():
    interface = Interface()
    interface.run()


if __name__ == "__main__":
    __main__()