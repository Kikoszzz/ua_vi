from vtkmodules.all import *

def create_renderer(background=(1, 1, 1)):
    ren = vtkRenderer()
    ren.SetBackground(*background)
    return ren

def create_render_window(renderer, size=(600, 600), title="Textures"):
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

def create_plane():
    plane = vtkPlaneSource()
    plane.SetOrigin(0, 0, 0)
    plane.SetPoint1(1, 0, 0)
    plane.SetPoint2(0, 1, 0)
    plane.SetResolution(10, 10)
    return plane

def apply_texture_to_plane(plane):

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

    return plane_actor

def main():
    renderer = create_renderer(background=(0.1, 0.2, 0.4))  # Set background color for visibility

    plane = create_plane()
    plane_actor = apply_texture_to_plane(plane)

    plane.SetPoint1(0.5, 0, 0)
    plane.SetPoint2(0, 1, 0)

    renderer.AddActor(plane_actor)

    render_window = create_render_window(renderer)

    start_interactor(render_window)

if __name__ == "__main__":
    main()
