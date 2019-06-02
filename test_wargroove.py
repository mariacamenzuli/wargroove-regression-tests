import cmp504
import numpy as np
import unittest


class TestWargroove(unittest.TestCase):

    def test_cherrystone_stronghold_exists(self):
        static_templates = {
            'cherrystone_dragon': 'data/cherrystone_dragon.png',
            'cherrystone_stronghold': 'data/cherrystone_stronghold.png'
        }
        displayCtrl = cmp504.display_controller.DisplayController(static_templates)
        mouseCtrl = cmp504.mouse_controller.MouseController()
        screenshot = displayCtrl.read_image('data/test-screenshot.png')
        match = displayCtrl.find_template('cherrystone_stronghold', image=screenshot)

        self.assertEqual(np.shape(match)[1], 1, "Cherrystone stronghold not located")


if __name__ == '__main__':
    unittest.main()
