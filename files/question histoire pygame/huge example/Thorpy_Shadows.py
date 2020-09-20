import pygame, thorpy

ap = thorpy.Application((500,400), "Shadows example")

e_img = thorpy.Draggable() # do not use 'make' !
painter = thorpy.painters.imageframe.ImageFrame("character.png",
                                                colorkey=(255,255,255))
e_img.set_painter(painter)
e_img.finish() #don't forget to finish

if thorpy.constants.CAN_SHADOWS:
    thorpy.makeup.add_static_shadow(e_img, {"target_altitude":0,
                                            "shadow_radius":3})

e_background = thorpy.Background(image=thorpy.style.EXAMPLE_IMG,
                                        elements=[e_img])

menu = thorpy.Menu(e_background)
menu.play()

ap.quit()

#examples of shadow arguments:
##thorpy.makeup.add_static_shadow(e_img,
##    {"target_altitude":10, # altitude (in pixels) of the target
##     "shadow_radius":3, # the smaller, the sharper is the shadow
##     "sun_angle":60, # angle in degrees of the sun
##     "shadow_color":(255,200,0), # color of the shadow
##     "alpha_factor":0.5, # alpha factor
##     "decay_mode":"linear"}) # linear or exponential
