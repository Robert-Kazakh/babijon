from django.shortcuts import render
import math

def calculation(request):
    return render(request,'main/calculation.html')

def base(request):
    Nmax = int(request.GET["Nmax"])
    Nmin = int(request.GET["Nmin"])
    Tperobt = int(request.GET["Tperobt"])
    tT = int(request.GET["tT"])
    deltat = int(request.GET["deltat"])
    AB = request.GET["AB"]
    if AB =="LiIon":
        kpd = 0.9
    elif AB =="NiCd":
        kpd =0.85
    elif AB =="NiH2":
        kpd=0.8
    elif AB == "NiMH":
        kpd =0.75
    h = int(request.GET["h"])
    tlet = int(request.GET["tlet"])
    fi1 = int(request.GET["fi1"])
    fi2 = int(request.GET["fi2"])
    SB = request.GET["SB"]
    if SB =="Kremnii":
        kpdSB =0.18
    elif SB == "AG":
        kpdSB = 0.265
    elif SB == "FI":
        kpdSB = 0.19
    Kzap = float(request.GET["Kzap"])
    gammamsb = int(request.GET["gammamsb"])
    qc= 1396
    Tsolar = (Tperobt - tT);
    Nps = ((Nmin * Tsolar + deltat * (Nmax - Nmin)) / Tperobt);
    Nsb = ((((Nmin * tT) + Nmax * deltat) / Tsolar * kpd) + Nmin);
    if 200 < h < 500:
        kd = 0.08
    elif 500 < h < 3000:
        kd = (0.08 + (0.22 * (h - 500)) / 2500)
    elif 3001 < h < 36000:
        kd = ((0.3 - 0.1 * (h - 3000)) / 17000)
    elif 36000 < h:
        kd = 0.1
    Nprsb = (Nsb * (1 + kd * tlet)) / (math.cos(fi1 * 0.0175) * math.cos(fi2 * 0.0175))
    Ssb = (Nprsb / (qc * Kzap * kpdSB))
    return render(request,'main/base.html',{"Tsolar":Tsolar,"Nps":Nps,"Nsb":Nsb,"Nprsb":Nprsb,"Ssb":Ssb})