import pygame
class gameresourse():
    def __init__(self):
        self.path='image/'
        self.startgame_img=None
        self.restartgame_img=None
        self.stopgame_img = None
        self.endgame_img=None
        self.secondgame_img=None
        self.bg_imag=None
        self.music='music/'
        self.music_pause=False

    def start_image(self):
        if not self.startgame_img:
            self.startgame_img=pygame.image.load(self.path+"name.png").convert_alpha()
        return self.startgame_img

    def restart_image(self):
        if not self.restartgame_img:
            self.restartgame_img=pygame.image.load(self.path+"name2.png").convert_alpha()
        return self.restartgame_img

    def stop_image(self):
        if not self.stopgame_img:
            self.stopgame_img=pygame.image.load(self.path+"name3.png").convert_alpha()
        return self.stopgame_img

    def end_image(self):
        if not self.endgame_img:
            self.endgame_img=pygame.image.load(self.path+"name4.png").convert_alpha()
        return self.endgame_img

    def second_image(self):
        if not self.secondgame_img:
            self.secondgame_img = pygame.image.load(self.path + "name5.png").convert_alpha()
        return self.secondgame_img

    def play_music(self):
        pygame.mixer.init()
        bg_music=self.music+'blank space.mp3'
        pygame.mixer.music.load(bg_music)
        pygame.mixer.music.play(-1)

    def pause_music(self):
        if not self.music_pause:
            pygame.mixer.music.pause()
            self.music_pause=True
        else:
            pygame.mixer.music.unpause()
            self.music_pause=False

    def bg_picture(self):
        if not self.bg_imag:
            self.bg_imag=pygame.image.load(self.path+"bg.jpg").convert_alpha()
        return self.bg_imag











