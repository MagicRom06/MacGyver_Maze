from character.character import Character
from constant.constant import Constant
from level.level import Level


class ConsoleMode(Constant):
    """
    Main class for console mode game
    """
    def __init__(self):
        Constant.__init__(self)
        self.level = Level(Constant.constant['level'])
        self.player = Character(Constant.constant['player'], self.level)

    def play(self):
        """
        method used to launch console game
        """
        progress = True
        self.level.generate()
        x_hero, y_hero = self.level.position(
            self.level.structure, Constant.constant['player'])
        while progress:
            print('Item : {}'.format(self.player.get_item_count()))
            for elt in self.level.structure:
                print("".join(elt))
            direction = input('Choose a direction: ')
            if direction == 'd':
                self.check_victory(x_hero, y_hero + 1)
                if self.player.move(x_hero, y_hero, 'right'):
                    y_hero += 1
            elif direction == 'q':
                self.check_victory(x_hero, y_hero - 1)
                if self.player.move(x_hero, y_hero, 'left'):
                    y_hero -= 1
            elif direction == 's':
                self.check_victory(x_hero + 1, y_hero)
                if self.player.move(x_hero, y_hero, 'down'):
                    x_hero += 1
            elif direction == 'z':
                self.check_victory(x_hero - 1, y_hero)
                if self.player.move(x_hero, y_hero, 'up'):
                    x_hero -= 1

    def check_victory(self, x_hero, y_hero):
        """
        this method will check, at every moves,
        if the player is in front of the boss and
        if he has all requirement to win or not
        """
        if self.level.is_final_boss(x_hero, y_hero):
            if self.player.has_all_items():
                print('You win... but what did you expect? '
                      'you\'re Macgyver !')
                exit()
            else:
                print('You\'re dead !!')
                exit()
