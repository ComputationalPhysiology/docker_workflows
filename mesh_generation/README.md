# Meshing pipeline

Build docker image
```
docker build -t mesh .
```
Run container (one level up `cd ..`)
```
docker run -ti --name mesh -e "TERM=xterm-256color" -w /home/fenics/shared -v $(pwd):/home/fenics/shared mesh
```


Go to folder called `mesh`
Edit `mesh.geo` - change surfaces (epi + endo)
Create mesh using gmsh

```
gmsh -3 mesh.geo
```
This will create a new file called `mesh.msh`

Convert to dolfin

```
gmsh2dolfin mesh.msh
```
This will create a new file called `mesh.h5`

Convert `mesh.h5`
```
python save_geometry.py mesh.h5 new_mesh.h5
```
Now create fiber fields using the script `create_fiber.py`
```
python create_fibers.py new_mesh.h5
```

exit container
```
exit
```
