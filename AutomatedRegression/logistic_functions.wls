getk23[list_]:=
Module[{fccase,ciacase,f2case,f3case},
fccase = RegFunction[ 0.293708, -0.248768, 15.105, 0,FC[t]];
ciacase = RegFunction[ 0.227484, -0.652642, 71.4237, 0,CIA[t]];
f2case = RegFunction[ 0.226644, -0.130635, 37.073, 0,F2[t]];
f3case = RegFunction[ 0.226655, -0.00362872, 674.652, 0,F3[t]];
Switch[list,FCL,fccase,CIAL,ciacase,F2L,f2case,F3L,f3case]
]
getkO2[list_]:=
Module[{fscase},
fscase = RegFunction[ 95.3616, -0.0134783, 258.284, 0,FS[t]];
Switch[list,FSL,fscase]
]
getkCIA[list_]:=
Module[{o2case,fmcase,mpcase},
o2case = RegFunction[ 4.661, -8.87757, 1.41475, 0.418826,O2[t]];
fmcase = RegFunction[ 5.50768, 0.0387998, 0.991932, 0.41756,FM[t]];
mpcase = RegFunction[ 3.006, 0.0690787, 3.09565, 0.42,MP[t]];
Switch[list,O2L,o2case,FML,fmcase,MPL,mpcase]
]
getkCYT[list_]:=
Module[{f2case,ciacase,f3case,fccase},
f2case = RegFunction[ 16.6101, 0.159447, 7.90727, 2.62995,F2[t]];
ciacase = RegFunction[ 1557.4, 0.744197, 59.1271, 2.62967,CIA[t]];
f3case = RegFunction[ 5.00448, 0.00537466, 0.991933, 2.62995,F3[t]];
fccase = RegFunction[ 2.15854, 1.00162, 8.74028, 2.62992,FC[t]];
Switch[list,F2L,f2case,CIAL,ciacase,F3L,f3case,FCL,fccase]
]
getkMIT[list_]:=
Module[{fscase},
fscase = RegFunction[ 168.632, 0.022031, 0.991933, 0.538779,FS[t]];
Switch[list,FSL,fscase]
]
getkMP[list_]:=
Module[{o2case,mpcase,fmcase},
o2case = RegFunction[ 4.1828, 8.89003, 0.130172, 0,O2[t]];
mpcase = RegFunction[ 0.176593, -0.0142367, 376.877, 0,MP[t]];
fmcase = RegFunction[ 0.931282, -0.0587368, 224.854, 0.00105854,FM[t]];
Switch[list,O2L,o2case,MPL,mpcase,FML,fmcase]
]
getkVAC[list_]:=
Module[{f2case,ciacase,f3case,fccase},
f2case = RegFunction[ 2.99975, -0.076787, 56.8973, 0,F2[t]];
ciacase = RegFunction[ 3.67913, -0.377767, 76.0689, 0,CIA[t]];
f3case = RegFunction[ 3.04175, -0.00213037, 1396.83, 0,F3[t]];
fccase = RegFunction[ 2.88787, -0.679725, 14.0134, 0.160357,FC[t]];
Switch[list,F2L,f2case,CIAL,ciacase,F3L,f3case,FCL,fccase]
]
