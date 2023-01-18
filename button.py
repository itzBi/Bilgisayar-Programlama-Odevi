import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) #resmi ölçeklendirmek için
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False

		#get mouse position
		mouse_position = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(mouse_position):  #mouse tıklandığında
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:     #pressed[0]= fare sol tık
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action