from vtkmodules.all import *

def main():

    sphereSource = vtkSphereSource()

    sphereSource.SetRadius(2)
    sphereSource.SetPhiResolution(40)
    sphereSource.SetThetaResolution(40)

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)

    ren = vtkRenderer()
    ren.AddActor(sphereActor)

    ren.SetBackground(1, 1, 1)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(300, 300)
    renWin.SetWindowName("Sphere")

    # Camera rotation
    for i in range(0, 360):
        renWin.Render()
        ren.GetActiveCamera().Azimuth(1)


if __name__ == "__main__":
    main()