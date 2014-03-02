from ROOT import *
import os
import glob
import math
from array import array
debug=False
gROOT.Reset();
gStyle.SetOptStat(1111111);
f = TFile( ’HtautauSignal_0428.root’, ’recreate’ )
t = TTree( ’t1’, ’testTree’)
mychain=TChain(’tau’)
os.chdir(’/home/doris/Desktop/mc12_8TeV.161576.PowHegPythia8_AU2CT10_ggH120_tautauhh.merge
.NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344_tid01108681_00’)
listing=os.listdir(’/home/doris/Desktop/mc12_8TeV.161576.PowHegPythia8_AU2CT10_ggH120_tautauhh.merge.
NTUP_TAU.e1217_s1469_s1470_r3542_r3549_p1344_tid01108681_00’)
a=len(listing)
for x in xrange(a):
  mychain.AddFile(listing[x])
  if debug:print listing[x]
entries = mychain.GetEntries()
v1=TLorentzVector()
v2=TLorentzVector()
#define flag array as int
flag=array(’i’,[0])
t1.Branch( ’flag’, flag, ’flag/i’ )
mass=array(’f’,[0])
t1.Branch(’mass’,mass, ’mass/F’)
for jentry in xrange(entries):
  # mass and flag array reset
  mass[0]=0
  flag[0]=0
  ientry = mychain.LoadTree( jentry)
  if ientry < 0:
    break
  nb = mychain.GetEntry(jentry)
  if nb <= 0:
    continue
  goodtau=[]
  for itau in xrange(mychain.tau_n):
    if debug: print "doing tau number ",itau
    if debug: print "pt is ",mychain.tau_pt[itau]
    if mychain.tau_n>=2 and mychain.tau_pt[itau]>=20000:
      goodtau.append(itau)
      if debug: print "I am adding a good tau to the list",itau
      if debug: print "the list is ",goodtau
  if len(goodtau)>1 :
    tau1 = goodtau[0]
    tau2 = goodtau[1]
    if debug: print "the good taus are numbers ",tau1,tau2
    if debug:print"the quality of tau is", mychain.tau_
16JetBDTSigLoose[tau1], mychain.tau_JetBDTSigLoose[tau2],mychain.tau_JetBDT
    SigMedium[tau1],mychain.tau_JetBDTSigMedium[tau2],
    mychain.tau_JetBDTSigTight[tau1], mychain.tau_JetBDTSigTight[tau2]
    #init
    flag[0]=1
    #flag corresponds to the highest (tightest) cut possible since same element value can overwrite the slot
    #ll
    if mychain.tau_JetBDTSigLoose[tau1]+mychain.tau_JetBDTSigLoose[tau2]==2:
      if debug:print "the taus pass ll "
      flag[0]=2
    #lm
    if mychain.tau_JetBDTSigLoose[tau1]+mychain.tau_JetBDTSigLoose[tau2]==2
    and mychain.tau_JetBDTSigMedium[tau1]+ mychain.tau_JetBDTSigMedium[tau2]>=1:
      if debug:print "the taus pass lm "
      flag[0]=3
    #mm
    if mychain.tau_JetBDTSigMedium[tau1]+ mychain.tau_JetBDTSigMedium[tau2]==2:
      if debug:print "the taus pass mm"
      flag[0]=4
    #lt
    if mychain.tau_JetBDTSigLoose[tau1]+ mychain.tau_JetBDTSigLoose[tau2]==2
    and mychain.tau_JetBDTSigTight[tau1]+mychain.tau_JetBDTSigLoose[tau2]>=1:
      if debug:print "the taus pass lt"
      flag[0]=5
    #mt
    if mychain.tau_JetBDTSigMedium[tau1]+mychain.tau_JetBDTSigMedium[tau2]==2
    and mychain.tau_JetBDTSigTight[tau1]+ mychain.tau_JetBDTSigTight[tau2]>=1:
      if debug:print "the taus pass mt "
      flag[0]=6
    #tt
    if mychain.tau_JetBDTSigTight[tau1]+mychain.tau_JetBDTSigTight[tau2]==2:
      if debug:print "the taus pass tt "
      flag[0]=7
    v1.SetPtEtaPhiM(mychain.tau_pt[tau1],mychain.tau_eta[tau1],mychain.tau_phi[tau1], mychain.tau_m[tau1])
    v2.SetPtEtaPhiM(mychain.tau_pt[tau2],mychain.tau_eta[tau2],mychain.tau_phi[tau2], mychain.tau_m[tau2])
    #mass calculation
    v=v1+v2
    taumass=v.M()
    tau=abs(taumass)
    print tau
    mass[0]=tau
    #keeping only entries with non zero mass and flag values
    if mass[0]==0 and flag[0]==0:
      continue
    else:
t1.Fill()
f.Write()
f.Close()