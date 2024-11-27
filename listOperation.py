numbers = [5, 9, 7, 6, 8]
fruits = ['pineapple', 'cherry', 'apple', 'avocado']

def add_values(value):
    numbers.append(value) 
    print(f"{value} Added successfully {numbers}")

def remove_values(value):
    numbers.remove(value)
    print(f"{value} removes successfully.")
    print(numbers)

def add_list():
    a = numbers + fruits
    print(f"first list{numbers}, second list{fruits}, list added together{a}")

def extend_list():
    numbers.extend(fruits)
    print(f"Extended list: {numbers}")

def pop_element():
    print(f"original array: ", numbers)
    c = numbers.pop(0)
    print(f"The value {c} is deleted successfully", numbers)

def del_element(del_ele):
    print(f"The original array: {numbers}")
    del numbers[del_ele]
    print(f"{del_ele} deleted", numbers)

def remove_element(remove_ele):
    if remove_ele in fruits:
        fruits.remove(remove_ele)
        print(f"The value {remove_ele} is removed", fruits)
    else:
        print(f"The value {remove_ele} is not found in the list")

def insert_element(value):
    numbers.insert(0, value)
    print(f"{value} inserted successfully", numbers)

def count_element(value):
    x = numbers.count(value)
    print(x)

def copy_list():
    z = numbers.copy()
    print(f"Copy successfully {z}")

def zip_list():
    list_zip = zip(numbers, fruits)
    z = list(list_zip)
    print(f"Zipped successfully: {z}")


if __name__ == '__main__':

    add_values(9)
    remove_values(8)
    add_list()
    extend_list()
    pop_element()
    del_element(1)
    remove_element("apple")
    insert_element("Cleg")
    count_element(9)
    copy_list()
    zip_list()
    