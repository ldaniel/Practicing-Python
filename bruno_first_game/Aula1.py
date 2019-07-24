import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Starting Template"

VELOCITY = 15
VELOCITY_BRICK = 18

class MyGame(arcade.Window):
   
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.page = 0
        self.character = arcade.Sprite('DownloadLink.png', scale = 0.25)
        self.character.center_x = 50
        self.character.center_y = SCREEN_HEIGHT / 2

        self.character_2 = arcade.Sprite('link_lttp.png', scale = 0.150)
        self.character_2.center_x = SCREEN_WIDTH - 50
        self.character_2.center_y = SCREEN_HEIGHT / 2
        
        self.brick = arcade.Sprite('Brick.png', scale = 0.125)
        self.brick.center_x = SCREEN_WIDTH / 2
        self.brick.center_y = SCREEN_HEIGHT / 2


    def on_draw(self):
        
        arcade.start_render()
        if self.page == 0:
            arcade.draw_text("Game Menu", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.RED, 64, anchor_x = 'center', anchor_y = 'center')
        elif self.page == 1:
            arcade.draw_text("Game Story", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.DARK_CYAN, 64, anchor_x = 'center', anchor_y = 'center')
        elif self.page == 2:
            self.character.draw()
            self.character_2.draw()
            self.brick.draw()
        
    def update(self, delta_time):
        
        self.character.update()
        self.character_2.update()

        self.brick.update()

        if arcade.check_for_collision(self.character, self.brick):
        
            self.brick.left = self.character.right + 1
            self.brick.change_x *= -1 
            self.brick.change_y = random.randint(-30,30)

        if arcade.check_for_collision(self.character_2, self.brick):
            
            self.brick.right = self.character_2.left - 1
            self.brick.change_x *= -1 
            self.brick.change_y = random.randint(-30,30)

        if self.brick.bottom < 0:
            self.brick.bottom = 1
            self.brick.change_y *= -1

        if self.brick.top > SCREEN_HEIGHT:
            self.brick.top = SCREEN_HEIGHT - 1
            self.brick.change_y *= -1

        if self.brick.right  < 0 or self.brick.left > SCREEN_WIDTH:
            self.brick.center_x = SCREEN_WIDTH / 2
            self.brick.center_y = SCREEN_HEIGHT / 2
            self.brick.change_x = 0
            self.brick.change_y = 0
        
    def on_key_press(self, key, key_modifiers): 
        
        if key == arcade.key.SPACE:
            self.page += 1
            arcade.set_background_color(arcade.color.AERO_BLUE)
            if self.page == 3:
            	self.setup()       

        if key == arcade.key.W:
        	self.character.change_y = VELOCITY

        if key == arcade.key.S:
        	self.character.change_y = -VELOCITY

        if key == arcade.key.D:
            self.character.change_x = VELOCITY

        if key == arcade.key.A:
            self.character.change_x = -VELOCITY

        if key == arcade.key.UP:
            self.character_2.change_y = VELOCITY

        if key == arcade.key.DOWN:
            self.character_2.change_y = -VELOCITY	

        if key == arcade.key.LEFT:
            self.character_2.change_x = -VELOCITY

        if key == arcade.key.RIGHT:
            self.character_2.change_x = VELOCITY

        if key == arcade.key.ENTER and self.page == 2:
            self.brick.change_x = -random.choice([-VELOCITY_BRICK, VELOCITY_BRICK])
            self.brick.change_y = 0

    def on_key_release(self, key, key_modifiers):
        
        if key == arcade.key.W or key == arcade.key.S:
            self.character.change_y = 0

        if key == arcade.key.A or key == arcade.key.D:
            self.character.change_x = 0

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.character_2.change_y = 0

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.character_2.change_x = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
       
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
      
        pass

def main():
    
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

main()