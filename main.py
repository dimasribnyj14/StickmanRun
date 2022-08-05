import save_settings as save
import scenes as scene
if save.saves["levels"] == 0 or save.saves["levels"] == "main_menu" or save.saves["levels"] == "0":
    scene.main_menu()
elif save.saves["levels"] == "first_level" or save.saves["levels"] == 1:
    scene.firstlevel()
else:
    scene.error()
