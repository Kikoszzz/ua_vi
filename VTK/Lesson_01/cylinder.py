from vtkmodules.all import *

def main():

    cylinderSource = vtkCylinderSource()

    cylinderSource.SetRadius(2)
    cylinderSource.SetHeight(3)
    cylinderSource.SetResolution(40)

    cylinderMapper = vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinderSource.GetOutputPort())

    cylinderActor = vtkActor()
    cylinderActor.SetMapper(cylinderMapper)

    ren = vtkRenderer()
    ren.AddActor(cylinderActor)
    ren.SetBackground(1, 1, 1)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(300, 300)
    renWin.SetWindowName("Cylinder")

    # Camera rotation
    for i in range(0, 900):
        renWin.Render()
        # ren.GetActiveCamera().Azimuth(1)


if __name__ == "__main__":
    main()