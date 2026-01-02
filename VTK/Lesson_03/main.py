"""
Lesson 3 - Callbacks, Glyphing and Picking
"""

from vtkmodules.vtkFiltersSources import vtkConeSource, vtkSphereSource
from vtkmodules.vtkFiltersCore import vtkGlyph3D
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2


def glyphing():
    coneSource = vtkConeSource()
    coneSource.SetResolution(16)
    
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(50)
    sphereSource.SetPhiResolution(50)
    
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
    renderer.AddActor(glyphActor)
    renderer.SetBackground(0.1, 0.2, 0.4)
    
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(800, 600)
    renderWindow.SetWindowName("Lesson 3 - Glyphing")
    
    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    
    renderWindow.Render()
    interactor.Start()


if __name__ == "__main__":
    glyphing()
