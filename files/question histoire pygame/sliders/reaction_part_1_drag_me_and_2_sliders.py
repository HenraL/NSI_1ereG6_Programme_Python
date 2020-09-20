#ThorPy real life tutorial : step 1
import thorpy

def run_application():
    W, H = 300, 300
    application = thorpy.Application(size=(W,H), caption="Real life example")

    draggable = thorpy.Draggable("Drag me")
    sx = thorpy.SliderX(length=100, limvals=(0, W), text="X:", type_=int)
    sy = thorpy.SliderX(length=100, limvals=(0, H), text="Y:", type_=int)

    background = thorpy.Background(color=(200,255,255),
    elements=[draggable, sx, sy])
    thorpy.store(background, [sx, sy])

    menu = thorpy.Menu(background) #create a menu for auto events handling
    menu.play()
    application.quit()

run_application()
