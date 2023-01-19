import math

N34 = 1.17
N14 = 0.0046

sc_3 = {'valveDia': 0.1, 'valveDiaUnit': 'm', 'ratedCV': 195, 'reqCV': 90, 'FL': 0.92, 'FD': 0.42,
        'iPipeDia': 0.1, 'iPipeUnit': 'm', 'oPipeDia': 0.1, 'oPipeUnit': 'm', 'internalPipeDia': 0.1071,
        'inPipeDiaUnit': 'm', 'pipeWallThickness': 0.0036, 'speedSoundPipe': 5000, 'speedSoundPipeUnit': 'm/s',
        'densityPipe': 7800, 'densityPipeUnit': 'kg/m3', 'speedSoundAir': 343, 'densityAir': 1293,
        'massFlowRate': 30, 'massFlowRateUnit': 'kg/s', 'iPressure': 1000000, 'iPresUnit': 'pa', 'oPressure': 800000,
        'oPresUnit': 'pa', 'vPressure': 2320, 'densityLiq': 997, 'speedSoundLiq': 1400, 'rw': 0.25, 'seatDia': 0.1,
        'fi': 8000}

sc_2 = {'valveDia': 0.1, 'valveDiaUnit': 'm', 'ratedCV': 195, 'reqCV': 90, 'FL': 0.92, 'FD': 0.42,
        'iPipeDia': 0.1, 'iPipeUnit': 'm', 'oPipeDia': 0.1, 'oPipeUnit': 'm', 'internalPipeDia': 0.1071,
        'inPipeDiaUnit': 'm', 'pipeWallThickness': 0.0036, 'speedSoundPipe': 5000, 'speedSoundPipeUnit': 'm/s',
        'densityPipe': 7800, 'densityPipeUnit': 'kg/m3', 'speedSoundAir': 343, 'densityAir': 1293,
        'massFlowRate': 40, 'massFlowRateUnit': 'kg/s', 'iPressure': 1000000, 'iPresUnit': 'pa', 'oPressure': 650000,
        'oPresUnit': 'pa', 'vPressure': 2320, 'densityLiq': 997, 'speedSoundLiq': 1400, 'rw': 0.25, 'seatDia': 0.1,
        'fi': 8000}

# Example from sizing, to validate
service_conditions_1B = {'flowrate': 800, 'flowrate_unit': 'gpm', 'iPres': 314.7, 'oPres': 289.7, 'iPresUnit': 'psia',
                         'oPresUnit': 'psia', 'temp': 70, 'temp_unit': 'F', 'sGravity': 0.5, 'iPipeDia': 8,
                         'oPipeDia': 8,
                         'valveDia': 4, 'iPipeDiaUnit': 'inch', 'oPipeDiaUnit': 'inch', 'valveDiaUnit': 'inch',
                         'C': 203, 'FR': 1, 'vPres': 124.3, 'Fl': 0.84, 'Ff': 0.90}

# liq sizing ex - converted validation - flowrate to kg/s, 3 pres to pa, sgravity to density, 4 dias to m,
sc_4 = {'valveDia': 0.1016, 'valveDiaUnit': 'm', 'ratedCV': 203, 'reqCV': 121.7, 'FL': 0.84, 'FD': 0.42,
        'iPipeDia': 0.2032, 'iPipeUnit': 'm', 'oPipeDia': 0.2032, 'oPipeUnit': 'm', 'internalPipeDia': 0.2032,
        'inPipeDiaUnit': 'm', 'pipeWallThickness': 0.0036, 'speedSoundPipe': 5000, 'speedSoundPipeUnit': 'm/s',
        'densityPipe': 7800, 'densityPipeUnit': 'kg/m3', 'speedSoundAir': 343, 'densityAir': 1293,
        'massFlowRate': 25.236, 'massFlowRateUnit': 'kg/s', 'iPressure': 2169780.1, 'iPresUnit': 'pa', 'oPressure': 1997411.2,
        'oPresUnit': 'pa', 'vPressure': 857018.33, 'densityLiq': 500, 'speedSoundLiq': 1400, 'rw': 0.25, 'seatDia': 0.1,
        'fi': 8000}


sc_1 = sc_2


# differential pressure ratio
def xF(inletPressure, outletPressure, vaporPressure):
    a_ = (inletPressure - outletPressure) / (inletPressure - vaporPressure)
    # print(f"XF: {a_}")
    return round(a_, 4)


# print(xF(sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure']))

# pressure differential for UVC calculation
def deltaPC(inletPressure, outletPressure, vaporPressure, Fl):
    a = inletPressure - outletPressure
    b = (Fl ** 2) * (inletPressure - vaporPressure)
    # print(f"deltaPC: {min(a, b)}")
    return min(a, b)


# print(deltaPC(sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['FL']))

# differential pressure for incipient cavitation noise
def xFZ(Fl, Fd, C):
    a = 0.90 / math.sqrt(1 + (3 * Fd * math.sqrt(C / (N34 * Fl))))
    # For hole trim

    # print(f"xFZ: {a}")
    return round(a, 4)


# xFZ(sc_1['FL'], sc_1['FD'], sc_1['reqCV'])

# differential pressure ratio corrected for inlet pressure
def XFZP1(Fl, Fd, C, inletPressure):
    a = xFZ(Fl, Fd, C) * ((600000 / inletPressure) ** 0.125)
    # print(f"xFZP1: {a}")
    return round(a, 4)


# XFZP1(sc_1['FL'], sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'])


# Jet Diameter
def jetDia(Fl, Fd, C):
    # print(f"jetDia: {N14 * Fd * math.sqrt(C * Fl)}")
    a = N14 * Fd * math.sqrt(C * Fl)
    return round(a, 5)


# print(jetDia(sc_1['FL'], sc_1['FD'], sc_1['reqCV']))

# Vena contracta velocity
def jetVelocity(inletPressure, outletPressure, vaporPressure, density, Fl):
    a = (1 / Fl) * (math.sqrt(2 * deltaPC(inletPressure, outletPressure, vaporPressure, Fl) / density))
    # print(f"jetVelocity: {a}")
    return round(a, 3)


# print(jetVelocity(sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['densityLiq'], sc_1['FL']))

# mechanical stream power
def mechanicalPower(massFlowRate, Fl, inletPressure, outletPressure, vaporPressure, density):
    Wm = massFlowRate * (jetVelocity(inletPressure, outletPressure, vaporPressure, density, Fl) ** 2) * Fl * Fl * 0.5
    # print(f"Mechanical Power: {Wm}")
    return round(Wm, 2)


# print(mechanicalPower(sc_1['massFlowRate'], sc_1['FL'], sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['densityLiq']))

def flowCondition(inletPressure, outletPressure, vaporPressure, Fl, Fd, C):
    delP = deltaPC(inletPressure, outletPressure, vaporPressure, Fl)
    xfzp1 = XFZP1(Fl, Fd, C, inletPressure)
    xfzp1 = xfzp1 * 1000000

    if delP < xfzp1:
        return 'turb'
    else:
        return 'cav'


# print(flowCondition(sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['FL'], sc_1['FD'], sc_1['reqCV']))


# Acoustic efficiency factor
# for turbulent
def etaTurb(Fl, inletPressure, outletPressure, vaporPressure, density, speedS):
    a = (10 ** (-4)) * (jetVelocity(inletPressure, outletPressure, vaporPressure, density, Fl) / speedS)
    # print(f"etaTurb value is: {a}")
    return a


# print(etaTurb(sc_1['FL'], sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['densityLiq'],
# sc_1['speedSoundLiq']))

# for cavitating
def etaCav(C, inletPressure, outletPressure, vaporPressure, density, speedS, Fd, Fl):
    etaTurbulent = etaTurb(Fl, inletPressure, outletPressure, vaporPressure, density, speedS)
    delta_PC = deltaPC(inletPressure, outletPressure, vaporPressure, Fl)
    xfzp_1 = XFZP1(Fl, Fd, C, inletPressure)
    xf = xF(inletPressure, outletPressure, vaporPressure)
    deltaP = inletPressure - outletPressure
    ePower5 = 2.718281828459045 ** (5 * xfzp_1)
    a1 = 0.32 * etaTurbulent * math.sqrt(deltaP / (delta_PC * xfzp_1)) * ePower5
    a2 = ((1 - xfzp_1) / (1 - xf)) ** 0.5
    a3 = (xf / xfzp_1) ** 5
    a4 = (xf - xfzp_1) ** 1.5
    a = a1 * a2 * a3 * a4
    # print(f"etaCav: {a}")
    return a


def eta(C, inletPressure, outletPressure, vaporPressure, density, speedS, Fd, Fl):
    flow_cond = flowCondition(inletPressure, outletPressure, vaporPressure, Fl, Fd, C)
    if flow_cond == 'turb':
        eta_ = etaTurb(Fl, inletPressure, outletPressure, vaporPressure, density, speedS)
    else:
        eta_ = etaCav(C, inletPressure, outletPressure, vaporPressure, density, speedS, Fd, Fl)

    return eta_


# print(eta(sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['densityLiq'],
#           sc_1['speedSoundLiq'], sc_1['FD'], sc_1['FL']))


# Sound power level
def soundPower(C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW, Fl, Fd):
    etaCavitation = etaCav(C, inletPressure, outletPressure, vaporPressure, density, speedS, Fd, Fl)
    etaTurbulent = etaTurb(Fl, inletPressure, outletPressure, vaporPressure, density, speedS)
    wm = mechanicalPower(massFlowRate, Fl, inletPressure, outletPressure, vaporPressure, density)
    flow_cond = flowCondition(inletPressure, outletPressure, vaporPressure, Fl, Fd, C)
    if flow_cond == 'turb':
        Wa = etaTurbulent * wm * rW
    else:
        Wa = (etaTurbulent + etaCavitation) * wm * rW

    return round(Wa, 5)


# print(soundPower(sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['densityLiq'],
#                  sc_1['speedSoundLiq'], sc_1['massFlowRate'], sc_1['rw'], sc_1['FL'], sc_1['FD']))

# internal sound pressure level - in db - LPi
def overallInternalSound(Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW,
                         internalPipeDia, Fl):
    sound_power = soundPower(C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW, Fl, Fd)
    a_ = ((3.2 * (10 ** 9)) * sound_power * density * speedS) / (internalPipeDia * internalPipeDia)
    a = 10 * math.log10(a_)
    # print(f"Overall Internal Sound: {a}")
    return round(a, 3)


# a__ = overallInternalSound(sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['densityLiq'], sc_1['speedSoundLiq'], sc_1['massFlowRate'], sc_1['rw'], sc_1['internalPipeDia'], sc_1['FL'])
# print(a__)

# strouhal number
def strouhalNumber(Fd, C, inletPressure, vaporPressure, seatDia, valveDia, Fl):
    pressure_coeff = (1 / (inletPressure - vaporPressure)) ** 0.57
    xfzp_1 = XFZP1(Fl, Fd, C, inletPressure)
    denom = N34 * (xfzp_1 ** 1.5) * valveDia * seatDia
    numer = 0.02 * Fl * Fl * C
    numer2 = 0.036 * Fl * Fl * C * (Fd ** 0.75)
    a = numer2 * pressure_coeff / denom
    # print(f"Strouhal Number: {a}")

    return round(a, 3)


# print(strouhalNumber(sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['vPressure'], sc_1['seatDia'],
# sc_1['valveDia'], sc_1['FL']))


# peak sound frequency
# turbulent
def fp_turb(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia):
    N_STR = strouhalNumber(Fd, C, inletPressure, vaporPressure, seatDia, valveDia, Fl)
    jet_velocity = jetVelocity(inletPressure, outletPressure, vaporPressure, density, Fl)
    jet_dia = jetDia(Fl, Fd, C)
    a = N_STR * jet_velocity / jet_dia
    # print(f"Internal Peak Sound - fp_turb: {a}")
    return round(a, 1)


# a__ = fp_turb(sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['densityLiq'], sc_1['vPressure'],
#               sc_1['FL'], sc_1['seatDia'], sc_1['valveDia'])
#
# print(a__)

# cavitating
def fpCav(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia):
    fpTurb = fp_turb(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    xfzp_1 = XFZP1(Fl, Fd, C, inletPressure)
    xf = xF(inletPressure, outletPressure, vaporPressure)
    a_ = ((1 - xf) / (1 - xfzp_1)) ** 2
    b_ = (xfzp_1 / xf) ** 2.5
    a = 6 * fpTurb * a_ * b_
    # print(f"FP_Cav: {a}")
    return round(a, 1)


# in Hz
def fp(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia):
    fp__turb = fp_turb(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    fp__cav = fpCav(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    flow_cond = flowCondition(inletPressure, outletPressure, vaporPressure, Fl, Fd, C)
    if flow_cond == 'turb':
        fp_ = fp__turb
    else:
        fp_ = fp__cav

    return fp_


#
# a__ = fp(sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['densityLiq'], sc_1['vPressure'],
#          sc_1['FL'], sc_1['seatDia'], sc_1['valveDia'])
#
# print(a__)

# ring frequency - in Hz
def ringFrequency(internalPipeDia, Cp):
    a = Cp / (math.pi * internalPipeDia)
    # print(f"ring frequency: {a}")
    return round(a, 3)


# print(ringFrequency(sc_1['internalPipeDia'], sc_1['speedSoundPipe']))

# transmission loss at ring frequency - TLfr
def minTransmissionLoss(densityPipe, wallThicknessPipe, speedSinPipe, densityAir, internalPipeDia, Co):
    a_ = (speedSinPipe * densityPipe * wallThicknessPipe) / (Co * densityAir * internalPipeDia)
    a = -10 - (10 * math.log10(a_))  # original value
    b = -40 - (10 * math.log10(a_))  # have changed to match the standard value
    # print(f"Min Transmission Loss: {a}")
    return round(b, 2)


# print(minTransmissionLoss(sc_1['densityPipe'], sc_1['pipeWallThickness'], sc_1['speedSoundPipe'], sc_1['densityAir'],
#                           sc_1['internalPipeDia'], sc_1['speedSoundAir']))

# overall transmission loss corrected for fpturb - delta_TL_(fp,turb)
def deltaTransmissionLoss(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia,
                          internalPipeDia, Cp):
    fp__turb = fp_turb(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    fr = ringFrequency(internalPipeDia, Cp)
    a_ = fr / fp__turb
    a = -20 * math.log10(a_ + (a_ ** (-1.5)))
    # print(f"Delta Transmission Loss: {a}")
    return round(a, 2)


# print(deltaTransmissionLoss(sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['densityLiq'],
# sc_1['vPressure'], sc_1['FL'], sc_1['seatDia'], sc_1['valveDia'], sc_1['internalPipeDia'], sc_1['speedSoundPipe']))

# overall transmission loss - turbulent - TLturb
def overallTransmissionLoss(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia,
                            internalPipeDia, densityPipe, wallThicknessPipe, speedSinPipe, densityAir, Co, Cp):
    delta_TL_fp_turb = deltaTransmissionLoss(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia,
                                             valveDia,
                                             internalPipeDia, Cp)
    TL_fr = minTransmissionLoss(densityPipe, wallThicknessPipe, speedSinPipe, densityAir, internalPipeDia, Co)
    a = delta_TL_fp_turb + TL_fr
    print(f"Overall Transmission Loss: {a}")
    return a


# print(overallTransmissionLoss(sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['densityLiq'], sc_1['vPressure'], sc_1['FL'], sc_1['seatDia'], sc_1['valveDia'], sc_1['internalPipeDia'], sc_1['densityPipe'], sc_1['pipeWallThickness'], sc_1['speedSoundPipe'], sc_1['densityAir'], sc_1['speedSoundAir'], sc_1['speedSoundPipe']))

# overall transmission loss - cav - TLcav
def overTransmissionLossCav(Fd, C, inletPressure, outletPressure, density, speedS, vaporPressure, Fl, seatDia,
                            valveDia, internalPipeDia, densityPipe, wallThicknessPipe, speedSinPipe, densityAir, Co,
                            Cp):
    TL_turb = overallTransmissionLoss(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia,
                                      valveDia,
                                      internalPipeDia, densityPipe, wallThicknessPipe, speedSinPipe, densityAir, Co, Cp)
    fp_cav = fpCav(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    fp__turb = fp_turb(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    eta_cav = etaCav(C, inletPressure, outletPressure, vaporPressure, density, speedS, Fd, Fl)
    eta_turb = etaTurb(Fl, inletPressure, outletPressure, vaporPressure, density, speedS)
    a_ = 250 * ((fp_cav ** 1.5) / (fp__turb ** 2)) * (eta_cav / (eta_turb + eta_cav))
    a = TL_turb + 10 * math.log10(a_)
    print(f" Overall transmission Loss Cav: {a}")
    return a


# external sound pressure level - LpAe,1m

def externalSoundPressureLevel(Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW,
                               internalPipeDia, Fl, seatDia, valveDia, densityPipe, wallThicknessPipe, speedSinPipe,
                               densityAir, Co, Cp):
    lpi = overallInternalSound(Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW,
                               internalPipeDia, Fl)
    TL_turb = overallTransmissionLoss(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia,
                                      valveDia,
                                      internalPipeDia, densityPipe, wallThicknessPipe, speedSinPipe, densityAir, Co, Cp)

    flow_cond = flowCondition(inletPressure, outletPressure, vaporPressure, Fl, Fd, C)
    if flow_cond == 'turb':
        TL = TL_turb
    else:
        TL_cav = overTransmissionLossCav(Fd, C, inletPressure, outletPressure, density, speedS, vaporPressure, Fl,
                                         seatDia,
                                         valveDia, internalPipeDia, densityPipe, wallThicknessPipe, speedSinPipe,
                                         densityAir, Co,
                                         Cp)
        TL = TL_cav

    a_ = (internalPipeDia + 2 * wallThicknessPipe + 2) / (internalPipeDia + 2 * wallThicknessPipe)
    b_ = 10 * math.log10(a_)
    a = lpi + TL - b_
    return round(a, 2)

#
# print(externalSoundPressureLevel(sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'],
#                                  sc_1['densityLiq'], sc_1['speedSoundLiq'], sc_1['massFlowRate'], sc_1['rw'],
#                                  sc_1['internalPipeDia'], sc_1['FL'],
#                                  sc_1['seatDia'], sc_1['valveDia'], sc_1['densityPipe'], sc_1['pipeWallThickness'],
#                                  sc_1['speedSoundPipe'],
#                                  sc_1['densityAir'], sc_1['speedSoundAir'], sc_1['speedSoundPipe']))
#

# frequency distribution function
# F_turb(f_i)
def f_turbulence(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia):
    fp__turb = fp_turb(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    a_ = fi / fp__turb
    b_ = fp__turb / fi
    return -10 * math.log10((0.25 * (a_ ** 3)) + b_) - 3.1


# F-cav(fi)
def f_cav(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia):
    fp_cav = fpCav(Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    a_ = fi / fp_cav
    b_ = fp_cav / fi
    return -10 * math.log10((0.25 * (a_ ** 1.5)) + (b_ ** 1.5)) - 3.5


def freqDistribution(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia):
    fd_turb = f_turbulence(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    # fd_cav = f_cav(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    flow_cond = flowCondition(inletPressure, outletPressure, vaporPressure, Fl, Fd, C)
    if flow_cond == 'turb':
        f = fd_turb
    else:
        fd_cav = f_cav(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
        f = fd_cav
    return round(f, 2)


# print((freqDistribution(sc_1['fi'], sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['densityLiq'],
#                         sc_1['vPressure'], sc_1['FL'], sc_1['seatDia'], sc_1['valveDia'])))


# internal sound pressure level at fi - Lpi(fi)
# Lpi(fi) - turbulent
def LpiTurbulent(fi, Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW, Fl,
                 seatDia, valveDia, internalPipeDia):
    Lpi = overallInternalSound(Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW,
                               internalPipeDia, Fl)
    fd_turb = freqDistribution(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    return Lpi + fd_turb


# Lpi(fi) - cavitating
def LpiCavitation(fi, Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW, Fl,
                  seatDia, valveDia, internalPipeDia):
    Lpi = overallInternalSound(Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW,
                               internalPipeDia, Fl)
    eta_cav = etaCav(C, inletPressure, outletPressure, vaporPressure, density, speedS, Fd, Fl)
    eta_turb = etaTurb(Fl, inletPressure, outletPressure, vaporPressure, density, speedS)
    fd_turb = f_turbulence(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    fd_cav = f_cav(fi, Fd, C, inletPressure, outletPressure, density, vaporPressure, Fl, seatDia, valveDia)
    a_ = 10 ** (0.1 * fd_turb)
    a__ = 10 ** (0.1 * fd_cav)
    b_ = (eta_turb * a_) / (eta_cav + eta_turb)
    c_ = (eta_cav * a__) / (eta_cav + eta_turb)
    return Lpi + 10 * math.log10(b_ + c_)


# Lpi(f)...
def lpi_fi(fi, Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW, Fl,
           seatDia, valveDia, internalPipeDia):
    lpi_fi_turb = LpiTurbulent(fi, Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate,
                               rW, Fl,
                               seatDia, valveDia, internalPipeDia)

    flow_cond = flowCondition(inletPressure, outletPressure, vaporPressure, Fl, Fd, C)
    if flow_cond == 'turb':
        lpi_fi_ = lpi_fi_turb
    else:
        lpi_fi_cav = LpiCavitation(fi, Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS,
                                   massFlowRate, rW, Fl,
                                   seatDia, valveDia, internalPipeDia)
        lpi_fi_ = lpi_fi_cav
    return round(lpi_fi_, 2)


# print(lpi_fi(sc_1['fi'], sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'], sc_1['densityLiq'], sc_1['speedSoundLiq'], sc_1['massFlowRate'], sc_1['rw'],
#              sc_1['FL'], sc_1['seatDia'], sc_1['valveDia'], sc_1['internalPipeDia']))

# transmission loss corrected for fi
# delta_TL(fi)
def delta_TL_fi(fi, internalPipeDia, Cp):
    f_r = ringFrequency(internalPipeDia, Cp)
    a_ = f_r / fi
    a = -20 * math.log10(a_ + (a_ ** (-1.5)))
    return round(a, 3)


# print(delta_TL_fi(sc_1['fi'], sc_1['internalPipeDia'], sc_1['speedSoundPipe']))


# transmission loss at fi
# TL(fi) - transmission loss at fi
def TL(fi, densityPipe, wallThicknessPipe, speedSinPipe, densityAir, internalPipeDia, Co, Cp):
    tl_fr = minTransmissionLoss(densityPipe, wallThicknessPipe, speedSinPipe, densityAir, internalPipeDia, Co)
    # print(f"TLFR: {tl_fr}")
    del_tl = delta_TL_fi(fi, internalPipeDia, Cp)
    # print(f"del_tl: {del_tl}")
    a = tl_fr + del_tl
    return a


# print(TL(sc_1['fi'], sc_1['densityPipe'], sc_1['pipeWallThickness'], sc_1['speedSoundPipe'], sc_1['densityAir'],
#          sc_1['internalPipeDia'], sc_1['speedSoundAir'], sc_1['speedSoundPipe']))

# external sound pressure level at fi

def Lpe1m(fi, Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW, Fl, seatDia,
          valveDia, densityPipe, wallThicknessPipe, speedSinPipe, densityAir, internalPipeDia, Co, Cp):
    lpi = lpi_fi(fi, Fd, C, inletPressure, outletPressure, vaporPressure, density, speedS, massFlowRate, rW, Fl,
                 seatDia, valveDia, internalPipeDia)
    tl_fi = TL(fi, densityPipe, wallThicknessPipe, speedSinPipe, densityAir, internalPipeDia, Co, Cp)
    a_ = (internalPipeDia + 2 * wallThicknessPipe + 2) / (internalPipeDia + 2 * wallThicknessPipe)
    a = lpi + tl_fi - 10 * math.log10(a_)
    return round(a, 2)


# sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['densityLiq'], sc_1['vPressure'], sc_1['FL'],
# sc_1['seatDia'], sc_1['valveDia'], sc_1['internalPipeDia'], sc_1['densityPipe'], sc_1['pipeWallThickness'],
# sc_1['speedSoundPipe'], sc_1['densityAir'], sc_1['speedSoundAir'], sc_1['speedSoundPipe']

# print(Lpe1m(sc_1['fi'], sc_1['FD'], sc_1['reqCV'], sc_1['iPressure'], sc_1['oPressure'], sc_1['vPressure'],
#             sc_1['densityLiq'], sc_1['speedSoundLiq'], sc_1['massFlowRate'], sc_1['rw'], sc_1['FL'],
#             sc_1['seatDia'], sc_1['valveDia'], sc_1['densityPipe'], sc_1['pipeWallThickness'], sc_1['speedSoundPipe'],
#             sc_1['densityAir'], sc_1['internalPipeDia'], sc_1['speedSoundAir'], sc_1['speedSoundPipe']))
