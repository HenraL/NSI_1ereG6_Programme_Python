#ThorPy reactions tutorial : step 2 - ThorPy events
import thorpy, pygame

def my_func_reaction(event):#Reactions functions must take an event as first arg
    element_name = event.el.get_text()
    element_value = event.el.get_value()
    print("You have just inserted a text into element named:", element_name)
    print("By the way, you inserted the following text: '", element_value, "'")

#We declare a Reaction reaction to THORPY_EVENTs with id EVENT_INSERT
my_reaction = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                              reac_func=my_func_reaction,
                              event_args={"id":thorpy.constants.EVENT_INSERT})

application = thorpy.Application(size=(300, 300), caption="Reaction tuto")

inserter = thorpy.Inserter(name="My Inserter", value="Write here!")
background = thorpy.Background(color=(255,255,255), elements=[inserter])
background.add_reaction(my_reaction) #add my_reaction to background's reactions

thorpy.store(background)

menu = thorpy.Menu(background) #create a menu for auto events handling
menu.play() #launch the menu

application.quit()
