vtk_module(vtkPVServerManagerRendering
  GROUPS
    ParaViewRendering
  DEPENDS
    vtkPVServerManagerCore
    vtkPVServerImplementationRendering
  TEST_LABELS
    PARAVIEW
)
