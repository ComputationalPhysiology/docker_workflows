# Gotran generated code for the  "tentusscher_2004_mcell" model
from __future__ import division

def init_state_values(**values):
    """
    Initialize state values
    """
    # Imports
    import numpy as np
    from modelparameters.utils import Range

    # Init values
    # Xr1=0, Xr2=1, Xs=0, m=0, h=0.75, j=0.75, d=0, f=1, fCa=1, s=1, r=0,
    # g=1, Ca_i=0.0002, Ca_SR=0.2, Na_i=11.6, V=-86.2, K_i=138.3
    init_values = np.array([0, 1, 0, 0, 0.75, 0.75, 0, 1, 1, 1, 0, 1, 0.0002,\
        0.2, 11.6, -86.2, 138.3], dtype=np.float_)

    # State indices and limit checker
    state_ind = dict([("Xr1",(0, Range())), ("Xr2",(1, Range())), ("Xs",(2,\
        Range())), ("m",(3, Range())), ("h",(4, Range())), ("j",(5,\
        Range())), ("d",(6, Range())), ("f",(7, Range())), ("fCa",(8,\
        Range())), ("s",(9, Range())), ("r",(10, Range())), ("g",(11,\
        Range())), ("Ca_i",(12, Range())), ("Ca_SR",(13, Range())),\
        ("Na_i",(14, Range())), ("V",(15, Range())), ("K_i",(16, Range()))])

    for state_name, value in values.items():
        if state_name not in state_ind:
            raise ValueError("{0} is not a state.".format(state_name))
        ind, range = state_ind[state_name]
        if value not in range:
            raise ValueError("While setting '{0}' {1}".format(state_name,\
                range.format_not_in(value)))

        # Assign value
        init_values[ind] = value

    return init_values

def init_parameter_values(**values):
    """
    Initialize parameter values
    """
    # Imports
    import numpy as np
    from modelparameters.utils import Range

    # Param values
    # P_kna=0.03, g_K1=5.405, g_Kr=0.096, g_Ks=0.062, g_Na=14.838,
    # g_bna=0.00029, g_CaL=0.000175, g_bca=0.000592, g_to=0.294,
    # K_mNa=40.0, K_mk=1.0, P_NaK=1.362, K_NaCa=1000.0, K_sat=0.1,
    # Km_Ca=1.38, Km_Nai=87.5, alpha=2.5, gamma=0.35, K_pCa=0.0005,
    # g_pCa=0.825, g_pK=0.0146, Buf_c=0.15, Buf_sr=10.0, Ca_o=2.0,
    # K_buf_c=0.001, K_buf_sr=0.3, K_up=0.00025, V_leak=8e-05,
    # V_sr=0.001094, Vmax_up=0.000425, a_rel=0.016464, b_rel=0.25,
    # c_rel=0.008232, tau_g=2.0, Na_o=140.0, Cm=0.185, F=96485.3415,
    # R=8314.472, T=310.0, V_c=0.016404, stim_amplitude=52.0,
    # stim_duration=1.0, stim_period=1000.0, stim_start=10.0, K_o=5.4
    init_values = np.array([0.03, 5.405, 0.096, 0.062, 14.838, 0.00029,\
        0.000175, 0.000592, 0.294, 40.0, 1.0, 1.362, 1000.0, 0.1, 1.38, 87.5,\
        2.5, 0.35, 0.0005, 0.825, 0.0146, 0.15, 10.0, 2.0, 0.001, 0.3,\
        0.00025, 8e-05, 0.001094, 0.000425, 0.016464, 0.25, 0.008232, 2.0,\
        140.0, 0.185, 96485.3415, 8314.472, 310.0, 0.016404, 52.0, 1.0,\
        1000.0, 10.0, 5.4], dtype=np.float_)

    # Parameter indices and limit checker
    param_ind = dict([("P_kna", (0, Range())), ("g_K1", (1, Range())),\
        ("g_Kr", (2, Range())), ("g_Ks", (3, Range())), ("g_Na", (4,\
        Range())), ("g_bna", (5, Range())), ("g_CaL", (6, Range())),\
        ("g_bca", (7, Range())), ("g_to", (8, Range())), ("K_mNa", (9,\
        Range())), ("K_mk", (10, Range())), ("P_NaK", (11, Range())),\
        ("K_NaCa", (12, Range())), ("K_sat", (13, Range())), ("Km_Ca", (14,\
        Range())), ("Km_Nai", (15, Range())), ("alpha", (16, Range())),\
        ("gamma", (17, Range())), ("K_pCa", (18, Range())), ("g_pCa", (19,\
        Range())), ("g_pK", (20, Range())), ("Buf_c", (21, Range())),\
        ("Buf_sr", (22, Range())), ("Ca_o", (23, Range())), ("K_buf_c", (24,\
        Range())), ("K_buf_sr", (25, Range())), ("K_up", (26, Range())),\
        ("V_leak", (27, Range())), ("V_sr", (28, Range())), ("Vmax_up", (29,\
        Range())), ("a_rel", (30, Range())), ("b_rel", (31, Range())),\
        ("c_rel", (32, Range())), ("tau_g", (33, Range())), ("Na_o", (34,\
        Range())), ("Cm", (35, Range())), ("F", (36, Range())), ("R", (37,\
        Range())), ("T", (38, Range())), ("V_c", (39, Range())),\
        ("stim_amplitude", (40, Range())), ("stim_duration", (41, Range())),\
        ("stim_period", (42, Range())), ("stim_start", (43, Range())),\
        ("K_o", (44, Range()))])

    for param_name, value in values.items():
        if param_name not in param_ind:
            raise ValueError("{0} is not a parameter.".format(param_name))
        ind, range = param_ind[param_name]
        if value not in range:
            raise ValueError("While setting '{0}' {1}".format(param_name,\
                range.format_not_in(value)))

        # Assign value
        init_values[ind] = value

    return init_values

def state_indices(*states):
    """
    State indices
    """
    state_inds = dict([("Xr1", 0), ("Xr2", 1), ("Xs", 2), ("m", 3), ("h", 4),\
        ("j", 5), ("d", 6), ("f", 7), ("fCa", 8), ("s", 9), ("r", 10), ("g",\
        11), ("Ca_i", 12), ("Ca_SR", 13), ("Na_i", 14), ("V", 15), ("K_i",\
        16)])

    indices = []
    for state in states:
        if state not in state_inds:
            raise ValueError("Unknown state: '{0}'".format(state))
        indices.append(state_inds[state])
    if len(indices)>1:
        return indices
    else:
        return indices[0]

def parameter_indices(*params):
    """
    Parameter indices
    """
    param_inds = dict([("P_kna", 0), ("g_K1", 1), ("g_Kr", 2), ("g_Ks", 3),\
        ("g_Na", 4), ("g_bna", 5), ("g_CaL", 6), ("g_bca", 7), ("g_to", 8),\
        ("K_mNa", 9), ("K_mk", 10), ("P_NaK", 11), ("K_NaCa", 12), ("K_sat",\
        13), ("Km_Ca", 14), ("Km_Nai", 15), ("alpha", 16), ("gamma", 17),\
        ("K_pCa", 18), ("g_pCa", 19), ("g_pK", 20), ("Buf_c", 21), ("Buf_sr",\
        22), ("Ca_o", 23), ("K_buf_c", 24), ("K_buf_sr", 25), ("K_up", 26),\
        ("V_leak", 27), ("V_sr", 28), ("Vmax_up", 29), ("a_rel", 30),\
        ("b_rel", 31), ("c_rel", 32), ("tau_g", 33), ("Na_o", 34), ("Cm",\
        35), ("F", 36), ("R", 37), ("T", 38), ("V_c", 39), ("stim_amplitude",\
        40), ("stim_duration", 41), ("stim_period", 42), ("stim_start", 43),\
        ("K_o", 44)])

    indices = []
    for param in params:
        if param not in param_inds:
            raise ValueError("Unknown param: '{0}'".format(param))
        indices.append(param_inds[param])
    if len(indices)>1:
        return indices
    else:
        return indices[0]

def monitor_indices(*monitored):
    """
    Monitor indices
    """
    monitor_inds = dict([("E_Na", 0), ("E_K", 1), ("E_Ks", 2), ("E_Ca", 3),\
        ("alpha_K1", 4), ("beta_K1", 5), ("xK1_inf", 6), ("i_K1", 7),\
        ("i_Kr", 8), ("xr1_inf", 9), ("alpha_xr1", 10), ("beta_xr1", 11),\
        ("tau_xr1", 12), ("xr2_inf", 13), ("alpha_xr2", 14), ("beta_xr2",\
        15), ("tau_xr2", 16), ("i_Ks", 17), ("xs_inf", 18), ("alpha_xs", 19),\
        ("beta_xs", 20), ("tau_xs", 21), ("i_Na", 22), ("m_inf", 23),\
        ("alpha_m", 24), ("beta_m", 25), ("tau_m", 26), ("h_inf", 27),\
        ("alpha_h", 28), ("beta_h", 29), ("tau_h", 30), ("j_inf", 31),\
        ("alpha_j", 32), ("beta_j", 33), ("tau_j", 34), ("i_b_Na", 35),\
        ("i_CaL", 36), ("d_inf", 37), ("alpha_d", 38), ("beta_d", 39),\
        ("gamma_d", 40), ("tau_d", 41), ("f_inf", 42), ("tau_f", 43),\
        ("alpha_fCa", 44), ("beta_fCa", 45), ("gama_fCa", 46), ("fCa_inf",\
        47), ("tau_fCa", 48), ("d_fCa", 49), ("i_b_Ca", 50), ("i_to", 51),\
        ("s_inf", 52), ("tau_s", 53), ("r_inf", 54), ("tau_r", 55), ("i_NaK",\
        56), ("i_NaCa", 57), ("i_p_Ca", 58), ("i_p_K", 59), ("i_rel", 60),\
        ("i_up", 61), ("i_leak", 62), ("g_inf", 63), ("d_g", 64),\
        ("Ca_i_bufc", 65), ("Ca_sr_bufsr", 66), ("i_Stim", 67), ("dXr1_dt",\
        68), ("dXr2_dt", 69), ("dXs_dt", 70), ("dm_dt", 71), ("dh_dt", 72),\
        ("dj_dt", 73), ("dd_dt", 74), ("df_dt", 75), ("dfCa_dt", 76),\
        ("ds_dt", 77), ("dr_dt", 78), ("dg_dt", 79), ("dCa_i_dt", 80),\
        ("dCa_SR_dt", 81), ("dNa_i_dt", 82), ("dV_dt", 83), ("dK_i_dt", 84)])

    indices = []
    for monitor in monitored:
        if monitor not in monitor_inds:
            raise ValueError("Unknown monitored: '{0}'".format(monitor))
        indices.append(monitor_inds[monitor])
    if len(indices)>1:
        return indices
    else:
        return indices[0]

def rhs(states, t, parameters, values=None):
    """
    Compute the right hand side of the tentusscher_2004_mcell ODE
    """
    # Imports
    import numpy as np
    import math

    # Assign states
    assert(len(states) == 17)
    Xr1, Xr2, Xs, m, h, j, d, f, fCa, s, r, g, Ca_i, Ca_SR, Na_i, V, K_i =\
        states

    # Assign parameters
    assert(len(parameters) == 45)
    P_kna, g_K1, g_Kr, g_Ks, g_Na, g_bna, g_CaL, g_bca, g_to, K_mNa, K_mk,\
        P_NaK, K_NaCa, K_sat, Km_Ca, Km_Nai, alpha, gamma, K_pCa, g_pCa,\
        g_pK, Buf_c, Buf_sr, Ca_o, K_buf_c, K_buf_sr, K_up, V_leak, V_sr,\
        Vmax_up, a_rel, b_rel, c_rel, tau_g, Na_o, Cm, F, R, T, V_c,\
        stim_amplitude, stim_duration, stim_period, stim_start, K_o =\
        parameters

    # Init return args
    if values is None:
        values = np.zeros((17,), dtype=np.float_)
    else:
        assert isinstance(values, np.ndarray) and values.shape == (17,)

    # Expressions for the Reversal potentials component
    E_Na = R*T*math.log(Na_o/Na_i)/F
    E_K = R*T*math.log(K_o/K_i)/F
    E_Ks = R*T*math.log((K_o + Na_o*P_kna)/(P_kna*Na_i + K_i))/F
    E_Ca = 0.5*R*T*math.log(Ca_o/Ca_i)/F

    # Expressions for the Inward rectifier potassium current component
    alpha_K1 = 0.1/(1.0 + 6.14421235332821e-06*math.exp(0.06*V - 0.06*E_K))
    beta_K1 = (0.36787944117144233*math.exp(0.1*V - 0.1*E_K) +\
        3.0606040200802673*math.exp(0.0002*V - 0.0002*E_K))/(1.0 +\
        math.exp(0.5*E_K - 0.5*V))
    xK1_inf = alpha_K1/(alpha_K1 + beta_K1)
    i_K1 = 0.4303314829119352*g_K1*math.sqrt(K_o)*(-E_K + V)*xK1_inf

    # Expressions for the Rapid time dependent potassium current component
    i_Kr = 0.4303314829119352*g_Kr*math.sqrt(K_o)*(-E_K + V)*Xr1*Xr2

    # Expressions for the Xr1 gate component
    xr1_inf = 1.0/(1.0 + 0.02437284407327961*math.exp(-0.14285714285714285*V))
    alpha_xr1 = 450.0/(1.0 + 0.011108996538242306*math.exp(-0.1*V))
    beta_xr1 = 6.0/(1.0 + 13.581324522578193*math.exp(0.08695652173913043*V))
    tau_xr1 = 1.0*alpha_xr1*beta_xr1
    values[0] = (-Xr1 + xr1_inf)/tau_xr1

    # Expressions for the Xr2 gate component
    xr2_inf = 1.0/(1.0 + 39.12128399815321*math.exp(0.041666666666666664*V))
    alpha_xr2 = 3.0/(1.0 + 0.049787068367863944*math.exp(-0.05*V))
    beta_xr2 = 1.12/(1.0 + 0.049787068367863944*math.exp(0.05*V))
    tau_xr2 = 1.0*alpha_xr2*beta_xr2
    values[1] = (-Xr2 + xr2_inf)/tau_xr2

    # Expressions for the Slow time dependent potassium current component
    i_Ks = g_Ks*math.pow(Xs, 2.0)*(-E_Ks + V)

    # Expressions for the Xs gate component
    xs_inf = 1.0/(1.0 + 0.6996725373751304*math.exp(-0.07142857142857142*V))
    alpha_xs = 1100.0/math.sqrt(1.0 +\
        0.18887560283756186*math.exp(-0.16666666666666666*V))
    beta_xs = 1.0/(1.0 + 0.049787068367863944*math.exp(0.05*V))
    tau_xs = 1.0*alpha_xs*beta_xs
    values[2] = (-Xs + xs_inf)/tau_xs

    # Expressions for the Fast sodium current component
    i_Na = g_Na*math.pow(m, 3.0)*(-E_Na + V)*h*j

    # Expressions for the m gate component
    m_inf = 1.0*math.pow(1.0 +\
        0.0018422115811651339*math.exp(-0.1107419712070875*V), -2.0)
    alpha_m = 1.0/(1.0 + 6.14421235332821e-06*math.exp(-0.2*V))
    beta_m = 0.1/(1.0 + 1096.6331584284585*math.exp(0.2*V)) + 0.1/(1.0 +\
        0.7788007830714049*math.exp(0.005*V))
    tau_m = 1.0*alpha_m*beta_m
    values[3] = (-m + m_inf)/tau_m

    # Expressions for the h gate component
    h_inf = 1.0*math.pow(1.0 +\
        15212.593285654404*math.exp(0.13458950201884254*V), -2.0)
    alpha_h = (4.4312679295805147e-07*math.exp(-0.14705882352941177*V) if V <\
        -40.0 else 0)
    beta_h = (310000.0*math.exp(0.3485*V) + 2.7*math.exp(0.079*V) if V <\
        -40.0 else 0.77/(0.13 +\
        0.049758141083938695*math.exp(-0.0900900900900901*V)))
    tau_h = 1.0/(alpha_h + beta_h)
    values[4] = (-h + h_inf)/tau_h

    # Expressions for the j gate component
    j_inf = 1.0*math.pow(1.0 +\
        15212.593285654404*math.exp(0.13458950201884254*V), -2.0)
    alpha_j = (1.0*(37.78 + V)*(-25428.0*math.exp(0.2444*V) -\
        6.948e-06*math.exp(-0.04391*V))/(1.0 +\
        50262745825.95399*math.exp(0.311*V)) if V < -40.0 else 0)
    beta_j = (0.02424*math.exp(-0.01052*V)/(1.0 +\
        0.003960868339904256*math.exp(-0.1378*V)) if V < -40.0 else\
        0.6*math.exp(0.057*V)/(1.0 + 0.040762203978366204*math.exp(-0.1*V)))
    tau_j = 1.0/(alpha_j + beta_j)
    values[5] = (-j + j_inf)/tau_j

    # Expressions for the Sodium background current component
    i_b_Na = g_bna*(-E_Na + V)

    # Expressions for the L_type Ca current component
    i_CaL = 4.0*g_CaL*math.pow(F, 2.0)*(-0.341*Ca_o +\
        Ca_i*math.exp(2.0*F*V/(R*T)))*V*d*f*fCa/(R*T*(-1.0 +\
        math.exp(2.0*F*V/(R*T))))

    # Expressions for the d gate component
    d_inf = 1.0/(1.0 + 0.513417119032592*math.exp(-0.13333333333333333*V))
    alpha_d = 0.25 + 1.4/(1.0 +\
        0.0677244716592409*math.exp(-0.07692307692307693*V))
    beta_d = 1.4/(1.0 + 2.718281828459045*math.exp(0.2*V))
    gamma_d = 1.0/(1.0 + 12.182493960703473*math.exp(-0.05*V))
    tau_d = 1.0*alpha_d*beta_d + gamma_d
    values[6] = (-d + d_inf)/tau_d

    # Expressions for the f gate component
    f_inf = 1.0/(1.0 + 17.411708063327644*math.exp(0.14285714285714285*V))
    tau_f = 80.0 + 165.0/(1.0 + 12.182493960703473*math.exp(-0.1*V)) +\
        1125.0*math.exp(-0.004166666666666667*math.pow(27.0 + V, 2.0))
    values[7] = (-f + f_inf)/tau_f

    # Expressions for the FCa gate component
    alpha_fCa = 1.0/(1.0 + 8.03402376701711e+27*math.pow(Ca_i, 8.0))
    beta_fCa = 0.1/(1.0 + 0.006737946999085467*math.exp(10000.0*Ca_i))
    gama_fCa = 0.2/(1.0 + 0.391605626676799*math.exp(1250.0*Ca_i))
    fCa_inf = 0.15753424657534246 + 0.684931506849315*alpha_fCa +\
        0.684931506849315*beta_fCa + 0.684931506849315*gama_fCa
    tau_fCa = 2.0
    d_fCa = (-fCa + fCa_inf)/tau_fCa
    values[8] = (0 if fCa_inf > fCa and V > -60.0 else d_fCa)

    # Expressions for the Calcium background current component
    i_b_Ca = g_bca*(-E_Ca + V)

    # Expressions for the Transient outward current component
    i_to = g_to*(-E_K + V)*r*s

    # Expressions for the s gate component
    s_inf = 1.0/(1.0 + 54.598150033144236*math.exp(0.2*V))
    tau_s = 3.0 + 5.0/(1.0 + 0.01831563888873418*math.exp(0.2*V)) +\
        85.0*math.exp(-0.003125*math.pow(45.0 + V, 2.0))
    values[9] = (-s + s_inf)/tau_s

    # Expressions for the r gate component
    r_inf = 1.0/(1.0 + 28.031624894526125*math.exp(-0.16666666666666666*V))
    tau_r = 0.8 + 9.5*math.exp(-0.0005555555555555556*math.pow(40.0 + V, 2.0))
    values[10] = (-r + r_inf)/tau_r

    # Expressions for the Sodium potassium pump current component
    i_NaK = K_o*P_NaK*Na_i/((K_mNa + Na_i)*(K_mk + K_o)*(1.0 +\
        0.0353*math.exp(-F*V/(R*T)) + 0.1245*math.exp(-0.1*F*V/(R*T))))

    # Expressions for the Sodium calcium exchanger current component
    i_NaCa = K_NaCa*(Ca_o*math.pow(Na_i, 3.0)*math.exp(F*gamma*V/(R*T)) -\
        alpha*math.pow(Na_o, 3.0)*Ca_i*math.exp(F*(-1.0 +\
        gamma)*V/(R*T)))/((1.0 + K_sat*math.exp(F*(-1.0 +\
        gamma)*V/(R*T)))*(Ca_o + Km_Ca)*(math.pow(Km_Nai, 3.0) +\
        math.pow(Na_o, 3.0)))

    # Expressions for the Calcium pump current component
    i_p_Ca = g_pCa*Ca_i/(K_pCa + Ca_i)

    # Expressions for the Potassium pump current component
    i_p_K = g_pK*(-E_K + V)/(1.0 +\
        65.40521574193832*math.exp(-0.16722408026755853*V))

    # Expressions for the Calcium dynamics component
    i_rel = (c_rel + a_rel*math.pow(Ca_SR, 2.0)/(math.pow(b_rel, 2.0) +\
        math.pow(Ca_SR, 2.0)))*d*g
    i_up = Vmax_up/(1.0 + math.pow(K_up, 2.0)*math.pow(Ca_i, -2.0))
    i_leak = V_leak*(-Ca_i + Ca_SR)
    g_inf = (1.0/(1.0 + 5.439910241481018e+20*math.pow(Ca_i, 6.0)) if Ca_i <\
        0.00035 else 1.0/(1.0 + 1.9720198874049195e+55*math.pow(Ca_i, 16.0)))
    d_g = (-g + g_inf)/tau_g
    values[11] = (0 if g_inf > g and V > -60.0 else d_g)
    Ca_i_bufc = 1.0/(1.0 + Buf_c*K_buf_c*math.pow(K_buf_c + Ca_i, -2.0))
    Ca_sr_bufsr = 1.0/(1.0 + Buf_sr*K_buf_sr*math.pow(K_buf_sr + Ca_SR, -2.0))
    values[12] = (-i_up - 0.5*Cm*(1.0*i_CaL + 1.0*i_b_Ca + 1.0*i_p_Ca -\
        2.0*i_NaCa)/(F*V_c) + i_leak + i_rel)*Ca_i_bufc
    values[13] = V_c*(-i_leak - i_rel + i_up)*Ca_sr_bufsr/V_sr

    # Expressions for the Sodium dynamics component
    values[14] = 1.0*Cm*(-1.0*i_Na - 1.0*i_b_Na - 3.0*i_NaCa -\
        3.0*i_NaK)/(F*V_c)

    # Expressions for the Membrane component
    i_Stim = (-stim_amplitude if t - stim_period*math.floor(t/stim_period) <=\
        stim_duration + stim_start and t -\
        stim_period*math.floor(t/stim_period) >= stim_start else 0)
    values[15] = -1.0*i_CaL - 1.0*i_K1 - 1.0*i_Kr - 1.0*i_Ks - 1.0*i_Na -\
        1.0*i_NaCa - 1.0*i_NaK - 1.0*i_Stim - 1.0*i_b_Ca - 1.0*i_b_Na -\
        1.0*i_p_Ca - 1.0*i_p_K - 1.0*i_to

    # Expressions for the Potassium dynamics component
    values[16] = 1.0*Cm*(2.0*i_NaK - 1.0*i_K1 - 1.0*i_Kr - 1.0*i_Ks -\
        1.0*i_Stim - 1.0*i_p_K - 1.0*i_to)/(F*V_c)

    # Return results
    return values

def monitor(states, t, parameters, monitored=None):
    """
    Computes monitored expressions of the tentusscher_2004_mcell ODE
    """
    # Imports
    import numpy as np
    import math

    # Assign states
    assert(len(states) == 17)
    Xr1, Xr2, Xs, m, h, j, d, f, fCa, s, r, g, Ca_i, Ca_SR, Na_i, V, K_i =\
        states

    # Assign parameters
    assert(len(parameters) == 45)
    P_kna, g_K1, g_Kr, g_Ks, g_Na, g_bna, g_CaL, g_bca, g_to, K_mNa, K_mk,\
        P_NaK, K_NaCa, K_sat, Km_Ca, Km_Nai, alpha, gamma, K_pCa, g_pCa,\
        g_pK, Buf_c, Buf_sr, Ca_o, K_buf_c, K_buf_sr, K_up, V_leak, V_sr,\
        Vmax_up, a_rel, b_rel, c_rel, tau_g, Na_o, Cm, F, R, T, V_c,\
        stim_amplitude, stim_duration, stim_period, stim_start, K_o =\
        parameters

    # Init return args
    if monitored is None:
        monitored = np.zeros((85,), dtype=np.float_)
    else:
        assert isinstance(monitored, np.ndarray) and monitored.shape == (85,)

    # Expressions for the Reversal potentials component
    monitored[0] = R*T*math.log(Na_o/Na_i)/F
    monitored[1] = R*T*math.log(K_o/K_i)/F
    monitored[2] = R*T*math.log((K_o + Na_o*P_kna)/(P_kna*Na_i + K_i))/F
    monitored[3] = 0.5*R*T*math.log(Ca_o/Ca_i)/F

    # Expressions for the Inward rectifier potassium current component
    monitored[4] = 0.1/(1.0 + 6.14421235332821e-06*math.exp(0.06*V -\
        0.06*monitored[1]))
    monitored[5] = (0.36787944117144233*math.exp(0.1*V - 0.1*monitored[1]) +\
        3.0606040200802673*math.exp(0.0002*V - 0.0002*monitored[1]))/(1.0 +\
        math.exp(0.5*monitored[1] - 0.5*V))
    monitored[6] = monitored[4]/(monitored[4] + monitored[5])
    monitored[7] = 0.4303314829119352*g_K1*math.sqrt(K_o)*(-monitored[1] +\
        V)*monitored[6]

    # Expressions for the Rapid time dependent potassium current component
    monitored[8] = 0.4303314829119352*g_Kr*math.sqrt(K_o)*(-monitored[1] +\
        V)*Xr1*Xr2

    # Expressions for the Xr1 gate component
    monitored[9] = 1.0/(1.0 +\
        0.02437284407327961*math.exp(-0.14285714285714285*V))
    monitored[10] = 450.0/(1.0 + 0.011108996538242306*math.exp(-0.1*V))
    monitored[11] = 6.0/(1.0 +\
        13.581324522578193*math.exp(0.08695652173913043*V))
    monitored[12] = 1.0*monitored[10]*monitored[11]
    monitored[68] = (-Xr1 + monitored[9])/monitored[12]

    # Expressions for the Xr2 gate component
    monitored[13] = 1.0/(1.0 +\
        39.12128399815321*math.exp(0.041666666666666664*V))
    monitored[14] = 3.0/(1.0 + 0.049787068367863944*math.exp(-0.05*V))
    monitored[15] = 1.12/(1.0 + 0.049787068367863944*math.exp(0.05*V))
    monitored[16] = 1.0*monitored[14]*monitored[15]
    monitored[69] = (-Xr2 + monitored[13])/monitored[16]

    # Expressions for the Slow time dependent potassium current component
    monitored[17] = g_Ks*math.pow(Xs, 2.0)*(-monitored[2] + V)

    # Expressions for the Xs gate component
    monitored[18] = 1.0/(1.0 +\
        0.6996725373751304*math.exp(-0.07142857142857142*V))
    monitored[19] = 1100.0/math.sqrt(1.0 +\
        0.18887560283756186*math.exp(-0.16666666666666666*V))
    monitored[20] = 1.0/(1.0 + 0.049787068367863944*math.exp(0.05*V))
    monitored[21] = 1.0*monitored[19]*monitored[20]
    monitored[70] = (-Xs + monitored[18])/monitored[21]

    # Expressions for the Fast sodium current component
    monitored[22] = g_Na*math.pow(m, 3.0)*(-monitored[0] + V)*h*j

    # Expressions for the m gate component
    monitored[23] = 1.0*math.pow(1.0 +\
        0.0018422115811651339*math.exp(-0.1107419712070875*V), -2.0)
    monitored[24] = 1.0/(1.0 + 6.14421235332821e-06*math.exp(-0.2*V))
    monitored[25] = 0.1/(1.0 + 1096.6331584284585*math.exp(0.2*V)) + 0.1/(1.0 +\
        0.7788007830714049*math.exp(0.005*V))
    monitored[26] = 1.0*monitored[24]*monitored[25]
    monitored[71] = (-m + monitored[23])/monitored[26]

    # Expressions for the h gate component
    monitored[27] = 1.0*math.pow(1.0 +\
        15212.593285654404*math.exp(0.13458950201884254*V), -2.0)
    monitored[28] = (4.4312679295805147e-07*math.exp(-0.14705882352941177*V)\
        if V < -40.0 else 0)
    monitored[29] = (310000.0*math.exp(0.3485*V) + 2.7*math.exp(0.079*V) if V\
        < -40.0 else 0.77/(0.13 +\
        0.049758141083938695*math.exp(-0.0900900900900901*V)))
    monitored[30] = 1.0/(monitored[28] + monitored[29])
    monitored[72] = (-h + monitored[27])/monitored[30]

    # Expressions for the j gate component
    monitored[31] = 1.0*math.pow(1.0 +\
        15212.593285654404*math.exp(0.13458950201884254*V), -2.0)
    monitored[32] = (1.0*(37.78 + V)*(-25428.0*math.exp(0.2444*V) -\
        6.948e-06*math.exp(-0.04391*V))/(1.0 +\
        50262745825.95399*math.exp(0.311*V)) if V < -40.0 else 0)
    monitored[33] = (0.02424*math.exp(-0.01052*V)/(1.0 +\
        0.003960868339904256*math.exp(-0.1378*V)) if V < -40.0 else\
        0.6*math.exp(0.057*V)/(1.0 + 0.040762203978366204*math.exp(-0.1*V)))
    monitored[34] = 1.0/(monitored[32] + monitored[33])
    monitored[73] = (-j + monitored[31])/monitored[34]

    # Expressions for the Sodium background current component
    monitored[35] = g_bna*(-monitored[0] + V)

    # Expressions for the L_type Ca current component
    monitored[36] = 4.0*g_CaL*math.pow(F, 2.0)*(-0.341*Ca_o +\
        Ca_i*math.exp(2.0*F*V/(R*T)))*V*d*f*fCa/(R*T*(-1.0 +\
        math.exp(2.0*F*V/(R*T))))

    # Expressions for the d gate component
    monitored[37] = 1.0/(1.0 +\
        0.513417119032592*math.exp(-0.13333333333333333*V))
    monitored[38] = 0.25 + 1.4/(1.0 +\
        0.0677244716592409*math.exp(-0.07692307692307693*V))
    monitored[39] = 1.4/(1.0 + 2.718281828459045*math.exp(0.2*V))
    monitored[40] = 1.0/(1.0 + 12.182493960703473*math.exp(-0.05*V))
    monitored[41] = 1.0*monitored[38]*monitored[39] + monitored[40]
    monitored[74] = (-d + monitored[37])/monitored[41]

    # Expressions for the f gate component
    monitored[42] = 1.0/(1.0 +\
        17.411708063327644*math.exp(0.14285714285714285*V))
    monitored[43] = 80.0 + 165.0/(1.0 + 12.182493960703473*math.exp(-0.1*V))\
        + 1125.0*math.exp(-0.004166666666666667*math.pow(27.0 + V, 2.0))
    monitored[75] = (-f + monitored[42])/monitored[43]

    # Expressions for the FCa gate component
    monitored[44] = 1.0/(1.0 + 8.03402376701711e+27*math.pow(Ca_i, 8.0))
    monitored[45] = 0.1/(1.0 + 0.006737946999085467*math.exp(10000.0*Ca_i))
    monitored[46] = 0.2/(1.0 + 0.391605626676799*math.exp(1250.0*Ca_i))
    monitored[47] = 0.15753424657534246 + 0.684931506849315*monitored[44] +\
        0.684931506849315*monitored[45] + 0.684931506849315*monitored[46]
    monitored[48] = 2.0
    monitored[49] = (-fCa + monitored[47])/monitored[48]
    monitored[76] = (0 if monitored[47] > fCa and V > -60.0 else monitored[49])

    # Expressions for the Calcium background current component
    monitored[50] = g_bca*(-monitored[3] + V)

    # Expressions for the Transient outward current component
    monitored[51] = g_to*(-monitored[1] + V)*r*s

    # Expressions for the s gate component
    monitored[52] = 1.0/(1.0 + 54.598150033144236*math.exp(0.2*V))
    monitored[53] = 3.0 + 5.0/(1.0 + 0.01831563888873418*math.exp(0.2*V)) +\
        85.0*math.exp(-0.003125*math.pow(45.0 + V, 2.0))
    monitored[77] = (-s + monitored[52])/monitored[53]

    # Expressions for the r gate component
    monitored[54] = 1.0/(1.0 +\
        28.031624894526125*math.exp(-0.16666666666666666*V))
    monitored[55] = 0.8 + 9.5*math.exp(-0.0005555555555555556*math.pow(40.0 +\
        V, 2.0))
    monitored[78] = (-r + monitored[54])/monitored[55]

    # Expressions for the Sodium potassium pump current component
    monitored[56] = K_o*P_NaK*Na_i/((K_mNa + Na_i)*(K_mk + K_o)*(1.0 +\
        0.0353*math.exp(-F*V/(R*T)) + 0.1245*math.exp(-0.1*F*V/(R*T))))

    # Expressions for the Sodium calcium exchanger current component
    monitored[57] = K_NaCa*(Ca_o*math.pow(Na_i,\
        3.0)*math.exp(F*gamma*V/(R*T)) - alpha*math.pow(Na_o,\
        3.0)*Ca_i*math.exp(F*(-1.0 + gamma)*V/(R*T)))/((1.0 +\
        K_sat*math.exp(F*(-1.0 + gamma)*V/(R*T)))*(Ca_o +\
        Km_Ca)*(math.pow(Km_Nai, 3.0) + math.pow(Na_o, 3.0)))

    # Expressions for the Calcium pump current component
    monitored[58] = g_pCa*Ca_i/(K_pCa + Ca_i)

    # Expressions for the Potassium pump current component
    monitored[59] = g_pK*(-monitored[1] + V)/(1.0 +\
        65.40521574193832*math.exp(-0.16722408026755853*V))

    # Expressions for the Calcium dynamics component
    monitored[60] = (c_rel + a_rel*math.pow(Ca_SR, 2.0)/(math.pow(b_rel, 2.0)\
        + math.pow(Ca_SR, 2.0)))*d*g
    monitored[61] = Vmax_up/(1.0 + math.pow(K_up, 2.0)*math.pow(Ca_i, -2.0))
    monitored[62] = V_leak*(-Ca_i + Ca_SR)
    monitored[63] = (1.0/(1.0 + 5.439910241481018e+20*math.pow(Ca_i, 6.0)) if\
        Ca_i < 0.00035 else 1.0/(1.0 + 1.9720198874049195e+55*math.pow(Ca_i,\
        16.0)))
    monitored[64] = (-g + monitored[63])/tau_g
    monitored[79] = (0 if monitored[63] > g and V > -60.0 else monitored[64])
    monitored[65] = 1.0/(1.0 + Buf_c*K_buf_c*math.pow(K_buf_c + Ca_i, -2.0))
    monitored[66] = 1.0/(1.0 + Buf_sr*K_buf_sr*math.pow(K_buf_sr + Ca_SR,\
        -2.0))
    monitored[80] = (-monitored[61] - 0.5*Cm*(1.0*monitored[36] +\
        1.0*monitored[50] + 1.0*monitored[58] - 2.0*monitored[57])/(F*V_c) +\
        monitored[60] + monitored[62])*monitored[65]
    monitored[81] = V_c*(-monitored[60] - monitored[62] +\
        monitored[61])*monitored[66]/V_sr

    # Expressions for the Sodium dynamics component
    monitored[82] = 1.0*Cm*(-1.0*monitored[22] - 1.0*monitored[35] -\
        3.0*monitored[56] - 3.0*monitored[57])/(F*V_c)

    # Expressions for the Membrane component
    monitored[67] = (-stim_amplitude if t -\
        stim_period*math.floor(t/stim_period) <= stim_duration + stim_start\
        and t - stim_period*math.floor(t/stim_period) >= stim_start else 0)
    monitored[83] = -1.0*monitored[17] - 1.0*monitored[22] -\
        1.0*monitored[35] - 1.0*monitored[36] - 1.0*monitored[50] -\
        1.0*monitored[51] - 1.0*monitored[56] - 1.0*monitored[57] -\
        1.0*monitored[58] - 1.0*monitored[59] - 1.0*monitored[67] -\
        1.0*monitored[7] - 1.0*monitored[8]

    # Expressions for the Potassium dynamics component
    monitored[84] = 1.0*Cm*(2.0*monitored[56] - 1.0*monitored[17] -\
        1.0*monitored[51] - 1.0*monitored[59] - 1.0*monitored[67] -\
        1.0*monitored[7] - 1.0*monitored[8])/(F*V_c)

    # Return results
    return monitored
