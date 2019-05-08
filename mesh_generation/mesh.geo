// meshing options
Mesh.CharacteristicLengthFromCurvature = 1;
Mesh.Lloyd = 1;
Geometry.HideCompounds = 0;
Mesh.CharacteristicLengthMin = 1.0;
Mesh.CharacteristicLengthMax = 1.0;
Mesh.ScalingFactor = 10.0;
Mesh.Optimize = 1;
Mesh.OptimizeNetgen = 1;
Mesh.RemeshParametrization = 7;  // (0=harmonic_circle, 1=conformal_spectral, 2=rbf, 3=harmonic_plane, 4=convex_circle, 5=convex_plane, 6=harmonic square, 7=conformal_fe) (Default=4)
Mesh.SurfaceFaces = 1;
Mesh.Algorithm    = 6; // (1=MeshAdapt, 2=Automatic, 5=Delaunay, 6=Frontal, 7=bamg, 8=delquad) (Default=2)
Mesh.Algorithm3D    = 4; // (1=Delaunay, 4=Frontal, 5=Frontal Delaunay, 6=Frontal Hex, 7=MMG3D, 9=R-tree) (Default=1)
Mesh.Recombine3DAll = 0;

// load the surfaces
Merge "endo_lv_0.ply";
Merge "epi_lv_0.ply";

CreateTopology;

ll[] = Line "*";
L_LV_base = newl; Compound Line(L_LV_base) = ll[1];
L_epi_base = newl; Compound Line(L_epi_base) = ll[0];
Physical Line("ENDORING") = { L_LV_base };
Physical Line("EPIRING") = { L_epi_base };

ss[] = Surface "*";
S_LV = news; Compound Surface(S_LV) = ss[0];
S_epi = news; Compound Surface(S_epi) = ss[1];
Physical Surface("ENDO") = { S_LV };
Physical Surface("EPI") = { S_epi };

LL_base = newll; 
Line Loop(LL_base) = { L_LV_base, L_epi_base };
S_base = news; Plane Surface(S_base) = { LL_base };
Physical Surface("BASE") = { S_base };

SL_wall = newsl; 
Surface Loop(SL_wall) = { S_LV, S_epi, S_base };
V_wall = newv; Volume(V_wall) = { SL_wall };
Physical Volume("WALL") = { V_wall };
Coherence;
