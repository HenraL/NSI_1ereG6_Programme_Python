import thorpy

application = thorpy.Application((600, 600), "Style examples")

buttons = [thorpy.make_button("button"+str(i)) for i in range(8)]

buttons[0].set_main_color((0,255,0))
buttons[1].set_main_color((0,255,0,100)) #with alpha value this time
buttons[2].set_font_color((255,255,0))
buttons[3].set_font_color_hover((0, 255, 0))
buttons[4].set_font("century") #may not work on your computer
buttons[5].set_font_size(18);buttons[5].scale_to_title()
buttons[6].set_size((100,100))
buttons[7].set_text("Hello\nI'm a new line");buttons[7].scale_to_title()

#set theme
thorpy.set_theme("human")
buttons += [thorpy.make_button("button"+str(i)) for i in range(8,11)]

#set default painter as ClassicFrame (same as used in theme 'classic')
thorpy.painterstyle.DEF_PAINTER = thorpy.painters.classicframe.ClassicFrame
thorpy.style.MARGINS = (50,2) #set default margins
buttons += [thorpy.make_button("button"+str(i)) for i in range(11,14)]

background = thorpy.Background(image=thorpy.style.EXAMPLE_IMG,
                                    elements=buttons)
thorpy.store(background)

#very personalized style
a_round_button = thorpy.Clickable("Round Button")
painter = thorpy.painters.optionnal.human.Human(size=(100,50),
                                                radius_ext=0.5,
                                                radius_int=0.4,
                                                border_color=(0,0,255))
a_round_button.set_painter(painter)
a_round_button.finish()

a_text_button = thorpy.make_text("Hello", font_size=20, font_color=(0,255,0))
a_text_button.stick_to(background, "right", "right")

menu = thorpy.Menu([background, a_round_button, a_text_button])
menu.play()

application.quit()
