# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Merge_GLExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Merge_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Merge_GL"

def getLabel():
    return "Merge_GL"

def getVersion():
    return 1

def getIconPath():
    return "Merge_GL.png"

def getGrouping():
    return "Community/GLSL/Merge"

def getPluginDescription():
    return "GPU accelerated merge node for Shadertoy."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Merge_GL")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createChoiceParam("blending", "Operation")
    entries = [ ("colorBurn", ""),
    ("colorDodge", ""),
    ("darken", ""),
    ("darkerColor", ""),
    ("difference", ""),
    ("divide", ""),
    ("exclusion", ""),
    ("hardLight", ""),
    ("hardMix", ""),
    ("lighten", ""),
    ("lighterColor", ""),
    ("linearBurn", ""),
    ("linearDodge", ""),
    ("linearLight", ""),
    ("luminosity", ""),
    ("matte", ""),
    ("multiply", ""),
    ("over", ""),
    ("overlay", ""),
    ("pinLight", ""),
    ("plus", ""),
    ("saturation", ""),
    ("screen", ""),
    ("softLight", ""),
    ("spotlightBlend", ""),
    ("substract", ""),
    ("vividLight", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("over")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.blending = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createSeparatorParam("line01", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line01 = param
    del param

    param = lastNode.createStringParam("aChannels", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("A Channels")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.aChannels = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool2", "R")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool2 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool3", "G")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool3 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool4", "B")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool4 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool5", "A")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool5 = param
    del param

    param = lastNode.createStringParam("bChannels", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("B Channels")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.bChannels = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool6", "R")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool6 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool7", "G")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool7 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool8", "B")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool8 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool9", "A")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool9 = param
    del param

    param = lastNode.createSeparatorParam("line02", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line02 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat1", "Mix :")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("separator19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator19 = param
    del param

    param = lastNode.createStringParam("separator20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator20 = param
    del param

    param = lastNode.createSeparatorParam("line03", "Merge_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("separator21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator21 = param
    del param

    param = lastNode.createStringParam("separator22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator22 = param
    del param

    param = lastNode.createSeparatorParam("line04", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line04 = param
    del param

    param = lastNode.createStringParam("separator23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator23 = param
    del param

    param = lastNode.createStringParam("separator24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator24 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("separator25", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator25 = param
    del param

    param = lastNode.createStringParam("separator26", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator26 = param
    del param

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
    del param

    param = lastNode.createStringParam("separator27", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator27 = param
    del param

    param = lastNode.createStringParam("separator28", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator28 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "B"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("B")
    lastNode.setLabel("B")
    lastNode.setPosition(4139, 3647)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupB = lastNode

    del lastNode
    # End of node "B"

    # Start of node "A"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("A")
    lastNode.setLabel("A")
    lastNode.setPosition(4334, 3813)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupA = lastNode

    del lastNode
    # End of node "A"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3810)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(17, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueBool2")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool3")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool4")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool5")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool6")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool7")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool8")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool9")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//                                                \n//                                                  \n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM                                        \n//                        MM.                          .MM                                \n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM                  \n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM     \n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM  \n//                     MM.  .MMM    MMMM            MMM.  .MM    \n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM      \n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM            \n//                        MM.                          .MM                 \n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM                                                      \n//                                                                \n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : crok_logicop Matchbox pour Autodesk Flame\n//\n// Adapted to Natron by F.Fernandez\n// Original code : crok_logicop Matchbox for Autodesk Flame\n//\n//****************************************************************************/\n// \n// Filename: logicOPS_3vis.glsl\n// Author: Eric Pouliot\n//\n// Copyright (c) 2013 3vis, Inc.\n//\n//*****************************************************************************/\n//\n//\tLicense Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.\n//\t\n//\t25 of the layer blending modes from Photoshop.\n//\t\n//\tThe ones I couldn\'t figure out are from Nvidia\'s advanced blend equations extension spec -\n//\thttp://www.opengl.org/registry/specs/NV/blend_equation_advanced.txt\n//\t\n//\t~bj.2013\n//\n//*****************************************************************************/\n\n// iChannel0: B, filter = nearest\n// iChannel1: A, filter = nearest\n// iChannel1: Modulate, filter = nearest\n// BBox: iChannel0\n\n\n\nuniform int blendingMode = 17; // Operation : (blending mode), min=0., max=25.\nuniform float opacity = 1; // Mix : (mix), min=0., max=1.\n\nuniform bool Ar = true; // R\nuniform bool Ag = true; // G\nuniform bool Ab = true; // B\nuniform bool Aa = true; // A\n\nuniform bool Br = true; // R\nuniform bool Bg = true; // G\nuniform bool Bb = true; // B\nuniform bool Ba = true; // A\n\n\n//********************* fonctions ***********************//\n\nfloat overlay( float s, float d )\n{\n\treturn (d < 0.5) ? 2.0 * s * d : 1.0 - 2.0 * (1.0 - s) * (1.0 - d);\n}\n\nfloat softLight( float s, float d )\n{\n\treturn (s < 0.5) ? d - (1.0 - 2.0 * s) * d * (1.0 - d) \n\t\t: (d < 0.25) ? d + (2.0 * s - 1.0) * d * ((16.0 * d - 12.0) * d + 3.0) \n\t\t\t\t\t : d + (2.0 * s - 1.0) * (sqrt(d) - d);\n}\n\nfloat hardLight( float s, float d )\n{\n\treturn (s < 0.5) ? 2.0 * s * d : 1.0 - 2.0 * (1.0 - s) * (1.0 - d);\n}\n\nfloat vividLight( float s, float d )\n{\n\treturn (s < 0.5) ? 1.0 - (1.0 - d) / (2.0 * s) : d / (2.0 * (1.0 - s));\n}\n\nfloat pinLight( float s, float d )\n{\n\treturn (2.0 * s - 1.0 > d) ? 2.0 * s - 1.0 : (s < 0.5 * d) ? 2.0 * s : d;\n}\n\n\n\n//****************** modes de fusion ********************//\n\nvec4 colorBurn( vec4 s, vec4 d )\n{\n\treturn 1.0 - (1.0 - d) / s;\n}\n\nvec4 colorDodge( vec4 s, vec4 d )\n{\n\treturn d / (1.0 - s);\n}\n\nvec4 darken( vec4 s, vec4 d )\n{\n\tvec4 c;\n\tc = min(s,d);\n\treturn c;\n}\n\nvec4 difference( vec4 s, vec4 d )\n{\n\treturn abs(d - s);\n}\n\nvec4 darkerColor( vec4 s, vec4 d )\n{\n\treturn (s.x + s.y + s.z < d.x + d.y + d.z) ? s : d;\n}\n\nvec4 divide( vec4 s, vec4 d )\n{\n\treturn s / d;\n}\n\nvec4 exclusion( vec4 s, vec4 d )\n{\n\treturn s + d - 2.0 * s * d;\n}\n\nvec4 hardLight( vec4 s, vec4 d )\n{\n\tvec4 c;\n\tc.x = hardLight(s.x,d.x);\n\tc.y = hardLight(s.y,d.y);\n\tc.z = hardLight(s.z,d.z);\n\treturn c;\n}\n\nvec4 hardMix( vec4 s, vec4 d )\n{\n\treturn floor(s + d);\n}\n\nvec4 lighten( vec4 s, vec4 d )\n{\n\treturn max(s,d);\n}\n\nvec4 lighterColor( vec4 s, vec4 d )\n{\n\treturn (s.x + s.y + s.z > d.x + d.y + d.z) ? s : d;\n}\n\nvec4 linearBurn( vec4 s, vec4 d )\n{\n\treturn s + d - 1.0;\n}\n\nvec4 linearDodge( vec4 s, vec4 d )\n{\n\treturn s + d;\n}\n\n\nvec4 linearLight( vec4 s, vec4 d )\n{\n\treturn 2.0 * s + d - 1.0;\n}\n\nvec4 screen( vec4 s, vec4 d )\n{\n\treturn s + d - s * d;\n}\n\nvec4 screenMode( vec4 s, vec4 d )\n{\n\tvec4 c;\n\tc = 1.0-((1.0-s)*(1.0-d));\n\treturn c;\n}\n\nvec4 matte( vec4 s, vec4 d)\n{\n\tvec4 c = vec4(0,0,0,0);\n\tc = (s*s.a) + (d*(1-s.a));\n\tc.a = s.a;\n\treturn c;\n}\n\nvec4 multiply( vec4 s, vec4 d )\n{\n\treturn s*d;\n}\n\nvec4 overlay( vec4 s, vec4 d )\n{\n\tvec4 c;\n\tc.x = overlay(s.x,d.x);\n\tc.y = overlay(s.y,d.y);\n\tc.z = overlay(s.z,d.z);\n\treturn c;\n}\n\nvec4 pinLight( vec4 s, vec4 d )\n{\n\tvec4 c;\n\tc.x = pinLight(s.x,d.x);\n\tc.y = pinLight(s.y,d.y);\n\tc.z = pinLight(s.z,d.z);\n\treturn c;\n}\n\nvec4 plus( vec4 s, vec4 d )\n{\n\treturn s + d;\n}\n\nvec4 softLight( vec4 s, vec4 d )\n{\n\tvec4 c;\n\tc.x = softLight(s.x,d.x);\n\tc.y = softLight(s.y,d.y);\n\tc.z = softLight(s.z,d.z);\n\treturn c;\n}\n\nvec4 spotlightBlend( vec4 s, vec4 d )\n{\n\treturn d*s+d;\n}\n\nvec4 substract( vec4 s, vec4 d )\n{\n\treturn s - d;\n}\n\nvec4 vividLight( vec4 s, vec4 d )\n{\n\tvec4 c;\n\tc.x = vividLight(s.x,d.x);\n\tc.y = vividLight(s.y,d.y);\n\tc.z = vividLight(s.z,d.z);\n\treturn c;\n}\n\nvec4 luminosity( vec4 s, vec4 d )\n{\n\tfloat dLum = dot(d, vec4(0.3, 0.59, 0.11,0));\n\tfloat sLum = dot(s, vec4(0.3, 0.59, 0.11,0));\n\tfloat lum = sLum - dLum;\n\tvec4 c = d + lum;\n\tfloat minC = min(min(c.x, c.y), c.z);\n\tfloat maxC = max(max(c.x, c.y), c.z);\n\tif(minC < 0.0) return sLum + ((c - sLum) * sLum) / (sLum - minC);\n\telse if(maxC > 1.0) return sLum + ((c - sLum) * (1.0 - sLum)) / (maxC - sLum);\n\telse return c;\n}\n\nvec4 over( vec4 s, vec4 d )\n{\n\tvec4 c;\n\tc = s + ( d*(1-s.a) );\n\treturn c;\n}\n\n\n\n\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\n\tvec2 uv = fragCoord.xy / iResolution.xy;\n\n\t// source texture (upper layer)\n\tvec4 s = texture2D(iChannel1, uv);\n\t\n\t// destination texture (lower layer)\n\tvec4 d = texture2D(iChannel0, uv);\n\n\t// mask texture (mask entry)\n\tvec4 mask = texture2D(iChannel2, uv);\n\n\tvec4 c = vec4(0.0);\n\n\n\t// ########### selection des couches ########### //\n\n\tif(Ar == false)\n\t\ts.r = 0;\n\n\tif(Ag == false)\n\t\ts.g = 0;\n\n\tif(Ab == false)\n\t\ts.b = 0;\n\n\tif(Aa == false)\n\t\ts.a = 0;\n\n\tif(Br == false)\n\t\td.r = 0;\n\n\tif(Bg == false)\n\t\td.g = 0;\n\n\tif(Bb == false)\n\t\td.b = 0;\n\n\tif(Ba == false)\n\t\td.a = 0;\n\n\t// ########### selection des modes de fusion ########### //\n\n\tif( blendingMode == 0)\n\t   \tc =  c + colorBurn(s,d);\n\n\telse if( blendingMode == 1)\n\t   \tc =  c + colorDodge(s,d);\n\n\telse if( blendingMode == 2)\n\t   \tc =  c + darken(s,d);\n\n\telse if(blendingMode == 3)\n\t\tc =  c + darkerColor(s,d);\t\t\n\n\telse if(blendingMode == 4)\n\t\tc =  c + difference(s,d);\n\n\telse if(blendingMode == 5)\n\t\tc =  c + divide(s,d);\n\n\telse if(blendingMode == 6)\n\t\tc =  c + exclusion(s,d);\n\n\telse if(blendingMode == 7)\n\t\tc =  c + hardLight(s,d);\n\n\telse if(blendingMode == 8)\n\t\tc =  c + hardMix(s,d);\n\n\telse if(blendingMode == 9)\n\t\tc =  c + lighten(s,d);\t\t\n\n\telse if(blendingMode == 10)\n\t\tc =  c + lighterColor(s,d);\n\n\telse if(blendingMode == 11)\n\t\tc =  c + linearBurn(s,d);\n\n\telse if(blendingMode == 12)\n\t\tc =  c + linearDodge(s,d);\n\n\telse if(blendingMode == 13)\n\t\tc =  c + linearLight(s,d);\t\t\n\n\telse if(blendingMode == 14)\n\t\tc =  c + luminosity(s,d);\n\n\telse if(blendingMode == 15)\n\t\tc =  c + matte(s,d);\n\n\telse if(blendingMode == 16)\n\t\tc =  c + multiply(s,d);\n\n\telse if(blendingMode == 17)\n\t\tc =  c + over(s,d);\n\n\telse if(blendingMode == 18)\n\t\tc =  c + overlay(s,d);\n\n\telse if(blendingMode == 19)\n\t\tc =  c + pinLight(s,d);\n\n\telse if(blendingMode == 20)\n\t\tc =  c + plus(s,d);\n\n\telse if(blendingMode == 21)\n\t\tc =  c + screenMode(s,d);\t\t\n\n\telse if(blendingMode == 22)\n\t\tc =  c + softLight(s,d);\n\n\telse if(blendingMode == 23)\n\t\tc =  c + spotlightBlend(s,d);\n\n\telse if(blendingMode == 24)\n\t\tc =  c + substract(s,d);\n\n\telse if(blendingMode == 25)\n\t\tc =  c + vividLight(s,d);\n\n\t// grabbing the result\n\tvec4 result = vec4(c.rgb, s.a);\n\n\n\n\n\n\t// multiplying the result by the opacity\n\tfragColor = mix(d, result, opacity);\n}\t")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("B")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("A")
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("blendingMode")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Operation :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("blending mode")
        del param

    param = lastNode.getParam("paramDefaultInt0")
    if param is not None:
        param.setValue(17, 0)
        del param

    param = lastNode.getParam("paramMinInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt0")
    if param is not None:
        param.setValue(25, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("opacity")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Mix :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("mix")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("Ar")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("R")
        del param

    param = lastNode.getParam("paramDefaultBool2")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("Ag")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("G")
        del param

    param = lastNode.getParam("paramDefaultBool3")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("Ab")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("B")
        del param

    param = lastNode.getParam("paramDefaultBool4")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("Aa")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("A")
        del param

    param = lastNode.getParam("paramDefaultBool5")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("Br")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("R")
        del param

    param = lastNode.getParam("paramDefaultBool6")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("Bg")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("G")
        del param

    param = lastNode.getParam("paramDefaultBool7")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType8")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName8")
    if param is not None:
        param.setValue("Bb")
        del param

    param = lastNode.getParam("paramLabel8")
    if param is not None:
        param.setValue("B")
        del param

    param = lastNode.getParam("paramDefaultBool8")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType9")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName9")
    if param is not None:
        param.setValue("Ba")
        del param

    param = lastNode.getParam("paramLabel9")
    if param is not None:
        param.setValue("A")
        del param

    param = lastNode.getParam("paramDefaultBool9")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupB)
    groupShadertoy1_2.connectInput(1, groupA)

    param = groupShadertoy1_2.getParam("paramValueInt0")
    param.setExpression("thisGroup.blending.get()", False, 0)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat1")
    group.getParam("Shadertoy1_2paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool2")
    group.getParam("Shadertoy1_2paramValueBool2").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool3")
    group.getParam("Shadertoy1_2paramValueBool3").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool4")
    group.getParam("Shadertoy1_2paramValueBool4").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool5")
    group.getParam("Shadertoy1_2paramValueBool5").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool6")
    group.getParam("Shadertoy1_2paramValueBool6").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool7")
    group.getParam("Shadertoy1_2paramValueBool7").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool8")
    group.getParam("Shadertoy1_2paramValueBool8").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool9")
    group.getParam("Shadertoy1_2paramValueBool9").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Merge_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
