from vtkmodules.all import *

def create_renderer(background=(1, 1, 1)):
    ren = vtkRenderer()
    ren.SetBackground(*background)
    return ren

def create_render_window(renderer1, renderer2, size=(600, 300), title="Lesson 1"):
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer1)
    ren_win.AddRenderer(renderer2)
    ren_win.SetSize(*size)
    ren_win.SetWindowName(title)
    return ren_win

def start_interactor(render_window):
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(render_window)
    iren.Initialize()
    iren.Start()
    return iren

# Sphere
def exercise_sphere(renderer):
    sphere = vtkSphereSource()
    sphere.SetRadius(1.0)
    sphere.SetThetaResolution(40)
    sphere.SetPhiResolution(40)

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    renderer.AddActor(actor)
    return actor

def rotate_sphere(sphere_actor, ren_win, renderer1, renderer2, iren):
    def rotate_sphere_callback(obj, event):
        sphere_actor.RotateZ(1)
        renderer1.GetRenderWindow().Render()
        renderer2.GetRenderWindow().Render()

    iren.AddObserver('TimerEvent', rotate_sphere_callback)
    iren.CreateRepeatingTimer(100)

def addLight(renderer, color, position):
    light = vtkLight()
    light.SetColor(color)
    light.SetPosition(position)
    light.SetFocalPoint(0, 0, 0)
    renderer.AddLight(light)

    sphere = vtkSphereSource()
    sphere.SetRadius(0.5)

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.SetPosition(*position)
    actor.GetProperty().SetColor(*color)
    actor.GetProperty().LightingOff()

    renderer.AddActor(actor)


def main():
    renderer1 = create_renderer(background=(0.1, 0.2, 0.4))
    renderer2 = create_renderer(background=(0.2, 0.3, 0.4))

    renderer1.SetViewport(0.0, 0.0, 0.5, 1.0)
    renderer2.SetViewport(0.5, 0.0, 1.0, 1.0)

    sphere_actor1 = exercise_sphere(renderer1)

    sphere_actor2 = exercise_sphere(renderer2)

    sphere_actor2.GetProperty().SetInterpolationToFlat()
    # sphere_actor2.GetProperty().SetInterpolationToGouraud()
    # sphere_actor2.GetProperty().SetInterpolationToPhong()

    cam2 = renderer2.GetActiveCamera()
    cam2.SetPosition(10, 0, 0)
    cam2.SetViewUp(0, 1, 0)
    cam2.Azimuth(90)

    ren_win = create_render_window(renderer1, renderer2, title="Shading Options")
    iren = start_interactor(ren_win)

    rotate_sphere(sphere_actor1, ren_win, renderer1, renderer2, iren)

    iren.Start()

if __name__ == "__main__":
    main()
