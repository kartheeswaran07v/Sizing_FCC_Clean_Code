import math

N2_val = 0.00214  # mm
N14 = 0.0046  # m

sc_initial_1 = {'valveSize': 0.1, 'valveOutletDiameter': 0.1, 'ratedCV': 195, 'reqCV': 90, 'No': 6, 'FLP': 0.789,
                'Iw': 0.181, 'valveSizeUnit': 'm', 'IwUnit': 'm', 'A': 0.00137, 'xT': 0.75, 'iPipeSize': 0.2,
                'oPipeSize': 0.2,
                'tS': 0.008, 'Di': 0.1, 'SpeedOfSoundinPipe_Cs': 5000, 'DensityPipe_Ps': 8000, 'densityUnit': 'kg/m3',
                'SpeedOfSoundInAir_Co': 343, 'densityAir_Po': 1.293, 'atmPressure_pa': 101325, 'atmPres': 'pa',
                'stdAtmPres_ps': 101325, 'stdAtmPres': 'pa', 'sigmaEta': 0.86, 'etaI': 1.2, 'Fp': 0.98,
                'massFlowrate': 2.22, 'massFlowrateUnit': 'kg/s', 'iPres': 1000000, 'iPresUnit': 'pa',
                'oPres': 720000, 'oPresUnit': 'pa', 'inletDensity': 5.3, 'iAbsTemp': 450, 'iAbsTempUnit': 'K',
                'specificHeatRatio_gamma': 1.22, 'molecularMass': 19.8, 'mMassUnit': 'kg/kmol',
                'internalPipeDia': 0.2031,
                'aEta': -3.8, 'stp': 0.2, 'R': 8314, 'RUnit': "J/kmol x K", 'fs': 1}

sc_initial_2 = {'valveSize': 0.1, 'valveOutletDiameter': 0.1, 'ratedCV': 195, 'reqCV': 90, 'No': 6, 'FLP': 0.789,
                'Iw': 0.181, 'valveSizeUnit': 'm', 'IwUnit': 'm', 'A': 0.00137, 'xT': 0.75, 'iPipeSize': 0.2,
                'oPipeSize': 0.2,
                'tS': 0.008, 'Di': 0.1, 'SpeedOfSoundinPipe_Cs': 5000, 'DensityPipe_Ps': 8000, 'densityUnit': 'kg/m3',
                'SpeedOfSoundInAir_Co': 343, 'densityAir_Po': 1.293, 'atmPressure_pa': 101325, 'atmPres': 'pa',
                'stdAtmPres_ps': 101325, 'stdAtmPres': 'pa', 'sigmaEta': 0.86, 'etaI': 1.2, 'Fp': 0.98,
                'massFlowrate': 2.29, 'massFlowrateUnit': 'kg/s', 'iPres': 1000000, 'iPresUnit': 'pa',
                'oPres': 690000, 'oPresUnit': 'pa', 'inletDensity': 5.3, 'iAbsTemp': 450, 'iAbsTempUnit': 'K',
                'specificHeatRatio_gamma': 1.22, 'molecularMass': 19.8, 'mMassUnit': 'kg/kmol',
                'internalPipeDia': 0.2031,
                'aEta': -3.8, 'stp': 0.2, 'R': 8314, 'RUnit': "J/kmol x K", 'fs': 1}

sc_initial_3 = {'valveSize': 0.1, 'valveOutletDiameter': 0.1, 'ratedCV': 195, 'reqCV': 90, 'No': 6, 'FLP': 0.789,
                'Iw': 0.181, 'valveSizeUnit': 'm', 'IwUnit': 'm', 'A': 0.00137, 'xT': 0.75, 'iPipeSize': 0.2,
                'oPipeSize': 0.2,
                'tS': 0.008, 'Di': 0.1, 'SpeedOfSoundinPipe_Cs': 5000, 'DensityPipe_Ps': 8000, 'densityUnit': 'kg/m3',
                'SpeedOfSoundInAir_Co': 343, 'densityAir_Po': 1.293, 'atmPressure_pa': 101325, 'atmPres': 'pa',
                'stdAtmPres_ps': 101325, 'stdAtmPres': 'pa', 'sigmaEta': 0.86, 'etaI': 1.2, 'Fp': 0.98,
                'massFlowrate': 2.59, 'massFlowrateUnit': 'kg/s', 'iPres': 1000000, 'iPresUnit': 'pa',
                'oPres': 480000, 'oPresUnit': 'pa', 'inletDensity': 5.3, 'iAbsTemp': 450, 'iAbsTempUnit': 'K',
                'specificHeatRatio_gamma': 1.22, 'molecularMass': 19.8, 'mMassUnit': 'kg/kmol',
                'internalPipeDia': 0.2031,
                'aEta': -3.8, 'stp': 0.2, 'R': 8314, 'RUnit': "J/kmol x K", 'fs': 1}

sc_initial_4 = {'valveSize': 0.1, 'valveOutletDiameter': 0.2031, 'ratedCV': 195, 'reqCV': 40, 'No': 6, 'FLP': 0.789,
                'Iw': 0.181, 'valveSizeUnit': 'm', 'IwUnit': 'm', 'A': 0.00137, 'xT': 0.75, 'iPipeSize': 0.2,
                'oPipeSize': 0.2031,
                'tS': 0.008, 'Di': 0.1, 'SpeedOfSoundinPipe_Cs': 5000, 'DensityPipe_Ps': 8000, 'densityUnit': 'kg/m3',
                'SpeedOfSoundInAir_Co': 343, 'densityAir_Po': 1.293, 'atmPressure_pa': 101325, 'atmPres': 'pa',
                'stdAtmPres_ps': 101325, 'stdAtmPres': 'pa', 'sigmaEta': 0.86, 'etaI': 1.2, 'Fp': 0.98,
                'massFlowrate': 1.18, 'massFlowrateUnit': 'kg/s', 'iPres': 1000000, 'iPresUnit': 'pa',
                'oPres': 420000, 'oPresUnit': 'pa', 'inletDensity': 5.3, 'iAbsTemp': 450, 'iAbsTempUnit': 'K',
                'specificHeatRatio_gamma': 1.22, 'molecularMass': 19.8, 'mMassUnit': 'kg/kmol',
                'internalPipeDia': 0.2031,
                'aEta': -3.8, 'stp': 0.2, 'R': 8314, 'RUnit': "J/kmol x K", 'fs': 1}

sc_initial_5 = {'valveSize': 0.1, 'valveOutletDiameter': 0.2031, 'ratedCV': 195, 'reqCV': 40, 'No': 6, 'FLP': 0.789,
                'Iw': 0.181, 'valveSizeUnit': 'm', 'IwUnit': 'm', 'A': 0.00137, 'xT': 0.75, 'iPipeSize': 0.2,
                'oPipeSize': 0.2031,
                'tS': 0.008, 'Di': 0.1, 'SpeedOfSoundinPipe_Cs': 5000, 'DensityPipe_Ps': 8000, 'densityUnit': 'kg/m3',
                'SpeedOfSoundInAir_Co': 343, 'densityAir_Po': 1.293, 'atmPressure_pa': 101325, 'atmPres': 'pa',
                'stdAtmPres_ps': 101325, 'stdAtmPres': 'pa', 'sigmaEta': 0.86, 'etaI': 1.2, 'Fp': 0.98,
                'massFlowrate': 1.19, 'massFlowrateUnit': 'kg/s', 'iPres': 1000000, 'iPresUnit': 'pa',
                'oPres': 50000, 'oPresUnit': 'pa', 'inletDensity': 5.3, 'iAbsTemp': 450, 'iAbsTempUnit': 'K',
                'specificHeatRatio_gamma': 1.22, 'molecularMass': 19.8, 'mMassUnit': 'kg/kmol',
                'internalPipeDia': 0.2031,
                'aEta': -3.8, 'stp': 0.2, 'R': 8314, 'RUnit': "J/kmol x K", 'fs': 1}

sc_initial = sc_initial_5


# def etaB(valveDia, pipeDia):
#     return 1 - ((valveDia / pipeDia) ** 4)
#
#
# def eta1(valveDia, pipeDia):
#     return 0.5 * ((1 - ((valveDia / pipeDia) ** 2)) ** 2)
#
#
# def eta2(valveDia, pipeDia):
#     return 1 * ((1 - ((valveDia / pipeDia) ** 2)) ** 2)
#
#
# def sigmaEta(valveDia, inletDia, outletDia):
#     a_ = eta1(valveDia, inletDia) + eta2(valveDia, outletDia) + etaB(valveDia, inletDia) - etaB(valveDia, outletDia)
#     return round(a_, 2)
#
#
# print(sigmaEta(100, 200, 200), etaB(0.1016, 0.2032))
#
#
# def fP(C, valveDia, inletDia, outletDia, N2_value):
#     a = (sigmaEta(valveDia, inletDia, outletDia) / N2_value) * ((C / valveDia ** 2) ** 2)
#     b_ = 1 / math.sqrt(1 + a)
#     return round(b_, 2)
#
#
# print(fP(sc_initial['reqCV'], sc_initial['valveSize'] * 1000, sc_initial['iPipeSize'] * 1000,
#          sc_initial['oPipeSize'] * 1000, N2_val))

# diff pressure ratio
def X(inletPressure, outletPressure):
    a = (inletPressure - outletPressure) / inletPressure
    return a


# print(X(sc_initial['iPres'], sc_initial['oPres']))


# absolute vena contracta pressure at subsonic flow conditions
def PVC(inletPressure, outletPressure, Flp, Fp):
    x = X(inletPressure, outletPressure)
    a_ = x / ((Flp / Fp) ** 2)
    a = inletPressure * (1 - a_)
    return round(a, 1)


# print(PVC(sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp']))


# Vena contracta differential pressure ratio at critical flow conditions
def XVCC(gamma):
    a_ = (2 / (gamma + 1)) ** (gamma / (gamma - 1))
    a = 1 - a_
    return round(a, 3)


# print(XVCC(sc_initial['specificHeatRatio_gamma']))


# differential pressure ratio at critical flow conditions
def XC(gamma, Flp, Fp):
    xvcc = XVCC(gamma)
    a_ = ((Flp / Fp) ** 2) * xvcc
    return round(a_, 3)


# print(XC(sc_initial['specificHeatRatio_gamma'], sc_initial['FLP'], sc_initial['Fp']))


# recovery correction factor
def alpha(gamma, Flp, Fp):
    xvcc = XVCC(gamma)
    xc = XC(gamma, Flp, Fp)
    a = (1 - xvcc) / (1 - xc)
    return round(a, 3)


# print(alpha(sc_initial['specificHeatRatio_gamma'], sc_initial['FLP'], sc_initial['Fp']))


# differential pressure ratio at break point
def XB(gamma, Flp, Fp):
    a_ = (1 / gamma) ** (gamma / (gamma - 1))
    al = alpha(gamma, Flp, Fp)
    b_ = (1 / al) * a_
    a = 1 - b_
    return round(a, 3)


# print(XB(sc_initial['specificHeatRatio_gamma'], sc_initial['FLP'], sc_initial['Fp']))


# differential pressure ratio where region of constant acoustical efficienty begins
def XCE(gamma, Flp, Fp):
    al = alpha(gamma, Flp, Fp)
    a = 1 - (1 / (22 * al))
    return round(a, 3)


# print(XCE(gamma=sc_initial['specificHeatRatio_gamma'], Flp=sc_initial['FLP'], Fp=sc_initial['Fp']))


# choose regime
def getRegime(inletPressure, outletPressure, gamma, Flp, Fp):
    x = X(inletPressure, outletPressure)
    xc = XC(gamma, Flp, Fp)
    xvcc = XVCC(gamma)
    xb = XB(gamma, Flp, Fp)
    xce = XCE(gamma, Flp, Fp)

    if x <= xc:
        return 'I'
    elif xc < x <= xvcc:
        return 'II'
    elif xvcc < x <= xb:
        return 'III'
    elif xb < x <= xce:
        return 'IV'
    elif xce < x:
        return 'V'


# print(getRegime(sc_initial['iPres'], sc_initial['oPres'], sc_initial['specificHeatRatio_gamma'], sc_initial['FLP'], sc_initial['Fp']))


# hydraulic diameter of a single flow passage
def dH(A, Iw):
    a = 4 * A / Iw
    return round(a, 3)


# print(dH(sc_initial['A'], sc_initial['Iw']))
# diameter of a circular orifice
def dO(No, A):
    a_ = (4 * No * A) / math.pi
    a = math.sqrt(a_)
    return round(a, 3)


# print(dO(sc_initial['No'], sc_initial['A']))
# valve style modifier
def FD(No, A, Iw):
    dh = dH(A, Iw)
    do = dO(No, A)
    a = dh / do
    return round(a, 3)


# print(FD(sc_initial['No'], sc_initial['A'], sc_initial['Iw']))

# Jet Diameter
def DJ(No, A, Iw, C, Flp, Fp):
    a_ = math.sqrt(C * Flp / Fp)
    fd = FD(No, A, Iw)
    a = N14 * fd * a_
    return round(a, 3)


# print(DJ(sc_initial['No'], sc_initial['A'], sc_initial['Iw'], sc_initial['reqCV'], sc_initial['FLP'], sc_initial[
# 'Fp']))

# TODO - Calculations for REGIME I

# Mach NUMBER AT Vena Contracta
def MVC_I(gamma, inletPressure, outletPressure, Flp, Fp):
    Fl = Flp / Fp
    a_ = 2 / (gamma - 1)
    x = X(inletPressure, outletPressure)
    b__ = 1 - (x / Fl ** 2)
    b_ = (b__ ** ((1 - gamma) / gamma)) - 1
    a = math.sqrt(a_ * b_)
    return round(a, 3)


# print(MVC_I(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp']))

# Acoustical efficiency factor - aef
def eta_aef_I(gamma, inletPressure, outletPressure, Flp, Fp, aEta):
    a_ = 1 * (10 ** aEta)
    b_ = (Flp / Fp) ** 2
    mvc3 = MVC_I(gamma, inletPressure, outletPressure, Flp, Fp) ** 3
    # mvc3 = 0.988**3
    a = a_ * b_ * mvc3
    return round(a, 7)


# print(eta_aef_I(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp'], sc_initial['aEta']))

# Speed of sound in vena contracta
def CVC_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi):
    x = X(inletPressure, outletPressure)
    Fl = Flp / Fp
    b__ = (1 - (x / Fl ** 2)) ** ((gamma - 1) / gamma)
    c_ = gamma * inletPressure / Pi
    a = math.sqrt(c_ * b__)
    return round(a, 2)


# print(CVC_I(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp'], sc_initial['inletDensity']))

# Vena contracta absolute temperature
def TVC_I(gamma, inletPressure, outletPressure, Flp, Fp, inletTemp):
    x = X(inletPressure, outletPressure)
    Fl = Flp / Fp
    b__ = (1 - (x / Fl ** 2)) ** ((gamma - 1) / gamma)
    a = inletTemp * b__
    return round(a, 1)


# print(TVC_I(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp'], sc_initial['iAbsTemp']))

# Stream power of mass flow
def WM_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate):
    mvc = MVC_I(gamma, inletPressure, outletPressure, Flp, Fp)
    cvc = CVC_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi)
    a_ = (mvc * cvc) ** 2
    a = massflowrate * a_ / 2
    return round(a, 1)


# print(WM_I(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['massFlowrate']))

# Sound power
def WA_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta):
    eta_ae = eta_aef_I(gamma, inletPressure, outletPressure, Flp, Fp, aEta)
    wm = WM_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate)
    a = eta_ae * wm
    return round(a, 1)


# print(WA_I(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['massFlowrate'], sc_initial['aEta']))

# Peak Frequency
def peakFreq_fp_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C):
    dj = DJ(No, A, Iw, C, Flp, Fp)
    mvc = MVC_I(gamma, inletPressure, outletPressure, Flp, Fp)
    cvc = CVC_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi)
    a = stp * mvc * cvc / dj
    return a


# print(peakFreq_fp(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#                   sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['stp'], sc_initial['No'], sc_initial['A'],
#                   sc_initial['Iw'], sc_initial['reqCV']))


# ------------------------------------------------------------------ XXX ---------------------------------------- #

# TODO - Calculations for REGIME II
# Speed of sound in vena contracta
def CVC_II(gamma, inletPressure, Pi):
    a_ = 2 * gamma * inletPressure / ((gamma + 1) * Pi)
    a = math.sqrt(a_)
    return round(a, 1)


# print(CVC_II(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['inletDensity']))


# Stream power of mass flow
def WM_II(gamma, inletPressure, Pi, massflowrate):
    cvcc = CVC_II(gamma, inletPressure, Pi)
    a = (massflowrate * cvcc * cvcc) / 2
    return round(a, 1)


#
# print(WM_II(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['inletDensity'],
#             sc_initial['massFlowrate']))


# Freely expanded jet Mach number
def MJ_II(gamma, inletPressure, outletPressure, Flp, Fp):
    x = X(inletPressure, outletPressure)
    al = alpha(gamma, Flp, Fp)
    a_1 = (2 / (gamma - 1)) * (((1 / (al * (1 - x))) ** ((gamma - 1) / gamma)) - 1)
    a1 = math.sqrt(a_1)
    a_2 = (2 / (gamma - 1)) * ((22 ** ((gamma - 1) / gamma)) - 1)
    a2 = math.sqrt(a_2)
    # print(a1, a2)
    a = min(a1, a2)
    return round(a, 2)


#
#
# print(MJ_II(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#             sc_initial['Fp']))


# Acoustic efficiency factor
def eta_aef_II(gamma, inletPressure, outletPressure, Flp, Fp, aEta):
    mj = MJ_II(gamma, inletPressure, outletPressure, Flp, Fp)
    x = X(inletPressure, outletPressure)
    xvcc = XVCC(gamma)
    power = 6.6 * ((Flp / Fp) ** 2)
    print(power)
    mj_p = mj ** power
    print(mj_p)
    a_ = 1 * (10 ** aEta)
    # print(a_)
    b_ = x / xvcc
    a = a_ * b_ * mj_p
    return round(a, 5)


# print(eta_aef_II(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#                  sc_initial['Fp'], sc_initial['aEta']))


def WA_II(gamma, inletPressure, outletPressure, Flp, Fp, aEta, Pi, massflowrate):
    eta_aef = eta_aef_II(gamma, inletPressure, outletPressure, Flp, Fp, aEta)
    wm = WM_II(gamma, inletPressure, Pi, massflowrate)
    wa = eta_aef * wm
    return round(wa, 1)


# Peak Frequency
def peakFreq_fp_II(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C):
    dj = DJ(No, A, Iw, C, Flp, Fp)
    mj = MJ_II(gamma, inletPressure, outletPressure, Flp, Fp)
    cvc = CVC_II(gamma, inletPressure, Pi)
    a = stp * mj * cvc / dj
    return a


#
# print(WA_II(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#             sc_initial['Fp'], sc_initial['aEta'], sc_initial['inletDensity'], sc_initial['massFlowrate']))
# print(peakFreq_fp_II(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#                      sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['stp'], sc_initial['No'], sc_initial['A'],
#                      sc_initial['Iw'], sc_initial['reqCV']))


# TODO - Calculations for REGIME III
def eta_aef_III(gamma, inletPressure, outletPressure, Flp, Fp, aEta):
    mj = MJ_II(gamma, inletPressure, outletPressure, Flp, Fp)
    power = 6.6 * ((Flp / Fp) ** 2)
    # print(power)
    mj_p = mj ** power
    # print(mj_p)
    a_ = 1 * (10 ** aEta)
    # print(a_)
    a = a_ * mj_p
    return round(a, 5)


#
# print(eta_aef_III(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#                   sc_initial['Fp'], sc_initial['aEta']))


def WA_III(gamma, inletPressure, outletPressure, Flp, Fp, aEta, Pi, massflowrate):
    eta_aef = eta_aef_III(gamma, inletPressure, outletPressure, Flp, Fp, aEta)
    wm = WM_II(gamma, inletPressure, Pi, massflowrate)
    wa = eta_aef * wm
    return round(wa, 1)


# Peak Frequency
def peakFreq_fp_III(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C):
    dj = DJ(No, A, Iw, C, Flp, Fp)
    mj = MJ_II(gamma, inletPressure, outletPressure, Flp, Fp)
    cvc = CVC_II(gamma, inletPressure, Pi)
    a = stp * mj * cvc / dj
    return a


#
#
# print(WA_III(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#              sc_initial['Fp'], sc_initial['aEta'], sc_initial['inletDensity'], sc_initial['massFlowrate']))
# print(
#     peakFreq_fp_III(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#                     sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['stp'], sc_initial['No'], sc_initial['A'],
#                     sc_initial['Iw'], sc_initial['reqCV']))


# TODO - Calculations for REGIME IV
def eta_aef_IV(gamma, inletPressure, outletPressure, Flp, Fp, aEta):
    mj = MJ_II(gamma, inletPressure, outletPressure, Flp, Fp)
    b_ = mj * mj / 2
    power = 6.6 * ((Flp / Fp) ** 2)
    # print(power)
    mj_p = math.sqrt(2) ** power
    # print(mj_p)
    a_ = 1 * (10 ** aEta)
    # print(a_)
    a = a_ * b_ * mj_p
    return round(a, 4)


#
# print(eta_aef_IV(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#                  sc_initial['Fp'], sc_initial['aEta']))


def WA_IV(gamma, inletPressure, outletPressure, Flp, Fp, aEta, Pi, massflowrate):
    eta_aef = eta_aef_IV(gamma, inletPressure, outletPressure, Flp, Fp, aEta)
    wm = WM_II(gamma, inletPressure, Pi, massflowrate)
    wa = eta_aef * wm
    return round(wa, 1)


# Peak Frequency
def peakFreq_fp_IV(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C):
    dj = DJ(No, A, Iw, C, Flp, Fp)
    mj = MJ_II(gamma, inletPressure, outletPressure, Flp, Fp)
    cvc = CVC_II(gamma, inletPressure, Pi)
    a__ = 1.4 * stp * cvc
    b__ = dj * math.sqrt(mj * mj - 1)
    a = a__ / b__
    return round(a, 1)


# print(WA_IV(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#             sc_initial['Fp'], sc_initial['aEta'], sc_initial['inletDensity'], sc_initial['massFlowrate']))
# print(
#     peakFreq_fp_IV(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#                    sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['stp'], sc_initial['No'], sc_initial['A'],
#                    sc_initial['Iw'], sc_initial['reqCV']))


# TODO - Calculations for REGIME V
# same as regime v formulae

# ------------------------------------------------------------------ XXX ---------------------------------------- #

# outlet Density
def outletDensity(inletPressure, outletPressure, Pi):
    a = Pi * (outletPressure / inletPressure)
    return round(a, 1)


# print(outletDensity(sc_initial['iPres'], sc_initial['oPres'], sc_initial['inletDensity']))
# speed of sound at downstream conditions
def C2(gamma, R, temp, M):
    a_ = gamma * R * temp / M
    a = math.sqrt(a_)
    return round(a)


# print(C2(sc_initial['specificHeatRatio_gamma'], sc_initial['R'], sc_initial['iAbsTemp'], sc_initial['molecularMass']))

# mach number at valve outlet
def MO(gamma, inletPressure, outletPressure, Pi, R, temp, M, massflowrate, valveDia):
    p2 = outletDensity(inletPressure, outletPressure, Pi)
    c2 = C2(gamma, R, temp, M)
    a_ = math.pi * valveDia * valveDia * p2 * c2
    a = 4 * massflowrate / a_
    return round(a, 2)


# mach number at donstream pipe - nothing but MO with valveDia as internalPipeDia

# print(MO(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['inletDensity'], sc_initial['R'], sc_initial['iAbsTemp'], sc_initial['molecularMass'], sc_initial['massFlowrate'], sc_initial['internalPipeDia']))
# Correction for Mach number
def LG(gamma, inletPressure, outletPressure, Pi, R, temp, M, massflowrate, oPipeDia):
    m2 = MO(gamma, inletPressure, outletPressure, Pi, R, temp, M, massflowrate, oPipeDia)
    a_ = 1 / (1 - m2)
    print(m2)
    a = 16 * math.log10(a_)
    return round(a, 2)


#
# #
# print(LG(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['inletDensity'],
#          sc_initial['R'], sc_initial['iAbsTemp'], sc_initial['molecularMass'], sc_initial['massFlowrate'],
#          sc_initial['iPipeSize']))


def WA(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta):
    if getRegime(inletPressure, outletPressure, gamma, Flp, Fp) == "I":
        wa = WA_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta)
    elif getRegime(inletPressure, outletPressure, gamma, Flp, Fp) == "II":
        wa = WA_II(gamma, inletPressure, outletPressure, Flp, Fp, aEta, Pi, massflowrate)
    elif getRegime(inletPressure, outletPressure, gamma, Flp, Fp) == "III":
        wa = WA_III(gamma, inletPressure, outletPressure, Flp, Fp, aEta, Pi, massflowrate)
    elif getRegime(inletPressure, outletPressure, gamma, Flp, Fp) == "IV":
        wa = WA_IV(gamma, inletPressure, outletPressure, Flp, Fp, aEta, Pi, massflowrate)
    else:
        wa = WA_IV(gamma, inletPressure, outletPressure, Flp, Fp, aEta, Pi, massflowrate)

    return wa


def peakFreq_fp(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C):
    if getRegime(inletPressure, outletPressure, gamma, Flp, Fp) == "I":
        fp = peakFreq_fp_I(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C)
    elif getRegime(inletPressure, outletPressure, gamma, Flp, Fp) == "II":
        fp = peakFreq_fp_II(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C)
    elif getRegime(inletPressure, outletPressure, gamma, Flp, Fp) == "III":
        fp = peakFreq_fp_III(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C)
    elif getRegime(inletPressure, outletPressure, gamma, Flp, Fp) == "IV":
        fp = peakFreq_fp_IV(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C)
    else:
        fp = peakFreq_fp_IV(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C)

    return fp


# overall internal sound-pressure level
def LPI(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta, R, temp, M, oPipeDia, internalPipeDia):
    wa = WA(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta)
    p2 = outletDensity(inletPressure, outletPressure, Pi)
    c2 = C2(gamma, R, temp, M)
    lg = LG(gamma, inletPressure, outletPressure, Pi, R, temp, M, massflowrate, oPipeDia)
    # print(f"Wa: {wa}, p2: {p2}, c2: {c2}, dj: , lg: {lg}")

    a__ = (3.2 * (10 ** 9)) * wa * p2 * c2 / (internalPipeDia ** 2)
    a_ = 10 * math.log10(a__)
    a = a_ + lg
    return round(a, 1)


#
# print(LPI(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#           sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['massFlowrate'], sc_initial['aEta'], sc_initial['R'],
#           sc_initial['iAbsTemp'], sc_initial['molecularMass'], sc_initial['oPipeSize'], sc_initial['internalPipeDia']))


# Frequency dependent internal spl (3rd octave bands: 12.5hz - 20 khz)
def L_pi_fi(fi, gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta, R, temp, M, oPipeDia,
            internalPipeDia, stp, No, A, Iw, C):
    fp = peakFreq_fp(gamma, inletPressure, outletPressure, Flp, Fp, Pi, stp, No, A, Iw, C)
    a__ = 1 + ((fi / (2 * fp)) ** 2.5)
    b__ = 1 + ((fp / (2 * fi)) ** 1.7)
    a_ = a__ * b__
    lpi = LPI(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta, R, temp, M, oPipeDia,
              internalPipeDia)
    a = lpi - 8 - 10 * math.log10(a_)
    return round(a)


# print(L_pi_fi(12.5, sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'],
#               sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['massFlowrate'], sc_initial['aEta'],
#               sc_initial['R'], sc_initial['iAbsTemp'], sc_initial['molecularMass'], sc_initial['oPipeSize'],
#               sc_initial['internalPipeDia'], sc_initial['stp'], sc_initial['No'], sc_initial['A'], sc_initial['Iw'],
#               sc_initial['reqCV']))

# f_i indexed frequency bands
frequencies = [12.5, 16, 20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250,
               1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000, 12500, 16000, 20000]
# delta_LA(fi)
a_factor = [-63.4, -56.7, -50.5, -44.7, -39.4, -34.6, -30.2, -26.2, 22.5, -19.1, -16.1, -13.4, -10.9, -8.6, -6.6, -4.8,
            -3.2, -1.9, -0.8, 0, 0.6, 1, 1.2, 1.3, 1.2, 1, 0.5, -0.1, -1.1, -2.5, -4.3, -6.6, -9.3]

freq_dict_list = []

for i in range(len(frequencies)):
    a_dict = {'fr': frequencies[i], 'del_l': a_factor[i]}
    freq_dict_list.append(a_dict)


# print(freq_dict_list)


# #
# for i in frequencies:
#     print(L_pi_fi(i, sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp'], sc_initial['inletDensity'], sc_initial['massFlowrate'], sc_initial['aEta'], sc_initial['R'], sc_initial['iAbsTemp'], sc_initial['molecularMass'], sc_initial['oPipeSize'], sc_initial['internalPipeDia'], sc_initial['stp'], sc_initial['No'], sc_initial['A'], sc_initial['Iw'], sc_initial['reqCV']))


# TODO - if MO is greater than 0.3, do the following formulae - 34-43 - only for Case 6 in testing
# Gas velocity in downstream pipe
def UP(gamma, inletPressure, outletPressure, Pi, massflowrate, internalPipeDia, R, temp, M):
    p2 = outletDensity(inletPressure, outletPressure, Pi)
    c2 = C2(gamma, R, temp, M)
    a = 4 * massflowrate / (math.pi * p2 * internalPipeDia * internalPipeDia)
    if a <= 0.8 * c2:
        print('UP is less than 0.8*c2')
    return a


# TODO - End of 43

# 7 more equations to go
# equations for MO greater than 0. 3 =
# ring frequency
def fr(cs, internalPipeDia):
    a = cs / (math.pi * internalPipeDia)
    return round(a)


# print(fr(sc_initial['SpeedOfSoundinPipe_Cs'], sc_initial['internalPipeDia']))
# internal coincidence pipe frequency
def fo(gamma, R, temp, M, cs, internalPipeDia, ca):
    c2 = C2(gamma, R, temp, M)
    f_r = fr(cs, internalPipeDia)
    a = f_r * c2 / (4 * ca)
    return round(a)


# print(fo(sc_initial['specificHeatRatio_gamma'], sc_initial['R'], sc_initial['iAbsTemp'], sc_initial['molecularMass'], sc_initial['SpeedOfSoundinPipe_Cs'], sc_initial['internalPipeDia'], sc_initial['SpeedOfSoundInAir_Co']))

# external coincidence frequency
def fg(ca, cs, ts):
    a = math.sqrt(3) * ca * ca / (math.pi * ts * cs)
    return round(a)


# print(fg(sc_initial['SpeedOfSoundInAir_Co'], sc_initial['SpeedOfSoundinPipe_Cs'], sc_initial['tS']))

# frequency factor Gx
def GX_fi(gamma, R, temp, M, cs, internalPipeDia, ca, fi):
    f_O = fo(gamma, R, temp, M, cs, internalPipeDia, ca)
    f_r = fr(cs, internalPipeDia)

    if fi < f_O:
        a_ = (f_O / f_r) ** (2 / 3)
        b_ = (fi / f_O) ** 4
        a = a_ * b_
        return a
    elif f_O <= fi < f_r:
        a = (fi / f_r) ** (1 / 2)
        return a
    elif (fi >= f_O) and (fi >= f_r):
        a = 1
        return a


#
# for i in frequencies:
#     print(GX_fi(sc_initial['specificHeatRatio_gamma'], sc_initial['R'], sc_initial['iAbsTemp'],
#                 sc_initial['molecularMass'], sc_initial['SpeedOfSoundinPipe_Cs'], sc_initial['internalPipeDia'],
#                 sc_initial['SpeedOfSoundInAir_Co'], i))


# Frequency factor Gy
def GY_fi(gamma, R, temp, M, cs, internalPipeDia, ca, ts, fi):
    f_o = fo(gamma, R, temp, M, cs, internalPipeDia, ca)
    f_g = fg(ca, cs, ts)

    if fi < f_o < f_g:
        a = f_o / f_g
        return a
    elif fi < f_o and f_o >= f_g:
        return 1
    elif f_o <= fi < f_g:
        a = fi / f_g
        return a
    elif fi >= f_o and fi >= f_g:
        return 1


#
# for i in frequencies:
#     print(GY_fi(sc_initial['specificHeatRatio_gamma'], sc_initial['R'], sc_initial['iAbsTemp'], sc_initial['molecularMass'], sc_initial['SpeedOfSoundinPipe_Cs'], sc_initial['internalPipeDia'], sc_initial['SpeedOfSoundInAir_Co'], sc_initial['tS'], i))

# frequency dependent structural loss factor

def eta_S_fi(fs, fi):
    # Structural loss factor reference frequency = 1 Hz - fs
    a = math.sqrt(fs / (fi * 100))
    return round(a, 5)


# for i in frequencies:
#     print(eta_S_fi(1, i))

# damping factor for transmission loss
def del_TL(valveDia):
    a = -16660 * (valveDia ** 3) + 6370 * (valveDia ** 2) - 813 * valveDia + 35.8
    if valveDia > 0.15:
        return 0
    elif 0.05 <= valveDia <= 0.15:
        return round(a, 1)
    elif valveDia < 0.05:
        return 9


# print(del_TL(sc_initial['valveSize']))

# Frequency dependent transmission loss
def TL_fi(gamma, inletPressure, outletPressure, Pi, R, temp, M, cs, internalPipeDia, ca, valveDia, ts, fs, fi, pa, ps,
          rho_s):
    c2 = C2(gamma, R, temp, M)
    eta_s = eta_S_fi(fs, fi)
    p2 = outletDensity(inletPressure, outletPressure, Pi)
    gyfi = GY_fi(gamma, R, temp, M, cs, internalPipeDia, ca, ts, fi)
    gxfi = GX_fi(gamma, R, temp, M, cs, internalPipeDia, ca, fi)
    d_tl = del_TL(valveDia)
    denom = ((p2 * c2 + 2 * math.pi * ts * fi * rho_s * eta_s) / (415 * gyfi)) + 1
    numer = (8.25 * (10 ** (-7))) * ((c2 / (ts * fi)) ** 2) * gxfi
    pres_factor = pa / ps
    a_ = numer * pres_factor / denom
    a = 10 * math.log10(a_) - d_tl
    return round(a, 1)

    # ca, valveDia, ts, fs, fi, pa, ps, rho_s


# for i in frequencies:
#     print(TL_fi(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['inletDensity'], sc_initial['R'], sc_initial['iAbsTemp'], sc_initial['molecularMass'], sc_initial['SpeedOfSoundinPipe_Cs'], sc_initial['internalPipeDia'], sc_initial['SpeedOfSoundInAir_Co'], sc_initial['valveSize'], sc_initial['tS'], 1, i, sc_initial['atmPressure_pa'], sc_initial['stdAtmPres_ps'], sc_initial['DensityPipe_Ps']))

# frequency dependent external sound pressure level
def lpe_1m_fi(fi, gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta, R, temp, M, oPipeDia,
              internalPipeDia, stp, No, A, Iw, C, cs, ca, valveDia, ts, fs, pa, ps, rho_s):
    lpi_fi = L_pi_fi(fi, gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta, R, temp, M, oPipeDia,
                     internalPipeDia, stp, No, A, Iw, C)
    tl_fi = TL_fi(gamma, inletPressure, outletPressure, Pi, R, temp, M, cs, internalPipeDia, ca, valveDia, ts, fs, fi,
                  pa, ps, rho_s)

    a_ = (internalPipeDia + 2 * ts + 2) / (internalPipeDia + 2 * ts)
    a__ = 10 * math.log10(a_)
    a = lpi_fi + tl_fi - a__
    return a


# A weighted sound-pressure level 1m from pipe wall
def lpae_1m(gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta, R, temp, M, oPipeDia,
            internalPipeDia, stp, No, A, Iw, C, cs, ca, valveDia, ts, fs, pa, ps, rho_s):

    sum__ = 0

    for dict__ in freq_dict_list:
        lpe_1m = lpe_1m_fi(dict__['fr'], gamma, inletPressure, outletPressure, Flp, Fp, Pi, massflowrate, aEta, R, temp,
                           M, oPipeDia,
                           internalPipeDia, stp, No, A, Iw, C, cs, ca, valveDia, ts, fs, pa, ps, rho_s)
        a = (lpe_1m + dict__['del_l']) / 10
        b = 10 ** a
        sum__ += b

    output = 10*math.log10(sum__)
    return round(output)


# print(lpae_1m(sc_initial['specificHeatRatio_gamma'], sc_initial['iPres'], sc_initial['oPres'], sc_initial['FLP'], sc_initial['Fp'],
#               sc_initial['inletDensity'], sc_initial['massFlowrate'], sc_initial['aEta'], sc_initial['R'], sc_initial['iAbsTemp'],
#               sc_initial['molecularMass'], sc_initial['oPipeSize'], sc_initial['internalPipeDia'], sc_initial['stp'], sc_initial['No'],
#               sc_initial['A'], sc_initial['Iw'], sc_initial['reqCV'], sc_initial['SpeedOfSoundinPipe_Cs'], sc_initial['SpeedOfSoundInAir_Co'],
#               sc_initial['valveSize'], sc_initial['tS'], sc_initial['fs'], sc_initial['atmPressure_pa'], sc_initial['stdAtmPres_ps'], sc_initial['DensityPipe_Ps']))


# formulas for Mo>0.3 is pending...