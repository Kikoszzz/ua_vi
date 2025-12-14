from vtkmodules.all import *

def main():
    
    coneSource = vtkConeSource()
    coneSource.SetHeight(2)
    coneSource.SetRadius(1)

    coneSource.SetResolution(60)
  
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection( coneSource.GetOutputPort() )
  
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    ren = vtkRenderer()
    ren.AddActor(coneActor)

    ren.SetBackground(1, 1, 1)

    cam1 = vtkCamera()
    
    # cam1.SetPosition(10, 0, 0)
    # cam1.SetViewUp(0, 1, 0)
    
    # cam1.SetPosition(10, 10, 0)
    # cam1.SetViewUp(0, 1, 1)
    # ren.SetActiveCamera(cam1)

    # Same result without creating a new camera
    # cam = ren.GetActiveCamera()
    # cam.SetPosition(10, 0, 0)
    # cam.SetViewUp(0, 1, 0)

    cube = vtkCubeSource()
    cubeMapper = vtkPolyDataMapper()
    cubeMapper.SetInputConnection(cube.GetOutputPort())

    cubeActor = vtkActor()
    cubeActor.SetMapper(cubeMapper)
    cubeActor.GetProperty().SetRepresentationToWireframe()

    # ren.AddActor(cubeActor)

    # Appearance in orthographic projection:
        # No perspective distortion
        # Parallel lines remain parallel
        # The cube's edges do not converge
        # Faces appear the same size regardless of distance
        # Rotating the camera produces architectural-style drawings instead of the 3D-depth look
    # cam = ren.GetActiveCamera()
    # cam.SetParallelProjection(True)

    # cam1 = ren.GetActiveCamera()
    # light = vtkLight()
    # # Create a pure red light source
    # light.SetColor(1, 0, 0)
    # # Place the light exactly at the camera's eye position, pointing in the same direction as the camera.
    # light.SetFocalPoint(cam1.GetFocalPoint())
    # light.SetPosition(cam1.GetPosition())
    # ren.AddLight(light)
    # # Effects:
    #     # Whole scene becomes illuminated with a red tint
    #         # The cone appears red-tinted, regardless of the origial material color
    #     # There are no shadows
    #         # No part of the cone becomes darker unless it faces away from the camera
    #     # The lighting follows the camera
    # # This happens because the light and the camera share the same position and direction



    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer.
    # We also set the size to be 300 pixels by 300.
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetWindowName('Cone')
    # VTK's default render window size is 300 × 300 pixels if not changed.
    renWin.SetSize(300, 300)

    # # Now we loop over 360 degrees and render the cone each time.
    # for i in range(0,360):
    #     # render the image
    #     renWin.Render()
    #     # rotate the active camera by one degree
    #     ren.GetActiveCamera().Azimuth(1)

    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()