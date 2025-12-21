###############################################################################
#       						Cone.py
###############################################################################

from vtkmodules.all import *


# Import only needed modules
# import vtkmodules.vtkInteractionStyle
# import vtkmodules.vtkRenderingOpenGL2
# from vtkmodules.vtkFiltersSources import vtkConeSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# )

def main():
    coneSource = vtkConeSource()

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())


    property = vtkProperty()
    property.SetColor(1.0, 0.3882, 0.2784)
    property.SetDiffuse(0.7)
    property.SetSpecular(0.4)
    property.SetSpecularPower(20)
    property.SetOpacity(0.5)

    coneActor = vtkActor()
    coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)
    coneActor.GetProperty().SetDiffuse(0.7)
    coneActor.GetProperty().SetSpecular(0.4)
    coneActor.GetProperty().SetSpecularPower(20)
    coneActor.GetProperty().SetOpacity(0.5)
    coneActor.SetMapper(coneMapper)

    coneActor2 = vtkActor()
    coneActor2.SetMapper(coneMapper)
    coneActor2.SetPosition(0, 2, 0)
    coneActor2.SetProperty(property)

    ren = vtkRenderer()
    ren.AddActor(coneActor)
    ren.AddActor(coneActor2)
    ren.SetBackground(1.0, 0.55, 0.41)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetSize(640, 480)
    renWin.SetWindowName('Cone')


    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()