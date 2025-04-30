# 定义一个类
class Person:
    # 构造函数，初始化对象的属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义一个方法
    def introduce(self, person):
        print(f"大家好，我叫 {person['name']}，今年 {person['age']} 岁。")

    @staticmethod
    def staticIntroduce(person):  # 不需要 self 参数
        print(f"static 大家好，我叫 {person['name']}，今年 {person['age']} 岁。")


# 创建对象
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# 调用对象的方法
person1.introduce({"name": "Alice1", "age": 21})
person2.introduce({"name": "Alice2", "age": 22})

Person.staticIntroduce({"name": "Alice3", "age": 23})
