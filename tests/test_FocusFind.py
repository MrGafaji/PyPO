import sys
import random

import unittest
import numpy as np

from src.PyPO.System import System
##
# @file
# 
# Script for testing the focus finding functionality of PyPO.

class Test_FocusFind(unittest.TestCase):
    def test_FocusFind_parabola(self):
        runRTDict = {
                "fr_in"     : "start",
                "fr_out"    : "fr_par",
                "t_name"    : "parabola",
                "tol"       : 1e-12,
                "device"    : "CPU"
                }
        for i in range(100):
            self._RT_random_parabola()
            
            self.s.runRayTracer(runRTDict)
            foc_find = self.s.findRTfocus("fr_par")

            for fp, ff in zip(self.s.system["parabola"]["focus_1"], foc_find):
                self.assertAlmostEqual(fp, ff, delta=1e-3)

            del self.s

    def _RT_random_parabola(self):
        self.s = System(verbose=False)

        TubeRTDict = {
                "name"      : "start",
                "nRays"     : 10,
                "nRing"     : 10,
                "angx0"     : 0,
                "angy0"     : 0,
                "x0"        : 1,
                "y0"        : 1
                }

        self.s.createTubeFrame(TubeRTDict)

        focus = np.array([0, 0, random.uniform(0,10)])

        parabola = {
                "name"      : "parabola",
                "gmode"     : "uv",
                "pmode"     : "focus",
                "focus_1"   : focus,
                "vertex"    : np.zeros(3),
                "lims_u"    : np.array([0, 1]),
                "lims_v"    : np.array([0, 360]),
                "gridsize"  : np.array([101, 101])
                }

        self.s.addParabola(parabola)
        self.s.translateGrids("start", focus, obj="frame")
    
    def test_FocusFind_ellipse_z(self):
        runRTDict = {
                "fr_in"     : "start",
                "fr_out"    : "fr_ell",
                "t_name"    : "ellipse",
                "tol"       : 1e-12,
                "device"    : "CPU"
                }
        for i in range(100):
            self._RT_random_ellipse("z")
            
            self.s.runRayTracer(runRTDict)
            foc_find = self.s.findRTfocus("fr_ell")

            #self.s.plotSystem(RTframes=["start", "fr_ell", "focus_fr_ell"])
            for fp, ff in zip(self.s.system["ellipse"]["focus_2"], foc_find):
                self.assertAlmostEqual(fp, ff, delta=1e-1)
            
            del self.s
            
    def test_FocusFind_ellipse_x(self):
        runRTDict = {
                "fr_in"     : "start",
                "fr_out"    : "fr_ell",
                "t_name"    : "ellipse",
                "tol"       : 1e-12,
                "device"    : "CPU"
                }
        for i in range(100):
            self._RT_random_ellipse("x")
           
            self.s.runRayTracer(runRTDict)
            foc_find = self.s.findRTfocus("fr_ell")
   
            #self.s.plotSystem(RTframes=["start", "fr_ell", "focus_fr_ell"])
            for fp, ff in zip(self.s.system["ellipse"]["focus_2"], foc_find):
                 self.assertAlmostEqual(fp, ff, delta=1e-1)
   
            del self.s

    def _RT_random_ellipse(self, orient):
        self.s = System(verbose=False)

        TubeRTDict = {
                "name"      : "start",
                "nRays"     : 10,
                "nRing"     : 10,
                "angx0"     : 10,
                "angy0"     : 10,
                "x0"        : 0,
                "y0"        : 0
                }

        self.s.createTubeFrame(TubeRTDict)

        if orient == "z":
            focus1 = np.array([0, 0, random.uniform(0,1)])
        else:
            focus1 = np.array([random.uniform(0,1), 0, 0])

        focus2 = -focus1 

        ellipse = {
                "name"      : "ellipse",
                "gmode"     : "uv",
                "pmode"     : "focus",
                "orient"    : orient,        
                "flip"      : True,
                "focus_1"   : focus1,
                "focus_2"   : focus2,
                "ecc"       : random.uniform(0.4, 0.7),
                "lims_u"    : np.array([0, 1]),
                "lims_v"    : np.array([0, 360]),
                "gridsize"  : np.array([101, 101])
                }

        self.s.addEllipse(ellipse)
        
        #tilt_frame = np.random.rand(3) * 1
        
        #self.s.rotateGrids("start", tilt_frame, obj="frame")
        self.s.translateGrids("start", focus1, obj="frame")

if __name__ == "__main__":
    unittest.main()
