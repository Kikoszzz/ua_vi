from vtkmodules.vtkFiltersSources import *
from vtkmodules.vtkFiltersCore import *
from vtkmodules.vtkRenderingCore import *
from vtkmodules.vtkCommonCore import *
from vtkmodules.vtkCommonDataModel import *
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2


class callBack:
    def __init__(self, picker, sphere_actor, render_window, text_mapper=None, text_actor=None):
        self.picker = picker
        self.sphere_actor = sphere_actor
        self.render_window = render_window
        self.text_mapper = text_mapper
        self.text_actor = text_actor
    
    def __call__(self, caller, event):
        pick_pos = self.picker.GetPickPosition()
        print(f"Picked point coordinates: ({pick_pos[0]:.3f}, {pick_pos[1]:.3f}, {pick_pos[2]:.3f})")
        
        self.sphere_actor.SetPosition(pick_pos)
        self.sphere_actor.VisibilityOn()
        
        if self.text_mapper and self.text_actor:
            selection_point = self.picker.GetSelectionPoint()
            
            coord_text = f"3D: ({pick_pos[0]:.2f}, {pick_pos[1]:.2f}, {pick_pos[2]:.2f})\n2D: ({selection_point[0]:.0f}, {selection_point[1]:.0f})"
            self.text_mapper.SetInput(coord_text)
            
            self.text_actor.SetPosition(selection_point[0] + 10, selection_point[1] + 10)
            self.text_actor.VisibilityOn()
        
        self.render_window.Render()


def glyphing():
    coneSource = vtkConeSource()
    coneSource.SetResolution(16)
    
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(50)
    sphereSource.SetPhiResolution(50)
    
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())
    
    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    
    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputConnection(sphereSource.GetOutputPort())
    glyph.SetScaleFactor(0.2)
    glyph.SetVectorModeToUseNormal()
    
    glyphMapper = vtkPolyDataMapper()
    glyphMapper.SetInputConnection(glyph.GetOutputPort())
    
    glyphActor = vtkActor()
    glyphActor.SetMapper(glyphMapper)
    
    renderer = vtkRenderer()
    renderer.AddActor(sphereActor)
    renderer.AddActor(glyphActor)
    
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(800, 600)
    renderWindow.SetWindowName("Lesson 3 - Glyphing")
    
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    
    style = vtkInteractorStyleTrackballCamera()
    style.SetCurrentRenderer(renderer)
    interactor.SetInteractorStyle(style)
    
    renderWindow.Render()
    interactor.Start()


def object_picking():
    coneSource = vtkConeSource()
    coneSource.SetResolution(16)
    
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(8)
    sphereSource.SetPhiResolution(8)
    
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())
    
    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    
    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputConnection(sphereSource.GetOutputPort())
    glyph.SetScaleFactor(0.2)
    glyph.SetVectorModeToUseNormal()
    
    glyphMapper = vtkPolyDataMapper()
    glyphMapper.SetInputConnection(glyph.GetOutputPort())
    
    glyphActor = vtkActor()
    glyphActor.SetMapper(glyphMapper)
    
    pickerSphereSource = vtkSphereSource()
    pickerSphereSource.SetRadius(0.05)
    
    pickerSphereMapper = vtkPolyDataMapper()
    pickerSphereMapper.SetInputConnection(pickerSphereSource.GetOutputPort())
    
    pickerSphereActor = vtkActor()
    pickerSphereActor.SetMapper(pickerSphereMapper)
    pickerSphereActor.GetProperty().SetColor(1, 0, 0)
    pickerSphereActor.VisibilityOff()
    
    textMapper = vtkTextMapper()
    textProperty = textMapper.GetTextProperty()
    textProperty.SetFontFamilyToCourier()
    textProperty.SetFontSize(12)
    textProperty.BoldOn()
    textProperty.SetJustificationToCentered()
    textProperty.SetColor(1, 1, 1)
    
    textActor = vtkActor2D()
    textActor.SetMapper(textMapper)
    textActor.VisibilityOff()
    
    renderer = vtkRenderer()
    renderer.AddActor(sphereActor)
    renderer.AddActor(glyphActor)
    renderer.AddActor(pickerSphereActor)
    renderer.AddActor(textActor)
    
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(800, 600)
    renderWindow.SetWindowName("Lesson 3 - Object Picking")
    
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    
    style = vtkInteractorStyleTrackballCamera()
    style.SetCurrentRenderer(renderer)
    interactor.SetInteractorStyle(style)
    
    picker = vtkPointPicker()
    callback = callBack(picker, pickerSphereActor, renderWindow, textMapper, textActor)
    picker.AddObserver(vtkCommand.EndPickEvent, callback)
    interactor.SetPicker(picker)
    
    renderWindow.Render()
    interactor.Start()

def unstructured_grid():
    coords = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1]]
    
    ugrid = vtkUnstructuredGrid()
    points = vtkPoints()
    
    for i in range(len(coords)):
        points.InsertPoint(i, coords[i])
    
    for i in range(len(coords)):
        ugrid.InsertNextCell(VTK_VERTEX, 1, [i])
    
    ugrid.SetPoints(points)
    
    ugridMapper = vtkDataSetMapper()
    ugridMapper.SetInputData(ugrid)
    
    ugridActor = vtkActor()
    ugridActor.SetMapper(ugridMapper)
    ugridActor.GetProperty().SetColor(1, 0, 0)
    ugridActor.GetProperty().SetPointSize(5)
    
    renderer = vtkRenderer()
    renderer.AddActor(ugridActor)
    
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(800, 600)
    renderWindow.SetWindowName("Lesson 3 - Unstructured Grid")
    
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    
    renderWindow.Render()
    interactor.Start()


def scalar_vector_association():
    coords = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1]]
    vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
    scalars = [0.1, 0.3, 0.5, 0.8]
    
    ugrid = vtkUnstructuredGrid()
    points = vtkPoints()
    
    for i in range(len(coords)):
        points.InsertPoint(i, coords[i])
    
    for i in range(len(coords)):
        ugrid.InsertNextCell(VTK_VERTEX, 1, [i])
    
    ugrid.SetPoints(points)
    
    vectorArray = vtkFloatArray()
    vectorArray.SetNumberOfComponents(3)
    vectorArray.SetName("Vectors")
    
    for vec in vectors:
        vectorArray.InsertNextTuple3(vec[0], vec[1], vec[2])
    
    ugrid.GetPointData().SetVectors(vectorArray)
    
    scalarArray = vtkFloatArray()
    scalarArray.SetNumberOfComponents(1)
    scalarArray.SetName("Scalars")
    
    for scalar in scalars:
        scalarArray.InsertNextValue(scalar)
    
    ugrid.GetPointData().SetScalars(scalarArray)
    
    coneSource = vtkConeSource()
    coneSource.SetResolution(16)
    
    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputData(ugrid)
    glyph.SetVectorModeToUseVector()
    glyph.SetScaleModeToScaleByScalar()
    glyph.SetScaleFactor(0.5)
    glyph.OrientOn()
    #glyph.OrientOff()
    #glyph.SetColorModeToColorByScalar()
    glyph.SetColorModeToColorByScalar()
    
    glyphMapper = vtkPolyDataMapper()
    glyphMapper.SetInputConnection(glyph.GetOutputPort())
    glyphMapper.SetScalarRange(0.1, 0.8)
    
    glyphActor = vtkActor()
    glyphActor.SetMapper(glyphMapper)
    
    renderer = vtkRenderer()
    renderer.AddActor(glyphActor)
    
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(800, 600)
    renderWindow.SetWindowName("Lesson 3 - Scalar and Vector Association")
    
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    
    renderWindow.Render()
    interactor.Start()


def hedgehog():
    coords = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1]]
    vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
    scalars = [0.1, 0.3, 0.5, 0.8]

    ugrid = vtkUnstructuredGrid()
    points = vtkPoints()

    for i in range(len(coords)):
        points.InsertPoint(i, coords[i])

    for i in range(len(coords)):
        ugrid.InsertNextCell(VTK_VERTEX, 1, [i])

    ugrid.SetPoints(points)

    vectorArray = vtkFloatArray()
    vectorArray.SetNumberOfComponents(3)
    vectorArray.SetName("Vectors")

    for vec in vectors:
        vectorArray.InsertNextTuple3(vec[0], vec[1], vec[2])

    ugrid.GetPointData().SetVectors(vectorArray)

    scalarArray = vtkFloatArray()
    scalarArray.SetNumberOfComponents(1)
    scalarArray.SetName("Scalars")

    for scalar in scalars:
        scalarArray.InsertNextValue(scalar)

    ugrid.GetPointData().SetScalars(scalarArray)

    hedgehog = vtkHedgeHog()
    hedgehog.SetInputData(ugrid)
    hedgehog.SetScaleFactor(0.4)

    hedgeMapper = vtkPolyDataMapper()
    hedgeMapper.SetInputConnection(hedgehog.GetOutputPort())
    hedgeMapper.SetScalarRange(0.1, 0.8)

    hedgeActor = vtkActor()
    hedgeActor.SetMapper(hedgeMapper)

    renderer = vtkRenderer()
    renderer.AddActor(hedgeActor)

    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(800, 600)
    renderWindow.SetWindowName("Lesson 3 - HedgeHog")

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    renderWindow.Render()
    interactor.Start()


if __name__ == "__main__":
    #glyphing()
    #object_picking()
    #unstructured_grid()
    #scalar_vector_association()
    hedgehog()