import cmp504
import numpy as np

static_templates = {
    'cherrystone_dragon': 'data/cherrystone_dragon.png',
    'cherrystone_stronghold': 'data/cherrystone_stronghold.png'
}

displayCtrl = cmp504.display_controller.DisplayController(static_templates)
mouseCtrl = cmp504.mouse_controller.MouseController()

screenshot = displayCtrl.read_image('data/test-screenshot.png')
print(screenshot)
match = displayCtrl.find_template('cherrystone_stronghold', image=screenshot)
print(np.shape(match)[1])