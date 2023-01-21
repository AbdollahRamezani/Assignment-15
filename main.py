import arcade
class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width // 2
        self.center_y = game.width // 2
        self.color = arcade.color.GREEN      
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.status = False
        self.body = []   #لیستی از دیکشنری ها که شامل ایکس و وای هست  

    def draw(self):  #دز اينجا از متد دراو پدر استفاده نكرديم وبا اورلودينگ يك تابع از خودمان تعريف كرديم
    
      for index,item in enumerate(self.body):
              if index % 2 == 0:
                 color=arcade.color.BLUE   
              else:
                  color=arcade.color.RED              
      arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
      for part in self.body:
            arcade.draw_rectangle_filled(part["x"], part["y"], self.width, self.height, color)
            

    def move(self):   
        self.center_x += self.change_x * self.speed  #اگر جهت حركت مثبت باشد مكان نيز مثبت ميشود و اگر جهت حركت منفي باشد مكان نيز منفي ميشود
        self.center_y += self.change_y * self.speed 
        self.body.append({"x": self.center_x, "y": self.center_y})
        if len(self.body) > self.score:
           self.body.pop(0)

    def eat(self ,food):
        del food    #براي اينكه هر دفعه يك سيب جديد ساخته بشه اول آبجكت سيب حذف ميكنيم
        self.score += 1
        self.status = True

    def eat_pear(self, pear):
        del pear
        self.score += 2   
        self.status = True

    def eat_bomb(self, bomb):
        del bomb
        self.score -=1 
        self.status = True
       
        
        
