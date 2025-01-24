class Car:
    def __init__(self,price,brand,color):
        '''初始化属性'''
        self.price = price
        self.brand = brand
        self.color = color
        self.mileage = 0
    def show_info(self):
        '''格式化显示车辆信息'''
        car_info = f'价格：{self.price}，品牌：{self.brand},颜色：{self.color}'
        return car_info
    def read_mileage(self):
        '''读取行驶里程 '''
        mileage=f'行驶里程为：{self.mileage}'
        return mileage
    def set_mileage(self,mileage):
        '''设置行驶里程 '''
        self.mileage = mileage
    def update_mileage(self,add_mileage):
        '''更新行驶里程 '''
        self.mileage += add_mileage
        print(f"增加了{add_mileage}公里,当前行驶里程为{self.mileage}")
    #显示油箱容量
    def show_tank(self,tank_capacity):
        print(f'油箱容量为{tank_capacity}')
#将实例用作属性 简洁优雅
class Battery:
    def __init__(self,battery_capacity):
        '''初始化电池容量 '''
        self.battery_capacity = battery_capacity
    def show_battery(self):
        '''显示当前电池容量 '''
        return self.battery_capacity
class ElectricCar(Car):
    def __init__ (self,battery_capacity,price,brand,color):
        ''' 初始化电动汽车的属性继承自Car类的属性和电池容量属性 '''
        super().__init__(price,brand,color)
        self.battery = Battery(battery_capacity)
    #根据当前电量，显示续航里程
    def show_range(self):
        if self.battery.show_battery() > 90:
            print('续航里程为100+公里')
        elif self.battery.show_battery() > 70:
            print('续航里程为80+公里')
        else:
            print('续航里程为50+公里')