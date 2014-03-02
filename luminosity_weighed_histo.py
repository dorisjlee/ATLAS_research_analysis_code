#Histogram Script Weighted with luminosity calculation
from ROOT import *
import os
from array import array
debug=False
gROOT.Reset();
gStyle.SetOptStat(1111111);
c1 = TCanvas( ’c1’, ’c1’, 200, 10, 600, 400 )
hf = TFile( ’/home/doris/Desktop/H->tautauSignal/HtautauSignal_0428flag.root’ )
h = TH1F( ’h1’, ’H and Z mass (weighted)’, 150, 0., 300000.)
h.SetFillColor(11)
hchain=TChain(’t1’)
hchain.AddFile(’/home/doris/Desktop/H->tautauSignal/HtautauSignal_0428flag.root’)
entries = hchain.GetEntries()
mass=[]
#Drawing Higgs Histogram
h_weight_factor=1./(8.759e4)
for jentry in xrange(entries):
  ientry = hchain.LoadTree( jentry)
  if ientry < 0:
    break
  nb = hchain.GetEntry(jentry)
  if nb <= 0:
    continue
  mass.append(hchain.mass)
for x in mass:
  h.Fill(x,h_weight_factor)
h.Draw(’BAR1’)
#Drawing Z Histogram
zh = TH1F( ’z’, ’test’, 150, 0., 300000.)
zh.SetFillColor(1)
zf = TFile(’/home/doris/Desktop/tauSignal.root’)
zchain=TChain(’t1’)
zchain.AddFile(’/home/doris/Desktop/tauSignal.root’)
z_entries = zchain.GetEntries()
zmass=[]
z_weight_factor=1./32562411.342
for jentry in xrange(z_entries):
  ientry = hchain.LoadTree( jentry)
  if ientry < 0:
    break
  nb = hchain.GetEntry(jentry)
  if nb <= 0:
    continue
  mass.append(hchain.mass)
for x in mass:
  zh.Fill(x,z_weight_factor)
zh.Draw(’BAR1 SAME’)