import pygame

def main():

    res = (1200, 900)
    display = pygame.display.set_mode(res, pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

    img = pygame.Surface(res, pygame.SRCALPHA)
    location = [res[0] / 2, res[1] / 2]
    move_left = False
    move_right = False

    v_speed = 2
    h_speed = .2

    while True:


        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:

                if event.button == 4:
                    location[1] -= v_speed
                elif event.button == 5:
                    location[1] += v_speed
                elif event.button == 1:
                    move_left = False
                elif event.button == 3:
                    move_right = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    move_left = True
                if event.button == 3:
                    move_right = True

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                elif event.key == pygame.K_SPACE:

                    img = pygame.Surface(res, pygame.SRCALPHA)
                    #location = [res[0] / 2, res[1] / 2]
                    move_left = False
                    move_right = False

        if move_left:
            location[0] -= h_speed

        if move_right:
            location[0] += h_speed

        if location[0] < 0:
            location[0] = 0
        elif location[0] > res[0]:
            location[0] = res[0]
        if location[1] < 0:
            location[1] = 0
        elif location[1] > res[1]:
            location[1] = res[1]

        l = [int(location[0]), int(location[1])]

        pygame.draw.circle(img, (180, 180, 180), l, 2, 0)

        pygame.Surface.fill(display, (120, 120, 120))
        pygame.Surface.blit(display, img, (0, 0))
        pygame.draw.circle(display, (0, 0, 0), l, 2, 0)
        pygame.display.update()





main()