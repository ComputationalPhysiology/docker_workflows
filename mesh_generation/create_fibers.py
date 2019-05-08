import os
import sys

if sys.version < '3.6':
    print('This script is only supported for python version 3.6 and above')
    sys.exit()

import h5py
import dolfin

try:
    import ldrb
except ImportError:
    print(('ldrb not installed - '
           'pip install git+https://github.com/ComputationalPhysiology/ldrb.git'))
    sys.exit()

try:
    from pulse import HeartGeometry
except ImportError:
    print(('pulse is not installed  - '
          'pip install git+https://github.com/ComputationalPhysiology/pulse.git'))


def check_h5group(h5name, h5group, delete=False, comm=dolfin.mpi_comm_world()):

    h5group_in_h5file = False
    if not os.path.isfile(h5name):
        return False

    filemode = "a" if delete else "r"
    if not os.access(h5name, os.W_OK):
        filemode = "r"
        if delete:
            print(("You do not have write access to file "
                   "{}").format(h5name))
            delete = False

    with h5py.File(h5name, filemode) as h5file:
        if h5group in h5file:
            h5group_in_h5file = True
            if delete:
                if dolfin.MPI.rank(comm) == 0:
                    print(("Deleting existing group: "
                           "'{}'").format(h5group))
                    del h5file[h5group]

    return h5group_in_h5file


def save_fields(fields, h5name):

    comm = dolfin.mpi_comm_world()
    fgroup = "microstructure"
    try:
        check_h5group(h5name, fgroup, delete=True, comm=comm)
    except RuntimeError:
        pass

    with dolfin.HDF5File(comm, h5name, 'a') as h5file:
        names = []
        for field in fields:
            label = field.label() \
                    if field.label().rfind('a Function') == -1 else ""
            name = "_".join(filter(None, [str(field), label]))
            fsubgroup = "{}/{}".format(fgroup, name)
            h5file.write(field, fsubgroup)
            h5file.attributes(fsubgroup)['name'] = field.name()
            names.append(name)

        elm = field.function_space().ufl_element()
        family, degree = elm.family(), elm.degree()
        fspace = '{}_{}'.format(family, degree)
        h5file.attributes(fgroup)['space'] = fspace
        h5file.attributes(fgroup)['names'] = ":".join(names)


# Decide on the angles you want to use
def create_fiber_fields(mesh, markers, ffun, angles=None,
                        fiber_space='Quadrature_2'):

    if angles is None:
        angles = dict(alpha_endo_lv=60,  # Fiber angle on the endocardium
                      alpha_epi_lv=-60,  # Fiber angle on the epicardium
                      beta_endo_lv=0,    # Sheet angle on the endocardium
                      beta_epi_lv=0)     # Sheet angle on the epicardium

    # Choose space for the fiber fields
    # This is a string on the form {family}_{degree}
    # fiber_space = 'Quadrature_2'
    # At all nodes
    # fiber_space = 'Lagrange_1'
    m = {
        'lv': markers.get('ENDO')[0],
        'epi': markers.get('EPI')[0],
        'base': markers.get('BASE')[0],
    }
    # Compute the microstructure
    fiber, sheet, sheet_normal = ldrb.dolfin_ldrb(mesh=mesh,
                                                  fiber_space=fiber_space,
                                                  ffun=ffun,
                                                  markers=m,
                                                  **angles)
    fiber.rename("fiber", "microstructure")
    sheet.rename("sheet", "microstructure")
    sheet_normal.rename("sheet_normal", "microstructure")
    ldrb.fiber_to_xdmf(fiber, 'lv_fiber')
    return [fiber, sheet, sheet_normal]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a input filename')
        sys.exit()
    infile = sys.argv[1]
    if not os.path.isfile(infile):
        print('File {} does not exist'.format(infile))
        sys.exit()

    geo = HeartGeometry.from_file(infile)
    dolfin.File('facets.pvd') << geo.ffun
    fields = create_fiber_fields(geo.mesh, geo.markers, geo.ffun)
    save_fields(fields, infile)
