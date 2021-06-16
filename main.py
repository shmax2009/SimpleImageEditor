import pygame
import pygame_gui
import easygui
import settings

# -------initialize-------

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((settings.Width, settings.Height))

background = pygame.Surface((settings.Width, settings.Height))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((settings.Width, settings.Height), 'theme.json')

open_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                           text='Open File',
                                           manager=manager)

clock = pygame.time.Clock()
is_running = True
image = None
# -------initialize-------
while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == open_button:
                    # Open file:
                    image = pygame.image.load(easygui.fileopenbox())
                    image = pygame.transform.scale(image, (settings.Width, settings.Height))

        manager.process_events(event)

    manager.update(time_delta)
    # -------draw-------

    window_surface.blit(background, (0, 0))
    if image is not None:
        window_surface.blit(image, (0, 0))
    manager.draw_ui(window_surface)
    # -------draw-------

    pygame.display.update()
