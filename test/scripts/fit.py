#!/usr/bin/env python

import os, re, sys, optparse, commands, shutil, imp
import math, ROOT

tdrstyle = imp.load_source('tdrstyle', './tdrstyle.py')
CMS_lumi = imp.load_source('CMS_lumi', './CMS_lumi.py') 

def path_leaf(path):
    return path.strip('/').strip('\\').split('/')[-1].split('\\')[-1]


def Compare(fn1, fn2, hist, xlow, xhigh):

  ROOT.gROOT.SetBatch()
  ROOT.gROOT.SetStyle('Plain')
  ROOT.gStyle.SetOptTitle(0)
  ROOT.gStyle.SetOptStat(0000)
  ROOT.gStyle.SetOptFit(0111)
  ROOT.gStyle.SetErrorX(0.0001);

  f1 = ROOT.TFile(fn1,'READ')
  f2 = ROOT.TFile(fn2,'READ')

  fn1 = fn1[:-5]
  fn2 = fn2[:-5]

  fn1 = path_leaf(fn1)
  fn2 = path_leaf(fn2)

  print fn1,fn2

## Get Canvas
  c1 = f1.Get(fn1)
  c2 = f2.Get(fn2)

  print c1,c2
  p1 = c1.FindObject("pad0")
  p2 = c2.FindObject("pad0")

  if hist == "Data":
    hist1 = p1.GetPrimitive("Data")
    hist2 = p2.GetPrimitive("Data")
  else:

    hs1 = p1.GetPrimitive("hsbkg")
    hs2 = p2.GetPrimitive("hsbkg")

    hist1 = hs1.GetStack().FindObject(hist);
    hist2 = hs2.GetStack().FindObject(hist);

  c0 = ROOT.TCanvas(fn1+'_comp_'+hist,'',800,600)
  c0.cd()
  pad0 = ROOT.TPad("pad2","",0.0,0.3,1.0,1.0)
  pad1 = ROOT.TPad("pad1","",0.0,0.0,1.0,0.3)

  pad0.Draw()
  pad0.cd()
  pad1.SetBottomMargin(0.05)
  pad0.SetLogy()
 
  hist1        . SetLineStyle(1)
  hist1        . SetLineWidth(1)
  hist1        . SetFillColor(0)

  hist2        . SetLineStyle(7)
  hist2        . SetLineWidth(1)
  hist2        . SetFillColor(0)

  hist1  . SetLineColor(1)
  hist2  . SetLineColor(2)


  hist1.Draw("hist")
  hist2.Draw("histsame")


  pad0.RedrawAxis()

  pad0.Update()

  xmin = pad0.GetUxmin();
  ymin = min(hist1.GetMinimum(),hist2.GetMinimum());
  xmax = pad0.GetUxmax();
  ymax = max(hist1.GetMaximum(),hist2.GetMaximum());
  print " pad0 Uymax = ", ymax
  hist1.SetMaximum(ymax*5000)
  hist1.SetMinimum(0.1)

  leg = ROOT.TLegend(0.12,0.66,0.88,0.88,'','brNDC')
  leg.SetBorderSize(0)
  leg.SetFillColor(0)
  leg.SetTextSize(0.040)
  leg.SetMargin(0.2)
  leg.SetNColumns(4)
  leg.SetColumnSeparation(0.1)
  leg.SetEntrySeparation(0.1)
  leg.AddEntry(hist1      ,"Old            " , "l")
  leg.AddEntry(hist2       ,"New       " , "l")

  leg.Draw()

  c0.cd()

  pad1.Draw()
  pad1.cd()
  pad1.SetTopMargin(0.05)
  pad1.SetBottomMargin(0.3)

  hratio = hist1.Clone('hratio')
  hratio.Divide(hist2)


  hratio.GetXaxis().SetTitleSize(0.14)
  hratio.GetXaxis().SetLabelSize(0.14)
  hratio.GetXaxis().SetTickLength(hist1.GetXaxis().GetTickLength()*7/3)

  hratio.GetYaxis().SetTitle("Old/New")
  hratio.GetYaxis().SetTitleSize(0.14)
  hratio.GetYaxis().SetLabelSize(0.14)
  hratio.GetYaxis().SetTickLength(hist1.GetYaxis().GetTickLength())
  hratio.GetYaxis().SetTitleOffset(0.28)
  hratio.GetYaxis().SetNdivisions(504)

  hratio.Draw("e1")

  hratio.GetXaxis().SetRangeUser(xlow,xhigh)
  hratio.SetMinimum(0.1)
  hratio.SetMaximum(2)

  line = ROOT.TLine(xlow,1,xhigh,1)
  line.Draw()

  pad1.RedrawAxis()

  c0.cd()

  CMS_lumi.lumi_13TeV = "2.2/ fb"
  CMS_lumi.writeExtraText = 1
  CMS_lumi.extraText = "Preliminary"

  iPos = 0
  if( iPos==0 ): CMS_lumi.relPosX = 0.13

  CMS_lumi.CMS_lumi(c0, 4, iPos)
  c0.Update()

  c0.SaveAs('../Plots/'+c0.GetName()+'.pdf')
  c0.SaveAs('../Plots/'+c0.GetName()+'.root')
  c0.SaveAs('../Plots/'+c0.GetName()+'.C')



def DrawPresel(fin, hist, xlow, xhigh, doratiofit): 

  ROOT.gROOT.SetBatch()
  ROOT.gROOT.SetStyle('Plain')
  ROOT.gStyle.SetOptTitle(0) 
  ROOT.gStyle.SetOptStat(0000) 
  ROOT.gStyle.SetOptFit(0111) 
  ROOT.gStyle.SetErrorX(0.0001);
  
  fin = ROOT.TFile(fin,'READ')
  
  hdata      = fin.Get('Data')
  httjets    = fin.Get('TTJets')
  hsingletop = fin.Get('ST')
  hwjets     = fin.Get('WJets')
  hqcd       = fin.Get('histQCD')
  htp1200LH    = fin.Get('Tprime1200_LH')
 # htp1500LH    = fin.Get('Tp1500__'+hist)
 # htp1800LH    = fin.Get('Tp1800__'+hist)
  
  ndata      = hdata.Integral() 
  nttjets    = httjets.Integral() 
  nsingletop = hsingletop.Integral() 
  nwjets     = hwjets.Integral() 
  nqcd       = hqcd.Integral() 
  
  rescalescd = ndata - nttjets - nsingletop - nwjets
  
  hqcd.Scale(rescalescd/nqcd)
  
  hbkg = hqcd.Clone('kbkg')
  hbkg . Add(hsingletop) 
  hbkg . Add(httjets) 
  hbkg . Add(hwjets) 
  
  hratio = hdata.Clone('hratio')
  hratio.Divide(hbkg)
  
  fun = ROOT.TF1('fun','[0] + [1]*x', 1000, 3000)
  if doratiofit:
    fun.SetParameter(0,1.05)
    fun.SetParameter(1,-0.004)
    fun.SetParName(0,'intercept')
    fun.SetParName(1,'slope')
    fitres = hratio.Fit('fun', 'S')
    cov = fitres.GetCovarianceMatrix()
    fitres.Print('V')
    #fitres.Write()
  
  hdata       . SetMarkerStyle(20) 
  hdata       . SetLineStyle(1) 
  hdata       . SetLineWidth(2) 
  hdata       . SetLineColor(1)  
    
  hbkg        . SetLineStyle(1) 
  hbkg        . SetLineWidth(1) 
  hbkg        . SetLineColor(1)  
  hbkg        . SetFillColor(0)  
    
  hsingletop  . SetLineColor(46)  
  hwjets      . SetLineColor(36)  
  httjets     . SetLineColor(26)  
  hqcd        . SetLineColor(16)  
  
  htp1200LH     . SetLineColor(3)  
  #htp1800LH     . SetLineColor(4)  
  
  htp1200LH     . SetLineWidth(2)  
  #htp1800LH     . SetLineWidth(2)  
  
  htp1200LH     . SetLineStyle(1)  
  #htp1800LH     . SetLineStyle(2)  
  
  hsingletop  . SetFillColor(46)  
  hsingletop  . SetFillColor(46)  
  hwjets      . SetFillColor(36)  
  httjets     . SetFillColor(26)  
  hqcd        . SetFillColor(16)  
  
  htp1200LH     . SetFillColor(0)  
  #htp1800LH     . SetFillColor(0)  
  
  hratio      . SetMarkerStyle(20) 
  hratio      . SetLineStyle(1) 
  hratio      . SetLineWidth(2) 
  hratio      . SetLineColor(1)  
    
  hsbkg = ROOT.THStack('hsbkg','')
  hsbkg.Add(hsingletop)
  hsbkg.Add(hwjets)
  hsbkg.Add(httjets)
  hsbkg.Add(hqcd)
  
  c0 = ROOT.TCanvas('c_data_mc_'+hist,'',800,600)
  c0.cd()
  pad0 = ROOT.TPad("pad0","",0.0,0.3,1.0,1.0)
  pad1 = ROOT.TPad("pad1","",0.0,0.0,1.0,0.3)
  
  pad0.Draw() 
  pad0.cd()
  pad1.SetBottomMargin(0.05)
  pad0.SetLogy()
  
  hdata.GetXaxis().SetTitleSize(0.14*0.3/0.7)
  hdata.GetXaxis().SetLabelSize(0.14*0.3/0.7)
  
  hdata.GetYaxis().SetTitle("Events/ 40 GeV")
  hdata.GetYaxis().SetTitleSize(0.14*0.3/0.7)
  hdata.GetYaxis().SetLabelSize(0.14*0.3/0.7)
  hdata.GetYaxis().SetTitleOffset(0.28*7/3)
  
  hdata.Draw("e1")
  hsbkg.Draw('histsame')
  hbkg.Draw('histsame')
  hdata.Draw('e1same')
  htp1200LH.Draw('histsame')
  #htp1800LH.Draw('histsame')

  hdata.GetXaxis().SetRangeUser(xlow,xhigh)
  
  hdata.GetXaxis().SetTitle('')
  hdata.GetXaxis().SetLabelSize(0)

  pad0.RedrawAxis()
  
  pad0.Update()

  xmin = pad0.GetUxmin();
  ymin = hdata.GetMinimum();
  xmax = pad0.GetUxmax();
  ymax = hdata.GetMaximum();
  print " pad0 Uymax = ", ymax 
  hdata.SetMaximum(ymax*5000)
  hdata.SetMinimum(0.1)

  leg = ROOT.TLegend(0.12,0.66,0.88,0.88,'','brNDC')
  leg.SetBorderSize(0)
  leg.SetFillColor(0)
  leg.SetTextSize(0.040)
  leg.SetMargin(0.2)  
  leg.SetNColumns(4)
  leg.SetColumnSeparation(0.1)
  leg.SetEntrySeparation(0.1)
  leg.AddEntry(hdata      ,"Data            " , "ep")
  leg.AddEntry(hqcd       ,"Multijets       " , "fl")
  leg.AddEntry(hwjets     ,"W+jets          " , "fl")
  leg.AddEntry(htp1200LH    ,"M(T) = 1200 GeV " , "fl")
  leg.AddEntry(hbkg       ,"Total background" , "fl")
  leg.AddEntry(httjets    ,"t#bar{t}+jets   " , "fl")
  leg.AddEntry(hsingletop ,"Single top: tW  " , "fl")
  #leg.AddEntry(htp1800LH    ,"M(T) = 1800 GeV " , "fl")

  #if doratiofit:
  #  leg.AddEntry(fun        ,"Data/MC fit         " , "l" );

  leg.Draw()
  
  c0.cd()
  
  pad1.Draw() 
  pad1.cd()
  pad1.SetTopMargin(0.05)
  pad1.SetBottomMargin(0.3)
  
  hratio.GetXaxis().SetTitleSize(0.14)
  hratio.GetXaxis().SetLabelSize(0.14)
  hratio.GetXaxis().SetTickLength(hdata.GetXaxis().GetTickLength()*7/3)
  
  hratio.GetYaxis().SetTitle("Data/MC")
  hratio.GetYaxis().SetTitleSize(0.14)
  hratio.GetYaxis().SetLabelSize(0.14)
  hratio.GetYaxis().SetTickLength(hdata.GetYaxis().GetTickLength())
  hratio.GetYaxis().SetTitleOffset(0.28)
  hratio.GetYaxis().SetNdivisions(504)
  
  hratio.Draw("e1")

  hratio.GetXaxis().SetRangeUser(xlow,xhigh)
  hratio.SetMinimum(0.1)
  hratio.SetMaximum(2)

  if doratiofit:
    hratio.SetStats(1)
    pad1.cd()
    fun.Draw('sames')
    pad1.Update()
    #ROOT.gPad.Update()
    pavestats = hratio.FindObject("stats")
    pavestats.SetX1NDC(0.50)
    pavestats.SetX2NDC(0.88)
    pavestats.SetY1NDC(0.70)
    pavestats.SetY2NDC(0.92) 
    pavestats.SetBorderSize(0)
    pavestats.SetStatFormat('6.4f')
    pad1.Modified();  

  line = ROOT.TLine(xlow,1,xhigh,1)
  line.Draw()
  
  pad1.RedrawAxis()

  c0.cd()

  CMS_lumi.lumi_13TeV = "2.2/ fb"
  CMS_lumi.writeExtraText = 1
  CMS_lumi.extraText = "Preliminary"
  
  iPos = 0
  if( iPos==0 ): CMS_lumi.relPosX = 0.13
  
  CMS_lumi.CMS_lumi(c0, 4, iPos)
  c0.Update() 

  c0.SaveAs('../Plots/'+c0.GetName()+'.pdf')
  c0.SaveAs('../Plots/'+c0.GetName()+'.root')
  c0.SaveAs('../Plots/'+c0.GetName()+'.C')

def DrawPreselPlots():
  fin = 'Final_histograms_ana.root'
  hists = ['npv' 
          ,'Presel_HT'
          ,'Presel_NAK4'
          ,'Presel_NAK8'
          ,'Presel_ptAK8_0'
          ,'Presel_ptAK4_0'
          ,'Presel_ptAK4_1'
          ,'Presel_ptAK4_2'
          ,'Presel_ptAK4_3'
          ,'Presel_etaAK8_0'
          ,'Presel_etaAK4_0'
          ,'Presel_etaAK4_1'
          ,'Presel_etaAK4_2'
          ,'Presel_etaAK4_3'
          ]
  xlow  = [0 , 1000  ,-0.5  ,-0.5  ,100  ,0    ,0    ,0    ,0      ,-2.4 ,-5 ,-5 , -5 ,-5]
  xhigh = [40, 3000  ,20.5  ,10.5  ,1000 ,1000 ,1000 ,1000 ,1000   , 2.4 , 5 , 5 ,  5 , 5]
  for hist in hists:
    doratiofit=False
    if 'HT' in hist:
      doratiofit = True
    DrawPresel(fin, hist, xlow[hists.index(hist)], xhigh[hists.index(hist)], doratiofit)

#DrawPreselPlots()

