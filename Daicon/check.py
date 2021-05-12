import vtk
from vtk.util.numpy_support import vtk_to_numpy, numpy_to_vtk
import numpy as np

reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName(r'\\192.168.0.113\Imagoworks\Data\confident\Mesh\IntraoralScan\DAEYOU\train\7061\mn.vtp')
reader.Update()
polydata=reader.GetOutput()
label_np = vtk_to_numpy(polydata.GetPointData().GetScalars())

print(np.unique(label_np))