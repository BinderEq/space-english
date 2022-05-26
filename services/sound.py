class Sound:
    EXPL = 0
    TAKE = 1
    SHOOT = 2
    def __init__(self, pygame):
        pygame.mixer.music.set_volume(0.8)
        self.sounds = []
        self.sounds.append(pygame.mixer.Sound("sound/explosion.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/take.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/shoot.mp3"))
    def play(self, num):
        self.sounds[num].play()
