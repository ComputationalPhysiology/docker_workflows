import os
import sys
import dolfin
import h5py
from fenicshotools import load_geometry


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


def save_geometry_to_h5(mesh, h5name, markers, h5group="",
                        overwrite_file=False, overwrite_group=True):
    """
    Save geometry and other geometrical functions to a HDF file.

    Parameters
    ----------
    mesh : :class:`dolfin.mesh`
        The mesh
    h5name : str
        Path to the file
    h5group : str
        Folder within the file. Default is "" which means in
        the top folder.
    markers : dict
        A dictionary with markers. See `get_markers`.
    overwrite_file : bool
        If true, and the file exists, the file will be overwritten (default: False)
    overwrite_group : bool
        If true and h5group exist, the group will be overwritten.

    """

    print("\nSave mesh to h5")
    assert isinstance(mesh, dolfin.Mesh)
    comm = mesh.mpi_comm()
    file_mode = "a" if os.path.isfile(h5name) and not overwrite_file else "w"

    # IF we should append the file but overwrite the group we need to
    # check that the group does not exist. If so we need to open it in
    # h5py and delete it.
    if file_mode == "a" and overwrite_group and h5group != "":
        check_h5group(h5name, h5group, delete=True, comm=comm)

    with dolfin.HDF5File(comm, h5name, file_mode) as h5file:

        # Save mesh
        ggroup = '{}/geometry'.format(h5group)

        mgroup = '{}/mesh'.format(ggroup)

        h5file.write(mesh, mgroup)

        for dim in range(4):

            if markers[dim][0] is not None:
                mf = dolfin.MeshFunction("size_t", mesh, markers[dim][0])
            else:
                mf = dolfin.MeshFunction("size_t", mesh, dim, mesh.domains())
            save_mf = dolfin.MPI.max(comm, len(set(mf.array()))) > 1

            if save_mf:
                dgroup = '{}/mesh/meshfunction_{}'.format(ggroup, dim)
                h5file.write(mf, dgroup)

        if markers is not None:
            # Save the boundary markers
            for dim, v in markers.items():
                if v is None:
                    continue
                if v[-1] is None:
                    continue
                for marker, name in v[-1].items():
                    for key_str in ["domain", "meshfunction"]:

                        dgroup = '{}/mesh/{}_{}'.format(ggroup, key_str, dim)

                        if h5file.has_dataset(dgroup):
                            aname = 'marker_name_{}'.format(name)
                            h5file.attributes(dgroup)[aname] = marker
    print("Geometry saved to {}".format(h5name))


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Please provide a input and output filename')
        sys.exit()
    infile = sys.argv[1]
    if not os.path.isfile(infile):
        print('File {} does not exist'.format(infile))
        sys.exit()
    outfile = sys.argv[2]

    mesh, phi, markers = load_geometry(dolfin.mpi_comm_world(), infile)

    save_geometry_to_h5(mesh, outfile, markers)
