from vtkmodules.all import *


class MyCallback(vtkCommand):
    """Callback class for picking events"""
    def __init__(self, picker, text_mapper, text_actor, marker_sphere):
        super().__init__()
        self.picker = picker
        self.text_mapper = text_mapper
        self.text_actor = text_actor
        self.marker_sphere = marker_sphere
    
    def Execute(self, obj, event):
        """Execute callback when picking event occurs"""
        if event == "EndPickEvent":
            # Get the picked point coordinates (3D world coordinates)
            pick_pos = self.picker.GetPickPosition()
            
            # Get pixel coordinates (2D viewport coordinates)
            selection_point = self.picker.GetSelectionPoint()
            
            # Print to console
            print(f"Picked point coordinates (3D): {pick_pos}")
            print(f"Selection point (2D pixels): {selection_point}")
            
            # Update marker sphere position
            self.marker_sphere.SetPosition(pick_pos)
            self.marker_sphere.GetProperty().VisibilityOn()
            
            # Update text mapper with coordinates
            text_str = f"({pick_pos[0]:.2f}, {pick_pos[1]:.2f}, {pick_pos[2]:.2f})"
            self.text_mapper.SetInput(text_str)
            
            # Update text actor position (convert 3D to 2D for display)
            self.text_actor.SetPosition(selection_point[0], selection_point[1])
            self.text_actor.GetProperty().VisibilityOn()
            
            # Force renderer update
            obj.GetRenderWindow().Render()


def glyphing():
    sphere_source = vtkSphereSource()
    
    cone_source = vtkConeSource()
    
    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(cone_source.GetOutputPort())
    glyph.SetInputConnection(sphere_source.GetOutputPort())
    glyph.SetScaleFactor(0.3)
    glyph.SetVectorModeToUseNormal()
    
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())
    
    actor = vtkActor()
    actor.SetMapper(mapper)
    
    ren1 = vtkRenderer()
    ren1.AddActor(actor)
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    
    renWin.Render()
    iren.Start()


# ============================================================================
# EXERCISE 2: Object Picking
# ============================================================================
def object_picking():
    sphere_source = vtkSphereSource()
    
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(sphere_source.GetOutputPort())
    
    actor = vtkActor()
    actor.SetMapper(mapper)
    
    marker_source = vtkSphereSource()
    
    marker_mapper = vtkPolyDataMapper()
    marker_mapper.SetInputConnection(marker_source.GetOutputPort())
    
    marker_actor = vtkActor()
    marker_actor.SetMapper(marker_mapper)
    marker_actor.VisibilityOff()
    
    text_mapper = vtkTextMapper()
    
    text_actor = vtkActor2D()
    text_actor.SetMapper(text_mapper)
    text_actor.VisibilityOff()
    
    myPicker = vtkPointPicker()
    
    mo1 = MyCallback(myPicker, text_mapper, text_actor, marker_actor)
    myPicker.AddObserver(vtkCommand.EndPickEvent, mo1)
    
    ren1 = vtkRenderer()
    ren1.AddActor(actor)
    ren1.AddActor(marker_actor)
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.SetPicker(myPicker)
    
    renWin.Render()
    iren.Start()


# ============================================================================
# EXERCISE 3: Display Coordinates on Renderer
# ============================================================================
def display_coordinates():
    sphere_source = vtkSphereSource()
    
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(sphere_source.GetOutputPort())
    
    actor = vtkActor()
    actor.SetMapper(mapper)
    
    marker_source = vtkSphereSource()
    
    marker_mapper = vtkPolyDataMapper()
    marker_mapper.SetInputConnection(marker_source.GetOutputPort())
    
    marker_actor = vtkActor()
    marker_actor.SetMapper(marker_mapper)
    marker_actor.VisibilityOff()
    
    textMapper = vtkTextMapper()
    textMapper.GetTextProperty().SetFontFamilyToCourier()
    textMapper.GetTextProperty().SetBold(1)
    textMapper.GetTextProperty().SetJustificationToCentered()
    
    textActor = vtkActor2D()
    textActor.SetMapper(textMapper)
    textActor.VisibilityOff()
    
    myPicker = vtkPointPicker()
    
    mo1 = MyCallback(myPicker, textMapper, textActor, marker_actor)
    myPicker.AddObserver(vtkCommand.EndPickEvent, mo1)
    
    ren1 = vtkRenderer()
    ren1.AddActor(actor)
    ren1.AddActor(marker_actor)
    ren1.AddActor(textActor)
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.SetPicker(myPicker)
    
    renWin.Render()
    iren.Start()


# ============================================================================
# EXERCISE 4: Unstructured Grid
# ============================================================================
def unstructured_grid():
    coords = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1]]
    aTetra = [0, 1, 2, 3]
    
    Ugrid = vtkUnstructuredGrid()
    points = vtkPoints()
    
    for i in range(len(coords)):
        points.InsertPoint(i, coords[i])
    
    for i in range(4):
        Ugrid.InsertNextCell(VTK_VERTEX, 1, [i])
    
    Ugrid.SetPoints(points)
    
    UGriMapper = vtkDataSetMapper()
    UGriMapper.SetInputData(Ugrid)
    
    UgridActor = vtkActor()
    UgridActor.SetMapper(UGriMapper)
    UgridActor.GetProperty().SetColor(1, 0, 0)
    UgridActor.GetProperty().SetPointSize(5)
    
    ren1 = vtkRenderer()
    ren1.AddActor(UgridActor)
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    
    renWin.Render()
    iren.Start()


# ============================================================================
# EXERCISE 5: Scalar Association to Vectors and Grids
# ============================================================================
def scalar_vector_association():
    coords = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1]]
    
    ugrid = vtkUnstructuredGrid()
    points = vtkPoints()
    
    for i in range(len(coords)):
        points.InsertPoint(i, coords[i])
    
    for i in range(4):
        ugrid.InsertNextCell(VTK_VERTEX, 1, [i])
    
    ugrid.SetPoints(points)
    
    vectors = vtkFloatArray()
    vectors.SetNumberOfComponents(3)
    
    vectors.InsertTuple3(0, 1, 0, 0)
    vectors.InsertTuple3(1, 0, 1, 0)
    vectors.InsertTuple3(2, 0, 0, 1)
    vectors.InsertTuple3(3, 1, 1, 1)
    
    ugrid.GetPointData().SetVectors(vectors)
    
    scalars = vtkFloatArray()
    scalars.SetNumberOfComponents(1)
    
    scalars.InsertTuple1(0, 0.1)
    scalars.InsertTuple1(1, 0.3)
    scalars.InsertTuple1(2, 0.5)
    scalars.InsertTuple1(3, 0.8)
    
    ugrid.GetPointData().SetScalars(scalars)
    
    coneSource = vtkConeSource()
    
    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputData(ugrid)
    glyph.SetVectorModeToUseVector()
    glyph.SetScaleModeToScaleByScalar()
    
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())
    
    actor = vtkActor()
    actor.SetMapper(mapper)
    
    ren1 = vtkRenderer()
    ren1.AddActor(actor)
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    
    renWin.Render()
    iren.Start()


# ============================================================================
# EXERCISE 6: HedgeHog Visualization
# ============================================================================
def hedgehog():
    coords = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1]]
    
    ugrid = vtkUnstructuredGrid()
    points = vtkPoints()
    
    for i in range(len(coords)):
        points.InsertPoint(i, coords[i])
    
    for i in range(4):
        ugrid.InsertNextCell(VTK_VERTEX, 1, [i])
    
    ugrid.SetPoints(points)
    
    vectors = vtkFloatArray()
    vectors.SetNumberOfComponents(3)
    
    vectors.InsertTuple3(0, 1, 0, 0)
    vectors.InsertTuple3(1, 0, 1, 0)
    vectors.InsertTuple3(2, 0, 0, 1)
    vectors.InsertTuple3(3, 1, 1, 1)
    
    ugrid.GetPointData().SetVectors(vectors)
    
    hedgehog = vtkHedgeHog()
    hedgehog.SetInputData(ugrid)
    
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(hedgehog.GetOutputPort())
    
    actor = vtkActor()
    actor.SetMapper(mapper)
    
    ren1 = vtkRenderer()
    ren1.AddActor(actor)
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    
    renWin.Render()
    iren.Start()


# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    glyphing()
    
    # object_picking()
    
    # display_coordinates()
    
    # unstructured_grid()
    
    # scalar_vector_association()
    
    # hedgehog()
