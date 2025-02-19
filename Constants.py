class ConstantsClass:
#Variables that have been set as an example, but are not real!!
    CLCruise = 0.45
    #ClMaxAirfoil is at an angle of attack of 12 degrees
    ClMaxAirfoil = 1.797
    ClClimb = 1.2
    ClTakeoff = 1.7
    #Clfl is used in landing field length
    Clfl = 0.6
    ClMaxEstimate = 2.1
    Cd0 = 0.01096
    AspectRatio = 10 
    OswaldFactor = 0.682
    StallSpeed = 70
    LandingAltitude = 1600
    LandingDensity = 1.04759
    RateOfClimb = 15
    Kt = 0.85
    FlapExtensionRatio = 1.21
    #ClMaxRatio is the ratio of CLmax of the wing to the ClMax of the airfoil
    ClMaxRatio = 0.82

    IterativeMass = 331660.47891014774
    #404691
    
#Known Values
    MachNum = 0.77
    ByPassRatio = 6
    CruiseSpeed = 228.3
    NumEngines = 2
    LandingLength = 1210
    TakeoffLength = 1296
    CVClimbGradient = 0.024
    dCLMaxWing = ClMaxEstimate - ClMaxAirfoil
    QuarterChordSweep = 24
    TaperRatio = 0.316
    dClMaxAirfoil = 1.3 * FlapExtensionRatio


#Mass Ratios (beta):
    MassRatio = 0.95
    MassRatioLanding = 0.845

#Less important constants
    SeaLevelTemperature = 288.15
    #Cruise Altitude: FL35000
    TemperatureAtCruise = 218.81
    PressureAtCruise = 23835.918
    DensityAtCruise = 0.3796
    #Climb Rate Altitude: 7400
    PressureAtClimb = 38800
    TemperatureAtClimb = 240
    DensityAtClimb = 0.563
    #Climb Gradient Altitude:1600m
    PressureAtClimbGrad = 83523.5
    TemperatureAtClimbGrad = 240
    DensityAtClimbGrad = 0.563

    #Climb Grad Requirements taken from CS-25 Certification Specifications * a safety factor (1.5)
    Cl25119 = 1.27
    Cd25119 = 0.059
    Oswald25119 = 0.868
    ClimbReq25119 = 0.038
    Cl25121a = 1.01
    Cd25121a = 0.0395
    Oswald25121a = 0.829
    ClimbReq25121a = 0.045
    Cl25121b = 1.013
    Cd25121b = 0.0395
    Oswald25121b = 0.829
    ClimbReq25121b = 0.036
    Cl25121c = 0.704
    Cd25121c = 0.02
    Oswald25121c = 0.79
    ClimbReq25121c = 0.018
    Cl25121d = 1.268
    Cd25121d = 0.059
    Oswald25121d = 0.829
    ClimbReq25121d = 0.0315
    
    CS25SafetyMargin = 1.5

    PressureAtTakeoff = 101325
    TemperatureAtTakeoff = 288.15
    DensityAtTakeoff = 1.225
    Gamma = 1.4

#Geometric Parameters
    FusL1 = 6.16
    FusL2 = 16.08
    FusL3 = 7.84
    FuselageDiameter = 2.8
    FinenessRatioFus = (FusL1 + FusL2 + FusL3)/FuselageDiameter
    TailS = 92/4 #WARNING!!
    TailTaperRatio = 0.3 #WARNING!!
    TailRootChord = 3.2 #WARNING!!
    TailThickToChord = 0.12 #WARNING!!

#IF Values (for class II drag estimation), as well as other misc parameters
    IFwing = 1.25 #for low wing
    IFtail = 1.045 #for conventional tail
    IFfus = 1 #NO IDEA LOL
    SurfaceKWing = 0.634 * 10*-5 #AN ESTIMATE
    SurfaceKTail = 0.634 * 10*-5 #AN ESTIMATE
    SurfaceKFuselage = 0.634 * 10*-5 #AN ESTIMATE
    PercentCd0DueToExcrecence = 1.035
    TechnologyFactorKa = 0.935 #FOR SUPERCRITICAL AIRFOILS


#VERSIONS: 

Constants = ConstantsClass()
