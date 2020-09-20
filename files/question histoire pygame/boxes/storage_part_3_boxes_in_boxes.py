#ThorPy storage tutorial : boxes
import thorpy

application = thorpy.Application(size=(400, 400), caption="Storage")

elements = [thorpy.make_button("button" + str(i)) for i in range(12)]

box1 = thorpy.Box(elements[0:4])
thorpy.store(box1, mode="h")
box1.fit_children()

box2 = thorpy.Box(elements[4:8])

box3 = thorpy.Box(elements[8:12])

box_2_3 = thorpy.make_group([box2,box3], mode="h")

boxes = [box1, box_2_3]
background = thorpy.Background(color=(200, 200, 255), elements=boxes)
thorpy.store(background)

menu = thorpy.Menu(background)
menu.play()

application.quit()
