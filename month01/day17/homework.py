from common.iterable_tools import IterableHelper

class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return f"员工编号是{self.eid},部门编号{self.did},姓名{self.name},薪资{self.money}"


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


# 3.
def get_count01():
    count = 0
    for item in list_employees:
        if item.money > 20000:
            count += 1

    return count


def get_count02():
    count = 0
    for item in list_employees:
        if item.did == 9001:
            count += 1

    return count

# for item in get_count02():
#     print(item)

money_count = IterableHelper.get_count(list_employees, lambda item: item.money > 20000)
print(money_count)

emp_count = IterableHelper.get_count(list_employees, lambda item: item.did == 9001)
print(emp_count)


# 4.
def get_min01():
    min_id = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_id.eid > list_employees[i].eid:
            min_id = list_employees[i]
    return min_id


def get_min02():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value.money > list_employees[i].money:
            min_value = list_employees[i]
    return min_value


def handle01(emp):
    return emp.money


def handle02(emp):
    return emp.eid


money = IterableHelper.get_min(list_employees, lambda item: item.money)
print(money.__dict__)

emp = IterableHelper.get_min(list_employees, lambda item: item.eid)
print(emp.__dict__)


# 5.
def order_by01():
    for i in range(len(list_employees) - 1):
        for j in range(i + 1, len(list_employees)):
            if list_employees[i].money > list_employees[j].money:
                list_employees[i], list_employees[j] = list_employees[j], list_employees[i]

    return list_employees


def order_by02(func):
    for i in range(len(list_employees) - 1):
        for j in range(i + 1, len(list_employees)):
            # if list_employees[i].eid > list_employees[j].eid:
            if func(list_employees[i]) > func(list_employees[j]):
                list_employees[i], list_employees[j] = list_employees[j], list_employees[i]

    return list_employees


IterableHelper.order_by(list_employees,lambda item: item.money)
for item in list_employees:
    print(item)

IterableHelper.order_by(list_employees,lambda item: item.eid)
for item in list_employees:
    print(item)