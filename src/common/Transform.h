#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <string>
#include <array>

#include "Structs.h"
#include "Utils.h"

#ifdef _WIN32
#   define PYPO_DLL __declspec(dllexport)
#else
#   define PYPO_DLL
#endif

#ifndef __Transform_h
#define __Transform_h

/*! \file Transform.h
    \brief Transformations for frames and fields/currents.
*/
extern "C"
{
    PYPO_DLL void transformRays(cframe *fr, double *mat);
}

#endif
