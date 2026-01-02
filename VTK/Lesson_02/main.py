from vtkmodules.vtkFiltersSources import vtkConeSource, vtkSphereSource, vtkPlaneSource
from vtkmodules.vtkFiltersGeneral import vtkTransformPolyDataFilter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkProperty,
    vtkTexture,
    vtkLight,
)
from vtkmodules.vtkIOImage import vtkJPEGReader
from vtkmodules.vtkCommonCore import vtkCommand
from vtkmodules.vtkCommonTransforms import vtkTransform
import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2

def multiple_actors():
    coneSource = vtkConeSource()

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    coneActor = vtkActor()
    coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)
    coneActor.GetProperty().SetDiffuse(0.7)
    coneActor.GetProperty().SetSpecular(0.4)
    coneActor.GetProperty().SetSpecularPower(20)
    coneActor.GetProperty().SetOpacity(0.5)
    coneActor.SetMapper(coneMapper)

    property = vtkProperty()
    property.SetColor(1.0, 0.3882, 0.2784)
    property.SetDiffuse(0.7)
    property.SetSpecular(0.4)
    property.SetSpecularPower(20)
    property.SetOpacity(0.5)

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
    renWin.SetWindowName('Multiple Actors - Two Cones')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()

def multiple_renderers():    
    def create_cone_actor():
        cone = vtkConeSource()
        cone.SetHeight(2)
        cone.SetRadius(1)
        cone.SetResolution(60)

        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(cone.GetOutputPort())

        actor = vtkActor()
        actor.SetMapper(mapper)
        return actor

    renderer1 = vtkRenderer()
    renderer1.SetBackground(0.1, 0.2, 0.4)
    renderer1.SetViewport(0.0, 0.0, 0.5, 1.0)

    renderer2 = vtkRenderer()
    renderer2.SetBackground(0.2, 0.3, 0.4)
    renderer2.SetViewport(0.5, 0.0, 1.0, 1.0)

    cone_actor1 = create_cone_actor()
    renderer1.AddActor(cone_actor1)

    cone_actor2 = create_cone_actor()
    renderer2.AddActor(cone_actor2)

    cam2 = renderer2.GetActiveCamera()
    cam2.SetPosition(10, 0, 0)
    cam2.SetViewUp(0, 1, 0)
    cam2.Azimuth(90)

    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer1)
    ren_win.AddRenderer(renderer2)
    ren_win.SetSize(600, 300)
    ren_win.SetWindowName('Multiple Renderers')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    def rotate_callback(obj, event):
        cone_actor1.RotateZ(1)
        ren_win.Render()

    iren.AddObserver(vtkCommand.TimerEvent, rotate_callback)
    iren.CreateRepeatingTimer(100)

    iren.Initialize()
    iren.Start()

def shading_options():
    
    def create_sphere_actor():
        sphere = vtkSphereSource()
        sphere.SetRadius(1.0)
        sphere.SetThetaResolution(40)
        sphere.SetPhiResolution(40)

        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())

        actor = vtkActor()
        actor.SetMapper(mapper)
        return actor

    renderer1 = vtkRenderer()
    renderer1.SetBackground(0.1, 0.2, 0.4)
    renderer1.SetViewport(0.0, 0.0, 0.5, 1.0)

    renderer2 = vtkRenderer()
    renderer2.SetBackground(0.2, 0.3, 0.4)
    renderer2.SetViewport(0.5, 0.0, 1.0, 1.0)

    sphere_actor1 = create_sphere_actor()
    renderer1.AddActor(sphere_actor1)

    sphere_actor2 = create_sphere_actor()
    sphere_actor2.GetProperty().SetInterpolationToFlat()
    # sphere_actor2.GetProperty().SetInterpolationToGouraud()
    # sphere_actor2.GetProperty().SetInterpolationToPhong()
    renderer2.AddActor(sphere_actor2)

    cam2 = renderer2.GetActiveCamera()
    cam2.SetPosition(10, 0, 0)
    cam2.SetViewUp(0, 1, 0)
    cam2.Azimuth(90)

    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer1)
    ren_win.AddRenderer(renderer2)
    ren_win.SetSize(600, 300)
    ren_win.SetWindowName('Shading Options')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    def rotate_callback(obj, event):
        sphere_actor1.RotateZ(1)
        ren_win.Render()

    iren.AddObserver(vtkCommand.TimerEvent, rotate_callback)
    iren.CreateRepeatingTimer(100)

    iren.Initialize()
    iren.Start()

def textures():
    plane = vtkPlaneSource()
    plane.SetOrigin(0, 0, 0)
    plane.SetPoint1(0.5, 0, 0)
    plane.SetPoint2(0, 1, 0)
    plane.SetResolution(10, 10)

    jpg_reader = vtkJPEGReader()
    jpg_reader.SetFileName("formula-1-logo.JPG")
    jpg_reader.Update()

    texture = vtkTexture()
    texture.SetInputConnection(jpg_reader.GetOutputPort())

    plane_mapper = vtkPolyDataMapper()
    plane_mapper.SetInputConnection(plane.GetOutputPort())

    plane_actor = vtkActor()
    plane_actor.SetMapper(plane_mapper)
    plane_actor.SetTexture(texture)

    renderer = vtkRenderer()
    renderer.SetBackground(0.1, 0.2, 0.4)
    renderer.AddActor(plane_actor)

    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer)
    ren_win.SetSize(600, 600)
    ren_win.SetWindowName('Textures')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    iren.Initialize()
    iren.Start()


def transformation():

    def make_plane_actor(image_path: str, rot=(0, 0, 0), trans=(0, 0, 0)):
        plane = vtkPlaneSource()
        plane.SetOrigin(-0.5, -0.5, 0)
        plane.SetPoint1(0.5, -0.5, 0)
        plane.SetPoint2(-0.5, 0.5, 0)
        plane.SetResolution(10, 10)

        tf = vtkTransform()
        tf.RotateX(rot[0])
        tf.RotateY(rot[1])
        tf.RotateZ(rot[2])
        tf.Translate(trans)

        tf_filter = vtkTransformPolyDataFilter()
        tf_filter.SetTransform(tf)
        tf_filter.SetInputConnection(plane.GetOutputPort())

        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(tf_filter.GetOutputPort())

        actor = vtkActor()
        actor.SetMapper(mapper)

        reader = vtkJPEGReader()
        reader.SetFileName(image_path)
        reader.Update()

        texture = vtkTexture()
        texture.SetInputConnection(reader.GetOutputPort())
        actor.SetTexture(texture)

        return actor

    faces = [
        ("images/Im1.jpg", (0, 0, 0), (0, 0, 0.5)),
        ("images/Im2.jpg", (0, 0, 0), (0, 0, -0.5)),
        ("images/Im3.jpg", (0, 90, 0), (0, 0, 0.5)),
        ("images/Im4.jpg", (0, 90, 0), (0, 0, -0.5)),
        ("images/Im5.jpg", (90, 0, 0), (0, 0, 0.5)),
        ("images/Im6.jpg", (90, 0, 0), (0, 0, -0.5)),
    ]

    renderer = vtkRenderer()

    for img, rot, trans in faces:
        actor = make_plane_actor(img, rot, trans)
        renderer.AddActor(actor)

    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer)
    ren_win.SetSize(800, 600)
    ren_win.SetWindowName('Transform - Textured Cube')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    iren.Initialize()
    ren_win.Render()
    iren.Start()


class vtkMyCallback(object):
    def __init__(self, renderer):
        self.ren = renderer

    def __call__(self, caller, ev):
        print(caller.GetClassName(), 'Event Id:', ev)
        cam = self.ren.GetActiveCamera()
        pos = cam.GetPosition()
        print("Camera Position: %f, %f, %f" % (pos[0], pos[1], pos[2]))


def callbacks_interaction():

    cone = vtkConeSource()
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cone.GetOutputPort())
    actor = vtkActor()
    actor.SetMapper(mapper)

    renderer = vtkRenderer()
    renderer.AddActor(actor)

    ren_win = vtkRenderWindow()
    ren_win.AddRenderer(renderer)
    ren_win.SetSize(640, 480)
    ren_win.SetWindowName('Callbacks Interaction')

    cb = vtkMyCallback(renderer)
    # renderer.AddObserver(vtkCommand.AnyEvent, cb)
    # renderer.AddObserver(vtkCommand.EndEvent, cb)
    # renderer.AddObserver(vtkCommand.StartEvent, cb)
    renderer.AddObserver(vtkCommand.ResetCameraEvent, cb)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    # multiple_actors()
    # multiple_renderers()
    # shading_options()
    # textures()
    # transformation()
    callbacks_interaction()
