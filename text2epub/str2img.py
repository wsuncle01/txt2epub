
import pygame
import textwrap
pygame.init()



def str2img(text:str):
    text = text.encode('utf-8').decode('utf-8')

    lines = textwrap.wrap(text,width=11)
    print(lines)

    screen = pygame.display.set_mode((480, 675), 0, 32)
    background = pygame.image.load("./background.jpg").convert()
    #设置字体和字号
    font = pygame.font.SysFont('Microsoft YaHei', 32)
    #渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
    #ftext = font.render(text, True, (0, 0, 0))

    screen.blit(background, (0, 0))
    i=1
    for line in lines:
        ftext = font.render(line, True, (0, 0, 0))
        x = (480 - ftext.get_width())/2
        y = (200 + ftext.get_height()*i*2) / 2
        screen.blit(ftext, (x, y))
        i+=1

        
        
    #screen.blit(ftext, (x, y))

    #保存图片
    pygame.image.save(screen, "cover.jpg")#图片保存地址

if __name__=="__main__":
    text = input('title:')
    str2img(text)
