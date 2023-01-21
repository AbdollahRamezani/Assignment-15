import arcade
from snake import Snake
from apple import Apple    
from pear import Pear
from bomb import Bomb

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake V1")
        arcade.set_background_color(arcade.color.KHAKI)
        self.food = Apple(self)
        self.snake = Snake(self)
        self.pear = Pear(self)
        self.bomb = Bomb(self)
        

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.pear.draw()
        self.snake.draw() #این تابع دراو تابع پدر نیست و تابعی است که خودمان در کلاس اسنیک تعریف کردیم
        self.bomb.draw()
        arcade.draw_text(f'Score:{self.snake.score}', 400, 20, arcade.color.DARK_BLUE, 15, 10, "right", "arial")
        if self.snake.score < 0 or self.width < self.snake.center_x < self.width or \
           self.height < self.snake.center_y < self.height:
                arcade.draw_rectangle_filled(0, 0, 1800, 1500, arcade.color.BLACK)
                arcade.draw_text("GAME OVER", 110,250,arcade.color.YELLOW,33, font_name= "Arial")
        arcade.finish_render()   

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)             
            self.food = Apple(self)  #آبجكت سيب كه در متد ايت در کلاس اسنیک حذف شده اينجا دوباره ميسازيم

        if arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat_pear(self.pear)             
            self.pear = Pear(self)     

        if arcade.check_for_collision(self.snake, self.bomb):
            self.snake.eat_bomb(self.bomb)             
            self.bomb = Bomb(self)   

        if arcade.check_for_collision(self.snake, self.snake): # بررسی برخورد مار با بدن خودش
            arcade.draw_rectangle_filled(0, 0, 1800, 1500, arcade.color.BLACK)
            arcade.draw_text("GAME OVER", 110,250,arcade.color.YELLOW,33, font_name= "Arial")              
            

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol== arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol== arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol== arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol== arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0   

             


game = Game()
arcade.run()        