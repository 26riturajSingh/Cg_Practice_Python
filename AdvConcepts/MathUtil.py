class MathUtil:

    @staticmethod
    def add(a,b):
        return a+b

    @classmethod
    def description(cls):
        print("This is the description")

print(MathUtil.add(1,2))
MathUtil.description()