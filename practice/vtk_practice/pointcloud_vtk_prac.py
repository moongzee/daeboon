import glob
import vtk
from vtk.util.numpy_support import vtk_to_numpy, numpy_to_vtk
import numpy as np
import pandas as pd 



def pointcloudToActor(pointcloud):

    vtk_pc = numpy_to_vtk(pointcloud)

    points = vtk.vtkPoints()
    points.SetData(vtk_pc)

    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)


    mapper = vtk.vtkOpenGLSphereMapper()
    mapper.SetInputData(polydata)
    # mapper.SetRadius(0.01)

    actor=vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor



if __name__ == "__main__":

    
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.SetSize(1000, 1000)
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())



    Daeyou=np.load(r'C:\Users\imagoworks-moongzeee\test\numpy_file\Daeyou_vector.npy')
    Daeyou_cut=np.load(r'C:\Users\imagoworks-moongzeee\test\numpy_file\Daeyou_cut_vector.npy')
    Ddh=np.load(r'C:\Users\imagoworks-moongzeee\test\numpy_file\Ddh_vector.npy')
    Ddh_cut=np.load(r'C:\Users\imagoworks-moongzeee\test\numpy_file\Ddh_cut_vector.npy')

    # Daeyou[:0] = np.absolute(Daeyou[:0])
    # Daeyou_cut[:0] = np.absolute(Daeyou_cut[:0])
    # Ddh = np.absolute(Ddh)
    # Ddh_cut = np.absolute(Ddh_cut)


    # #daeyou actor
    # actor1 = pointcloudToActor(Daeyou)
    # actor1.GetProperty().SetColor(15, 77, 1)
    # ren.AddActor(actor1)
    


    # #daeyou_cut actor
    # actor2 = pointcloudToActor(Daeyou_cut)
    # actor2.GetProperty().SetColor(2, 0, 0)
    # ren.AddActor(actor2)
    

    # #ddh actor
    # actor3 = pointcloudToActor(Ddh)
    # actor3.GetProperty().SetColor(55, 11, 0)
    # ren.AddActor(actor3)

    #ddh_cut actor
    actor4 = pointcloudToActor(Ddh_cut)
    actor4.GetProperty().SetColor(88, 30, 44)
    ren.AddActor(actor4)



    renWin.Render()
    iren.Initialize()
    iren.Start()