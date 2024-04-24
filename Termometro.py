from math import pi
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
therm_circle_center = [200, 560]
therm_rect_center = pygame.Rect(160, 250, 80, 300)
therm_arc_r = [130, 500, 150, 125]
therm_arc_l = [120, 500, 150, 125]
thermometer_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.arc(screen, "black", therm_arc_r, 0, pi / 3, 10)
    pygame.draw.arc(screen, "black", therm_arc_l, (2 * pi)/3, pi, 10)
    pygame.draw.circle(screen, "black", therm_circle_center, 80, 10, False, False, True, True)
    pygame.draw.rect(screen, "black", therm_rect_center, width=10, border_radius=50, border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=50)
    pygame.draw.circle(screen, "black", therm_circle_center, 60)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

