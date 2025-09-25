import pygame as p

p.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 500,500

screen = p.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
p.display.set_caption("Adding Image and Background Image")

bg_image = p.transform.scale(p.image.load(r"C:\Users\jiten\OneDrive\Desktop\Python Codingal\download (1).png").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))

pg_image = p.transform.scale(p.image.load(r"C:\Users\jiten\OneDrive\Desktop\Python Codingal\PeNgUiN.png").convert_alpha(),(200,200))

pg_rect = pg_image.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2 - 30))

text = p.font.Font(None,36).render("Hello World", True,p.Color("black"))

text_rect = text.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2 + 110))

def game_loop():
    clock = p.time.Clock()
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT():
                running = False
        screen.blit(bg_image,(0,0))
        screen.blit(pg_image,pg_rect)
        screen.blit(text,text_rect)

        p.display.flip()
        clock.tick(30)
    
    p.quit()

if __name__  == "__main__":
    game_loop()