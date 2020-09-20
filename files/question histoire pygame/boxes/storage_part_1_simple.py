#ThorPy storage tutorial : basics - step1
import thorpy, random

application = thorpy.Application(size=(400, 400), caption="Storage")

elements = [thorpy.make_button("button" + str(i)) for i in range(12)]
for e in elements:
    w, h = e.get_rect().size
    w, h = w*(1+random.random()/2.), h*(1+random.random()/2.)
    e.set_size((w,h))
background = thorpy.Background(color=(200, 200, 255),elements=elements)

thorpy.store(background, y=0)
background.refresh_lift() #add/remove scroll lift is needed/not needed

menu = thorpy.Menu(background)
menu.play()

application.quit()
