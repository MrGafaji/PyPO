import sys
import random

sys.path.append('../../')

import unittest
import numpy as np

from src.PyPO.System import System
import src.PyPO.MatTransform as mt
##
# @file
# 
# Script for testing the transformational formalism of PyPO.

class Test_MatTransform(unittest.TestCase):
    def setUp(self):
        self.s = System()
        
        parabola_ref = {
                "name"      : "parabola_ref",
                "gmode"     : "uv",
                "pmode"     : "focus",
                "focus_1"   : np.array([0,0,1]),
                "vertex"    : np.zeros(3),
                "lims_u"    : np.array([0, 1]),
                "lims_v"    : np.array([0, 360]),
                "gridsize"  : np.array([101, 101])
                }

        self.s.addParabola(parabola_ref)
   
        parabola_test = self.s.copyObj(parabola_ref)
        parabola_test["name"] = "parabola_test"

        self.s.addParabola(parabola_test)

    def test_translations(self):
        translation0 = np.random.rand(3)
        translation1 = np.random.rand(3)

        # translate test parabola by given amount
        self.s.translateGrids("parabola_test", translation0)
    
        for x0, x0test in zip(translation0, self.s.system["parabola_test"]["pos"]):
            self.assertAlmostEqual(x0, x0test)
        
        # translate test parabola again
        self.s.translateGrids("parabola_test", translation1)
    
        for x1, x1test in zip(translation1 + translation0, self.s.system["parabola_test"]["pos"]):
            self.assertAlmostEqual(x1, x1test)

        # Test absolute translations
        translation0abs = np.random.rand(3)
        translation1abs = np.random.rand(3)

        self.s.translateGrids("parabola_test", translation0abs, mode="absolute")
        self.s.translateGrids("parabola_ref", translation0abs, mode="absolute")

        # Test if pos is translated properly
        for x0a, x0atest in zip(translation0abs, self.s.system["parabola_test"]["pos"]):
            self.assertAlmostEqual(x0a, x0atest)

        # Unpack grids and check if equal
        g0atest = self.s.generateGrids("parabola_test")
        g0aref = self.s.generateGrids("parabola_ref")

        for x0atest, x0aref in zip(g0atest.x.ravel(), g0aref.x.ravel()):
            self.assertAlmostEqual(x0atest, x0aref)
        
        for y0atest, y0aref in zip(g0atest.y.ravel(), g0aref.y.ravel()):
            self.assertAlmostEqual(y0atest, y0aref)
        
        for z0atest, z0aref in zip(g0atest.z.ravel(), g0aref.z.ravel()):
            self.assertAlmostEqual(z0atest, z0aref)

        self.s.homeReflector("parabola_ref")
        
        self.s.translateGrids("parabola_test", translation1abs, mode="absolute")
        self.s.translateGrids("parabola_ref", translation1abs, mode="absolute")
        
        for x1a, x1atest in zip(translation1abs, self.s.system["parabola_test"]["pos"]):
            self.assertAlmostEqual(x1a, x1atest)

        # Unpack grids and check if equal
        g1atest = self.s.generateGrids("parabola_test")
        g1aref = self.s.generateGrids("parabola_ref")

        for x1atest, x1aref in zip(g1atest.x.ravel(), g1aref.x.ravel()):
            self.assertAlmostEqual(x1atest, x1aref)
        
        for y1atest, y1aref in zip(g1atest.y.ravel(), g1aref.y.ravel()):
            self.assertAlmostEqual(y1atest, y1aref)
        
        for z1atest, z1aref in zip(g1atest.z.ravel(), g1aref.z.ravel()):
            self.assertAlmostEqual(z1atest, z1aref)
        
        for a0atest, a0aref in zip(g0atest.area.ravel(), g0aref.area.ravel()):
            self.assertAlmostEqual(a0atest, a0aref)
        
        self.s.homeReflector("parabola_test")

    def test_rotations(self):
        rotation0 = np.degrees((np.random.rand(3) - 0.5)*np.pi)
        rotation1 = np.degrees((np.random.rand(3) - 0.5)*np.pi)

        pivot0 = np.random.rand(3)
        pivot1 = np.random.rand(3)


        # rotate test parabola by given amount
        self.s.rotateGrids("parabola_test", rotation0, pivot=pivot0)
        self.s.rotateGrids("parabola_test", rotation1, pivot=pivot1)
    
        rotation0abs = np.degrees(np.random.rand(3))
        pivot0abs = np.random.rand(3)
        
        print(rotation0 + rotation1, rotation0abs)
        self.s.rotateGrids("parabola_test", rotation0abs, pivot=pivot0abs, mode="absolute")
        self.s.rotateGrids("parabola_ref", rotation0abs, pivot=pivot0abs, mode="absolute")

        #for x0ref, x0test in zip(self.s.system["parabola_ref"]["pos"], self.s.system["parabola_test"]["pos"]):
        #    self.assertAlmostEqual(x0ref, x0test)
        
        print(np.cross(self.s.system["parabola_ref"]["ori"], self.s.system["parabola_test"]["ori"]))
        print(np.dot(self.s.system["parabola_ref"]["ori"], self.s.system["parabola_test"]["ori"]))
        for r0ref, r0test in zip(self.s.system["parabola_ref"]["ori"], self.s.system["parabola_test"]["ori"]):
            #print(self.assertAlmostEqual(r0ref, r0test))
            print(r0ref - r0test)
        
        # Unpack grids and check if equal
        #g0atest = self.s.generateGrids("parabola_test")
        #g0aref = self.s.generateGrids("parabola_ref")
        
        """
        for x0atest, x0aref in zip(g0atest.x.ravel(), g0aref.x.ravel()):
            self.assertAlmostEqual(x0atest, x0aref)
        
        for y0atest, y0aref in zip(g0atest.y.ravel(), g0aref.y.ravel()):
            self.assertAlmostEqual(y0atest, y0aref)
        
        for z0atest, z0aref in zip(g0atest.z.ravel(), g0aref.z.ravel()):
            self.assertAlmostEqual(z0atest, z0aref)
        for nx0atest, nx0aref in zip(g0atest.nx.ravel(), g0aref.nx.ravel()):
            print(nx0atest, nx0aref)
            self.assertAlmostEqual(nx0atest, nx0aref)
        
        for ny0atest, ny0aref in zip(g0atest.ny.ravel(), g0aref.ny.ravel()):
            self.assertAlmostEqual(ny0atest, ny0aref)
        
        for nz0atest, nz0aref in zip(g0atest.nz.ravel(), g0aref.nz.ravel()):
            self.assertAlmostEqual(nz0atest, nz0aref)
        
        for a0atest, a0aref in zip(g0atest.area.ravel(), g0aref.area.ravel()):
            self.assertAlmostEqual(a0atest, a0aref)
        # translate test parabola again
        self.s.translateGrids("parabola_test", translation1)
    
        for x1, x1test in zip(translation1 + translation0, self.s.system["parabola_test"]["pos"]):
            self.assertAlmostEqual(x1, x1test)

        # Test absolute translations
        translation0abs = np.random.rand(3)
        translation1abs = np.random.rand(3)

        self.s.translateGrids("parabola_test", translation0abs, mode="absolute")
        self.s.translateGrids("parabola_ref", translation0abs, mode="absolute")

        # Test if pos is translated properly
        for x0a, x0atest in zip(translation0abs, self.s.system["parabola_test"]["pos"]):
            self.assertAlmostEqual(x0a, x0atest)

        # Unpack grids and check if equal
        g0atest = self.s.generateGrids("parabola_test")
        g0aref = self.s.generateGrids("parabola_ref")

        for x0atest, x0aref in zip(g0atest.x.ravel(), g0aref.x.ravel()):
            self.assertAlmostEqual(x0atest, x0aref)
        
        for y0atest, y0aref in zip(g0atest.y.ravel(), g0aref.y.ravel()):
            self.assertAlmostEqual(y0atest, y0aref)
        
        for z0atest, z0aref in zip(g0atest.z.ravel(), g0aref.z.ravel()):
            self.assertAlmostEqual(z0atest, z0aref)

        self.s.homeReflector("parabola_ref")
        
        self.s.translateGrids("parabola_test", translation1abs, mode="absolute")
        self.s.translateGrids("parabola_ref", translation1abs, mode="absolute")
        
        for x1a, x1atest in zip(translation1abs, self.s.system["parabola_test"]["pos"]):
            self.assertAlmostEqual(x1a, x1atest)

        # Unpack grids and check if equal
        g1atest = self.s.generateGrids("parabola_test")
        g1aref = self.s.generateGrids("parabola_ref")

        for x1atest, x1aref in zip(g1atest.x.ravel(), g1aref.x.ravel()):
            self.assertAlmostEqual(x1atest, x1aref)
        
        for y1atest, y1aref in zip(g1atest.y.ravel(), g1aref.y.ravel()):
            self.assertAlmostEqual(y1atest, y1aref)
        
        for z1atest, z1aref in zip(g1atest.z.ravel(), g1aref.z.ravel()):
            self.assertAlmostEqual(z1atest, z1aref)
        
        self.s.homeReflector("parabola_test")
        """
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
