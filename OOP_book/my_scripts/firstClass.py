class Sum():
    def __init__(self,*args):
        self.num = args
    def sum(self):
        sum_ = 0
        for i in self.num:
            if not isinstance(i,int | float):
                raise TypeError(f"{i} ({type(i).__name__}) not operable")
            sum_ += i
        return sum_
if __name__ == "__main__":
    sum_obj = Sum(1,2,3,4,5)
    print(sum_obj.sum())
    sum_obj = Sum(1,2,"3")
    print(sum_obj.sum())
        