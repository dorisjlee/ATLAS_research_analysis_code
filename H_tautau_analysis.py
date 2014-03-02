from ROOT import *
import os
from array import array
#debug=False
gROOT.Reset();
gStyle.SetOptStat(1111111);
f = TFile( ’/home/doris/Desktop/H->tautauSignal/HtautauSignal_0428flag.root’ )
newF=TFile(’H->tautauSignal0516Analysis.root’,’update’)
newT=TTree (’analysis7’,’analysisTree’)
mychain=TChain(’t1’)
mychain.AddFile(’/home/doris/Desktop/H->tautauSignal/HtautauSignal_0428flag.root’)
entries = mychain.GetEntries()
#init
tt = array( ’f’, [ 0 ] )
newT.Branch( ’tau_tt’, tt, ’tau_tt/F’ )
for jentry in xrange(entries):
  tt[0]=0
  ientry = mychain.LoadTree( jentry)
  if ientry < 0:
    break
  nb = mychain.GetEntry(jentry)
  if nb <= 0:
    continue
  #Get number of entries that passes tt (Can be modified for different purposes)
  if mychain.flag >=7:
    print mychain.mass
    tt[0]=mychain.mass
    if debug:print tt[0]
  if tt[0]==0:
    continue
  else:
    newT.Fill()
newF.Write()
newT.GetEntries()
#newT.Scan("tau_m_tt")
#newT.Fit(’gaus’,’tau_m_tt’)
f.Close()
newF.Close()
