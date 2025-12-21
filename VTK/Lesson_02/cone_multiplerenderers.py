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

# Cone
def exercise_cone(renderer):
    cone = vtkConeSource()
    cone.SetHeight(2)
    cone.SetRadius(1)
    cone.SetResolution(60)

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cone.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)

    renderer.AddActor(actor)
    return actor

def rotate_cone(cone_actor, ren_win, renderer1, renderer2, iren):
    def rotate_cone_callback(obj, event):
        cone_actor.RotateZ(1)
        renderer1.GetRenderWindow().Render()
        renderer2.GetRenderWindow().Render()

    iren.AddObserver('TimerEvent', rotate_cone_callback)
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

# Main function
def main():
    renderer1 = create_renderer(background=(0.1, 0.2, 0.4))
    renderer2 = create_renderer(background=(0.2, 0.3, 0.4))

    renderer1.SetViewport(0.0, 0.0, 0.5, 1.0)
    renderer2.SetViewport(0.5, 0.0, 1.0, 1.0)

    cone_actor1 = exercise_cone(renderer1)

    cone_actor2 = exercise_cone(renderer2)

    cam2 = renderer2.GetActiveCamera()
    cam2.SetPosition(10, 0, 0)
    cam2.SetViewUp(0, 1, 0)
    cam2.Azimuth(90)

    ren_win = create_render_window(renderer1, renderer2, title="Multiple Renderers – VTK")

    iren = start_interactor(ren_win)

    rotate_cone(cone_actor1, ren_win, renderer1, renderer2, iren)

    iren.Start()

if __name__ == "__main__":
    main()
