#ThorPy reactions tutorial : step 3 - Dynamically modify events
import thorpy, pygame

def my_func_reaction2(): #constant reaction do not take event as first arg
    print("reaction 2 launched")

def my_func_reaction1(el, reac_1):
    new_reaction = thorpy.ConstantReaction(reacts_to=pygame.MOUSEBUTTONDOWN,
                                           reac_func=my_func_reaction2)
    el.remove_reaction(reac_1)
    el.add_reaction(new_reaction)
    thorpy.functions.refresh_current_menu() #tell menu to refresh reactions!
    print("reaction 1 launched - replacing reac 1 by reac 2")

application = thorpy.Application(size=(300, 300), caption="Reaction tuto")

background = thorpy.Background(color=(255,255,255))

reac_1 = thorpy.ConstantReaction(reacts_to=pygame.MOUSEBUTTONDOWN,
                                 reac_func=my_func_reaction1,
                                 params={"el":background,
                                         "reac_1":None})
reac_1.params["reac_1"] = reac_1
background.add_reaction(reac_1)

menu = thorpy.Menu(background)
menu.play()

application.quit()
