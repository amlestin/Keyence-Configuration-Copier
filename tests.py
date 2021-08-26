import unittest
import setup_microscope

class TestSetupMicroscope(unittest.TestCase):
    def test_supported_platform(self):
        self.assertTrue(setup_microscope.supported_platform("Windows"))
        self.assertFalse(setup_microscope.supported_platform("Darwin"))

if __name__ == '__main__':
    unittest.main()