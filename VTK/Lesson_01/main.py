from vtkmodules.all import *

def create_renderer(background=(1, 1, 1)):
    ren = vtkRenderer()
    ren.SetBackground(*background)
    return ren

def create_render_window(renderer, size=(300, 300), title="Lesson 1"):
    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer)
    ren_win.SetSize(*size)
    ren_win.SetWindowName(title)
    return ren_win

def start_interactor(render_window):
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(render_window)
    iren.Initialize()
    iren.Start()


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


# Sphere
# Cylinder
def exercise_other_primitives(renderer):
    # Sphere
    sphere = vtkSphereSource()
    sphere.SetRadius(2)
    sphere.SetThetaResolution(40)
    sphere.SetPhiResolution(40)

    sphere_mapper = vtkPolyDataMapper()
    sphere_mapper.SetInputConnection(sphere.GetOutputPort())

    sphere_actor = vtkActor()
    sphere_actor.SetMapper(sphere_mapper)

    # Cylinder
    cylinder = vtkCylinderSource()
    cylinder.SetRadius(2)
    cylinder.SetHeight(3)
    cylinder.SetResolution(40)

    cylinder_mapper = vtkPolyDataMapper()
    cylinder_mapper.SetInputConnection(cylinder.GetOutputPort())

    cylinder_actor = vtkActor()
    cylinder_actor.SetMapper(cylinder_mapper)
    
    # renderer.AddActor(sphere_actor)
    renderer.AddActor(cylinder_actor)


# Camera control
def exercise_camera_control(renderer):
    # cam1 = vtkCamera()
    # cam1.SetPosition(10, 0, 0)
    # cam1.SetViewUp(0, 1, 0)

    # cam1.SetPosition(10, 10, 0)
    # cam1.SetViewUp(0, 1, 1)

    # renderer.SetActiveCamera(cam1)

    cam = renderer.GetActiveCamera()
    cam.SetPosition(10, 0, 0)
    cam.SetViewUp(0, 1, 0)


# Orthographic projection + cube
def exercise_orthographic_cube(renderer):
    cube = vtkCubeSource()

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cube.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetRepresentationToWireframe()

    renderer.AddActor(actor)

    cam = renderer.GetActiveCamera()
    cam.SetParallelProjection(True)


# Lighting – camera light
def exercise_camera_light(renderer):
    exercise_cone(renderer)

    cam = renderer.GetActiveCamera()

    light = vtkLight()
    light.SetColor(1, 0, 0)
    light.SetPosition(cam.GetPosition())
    light.SetFocalPoint(cam.GetFocalPoint())

    renderer.AddLight(light)


# Actor properties
def exercise_actor_properties(actor):
    actor.GetProperty().SetColor(1, 0, 0)   # Vermelho
    actor.GetProperty().SetOpacity(0.5)

    # actor.GetProperty().SetRepresentationToPoints()
    # actor.GetProperty().SetRepresentationToWireframe()




# Multiple lights + spheres
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


# Configuração de múltiplas luzes com cores e posições específicas
def exercise_multiple_lights(renderer):
    addLight(renderer, (1, 0, 0), (-5, 0, 0))  # Vermelho
    addLight(renderer, (0, 1, 0), (0, 0, -5))  # Verde
    addLight(renderer, (0, 0, 1), (5, 0, 0))   # Azul
    addLight(renderer, (1, 1, 0), (0, 0, 5))   # Amarelo


def main():
    renderer = create_renderer()

    cone_actor = exercise_cone(renderer)
    # exercise_camera_control(renderer)
    # exercise_other_primitives(renderer)
    # exercise_orthographic_cube(renderer)
    # exercise_camera_light(renderer)
    # exercise_actor_properties(cone_actor)
    exercise_multiple_lights(renderer)

    ren_win = create_render_window(renderer, title="Lesson 1 – VTK")
    start_interactor(ren_win)


if __name__ == "__main__":
    main()
