
pg.init()
screen = pg.display.set_mode((640, 280))
pg.display.set_caption("Text adventures with Pygame")
myfont = pg.font.SysFont("Comic Sans MS", 30)
label = myfont.render("Python and Pygame are Fun!", 1, yellow)
screen.blit(label, (100, 100))
pg.display.flip()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            raise SystemExit