import thorpy, random

application = thorpy.Application(size=(400, 400), caption="Storage")

elements = [thorpy.make_button("button" + str(i)) for i in range(12)]
for e in elements:
    w, h = e.get_rect().size
    w, h = w*(1+random.random()/2.), h*(1+random.random()/2.)
    e.set_size((w,h))
background = thorpy.Background(color=(200, 200, 255),elements=elements)

thorpy.store(background, elements[0:3], x=380, y=10, align="right")
thorpy.store(background, elements[3:6], x=10, y=10, align="left", gap=0)
thorpy.store(background, elements[6:9], mode="h", y=200)
thorpy.store(background, elements[9:12], mode="h", y=300, align="top")

menu = thorpy.Menu(background)
menu.play()

application.quit()
